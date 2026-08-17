#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the clean three-plane original T1 figure used in the "
            "CAT26 single-subject portfolio."
        )
    )
    parser.add_argument(
        "--t1",
        required=True,
        type=Path,
        help="Input T1-weighted NIfTI (.nii or .nii.gz).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            Path(__file__).resolve().parents[1]
            / "results"
            / "figures"
            / "fig2_original_t1.png"
        ),
        help="Output PNG.",
    )

    args = parser.parse_args()

    if not args.t1.is_file():
        raise FileNotFoundError(args.t1)

    img = nib.load(str(args.t1))
    can = nib.as_closest_canonical(img)

    axcodes = nib.aff2axcodes(can.affine)
    if axcodes != ("R", "A", "S"):
        raise RuntimeError(
            f"Unexpected canonical orientation: {axcodes}"
        )

    data = np.asarray(can.dataobj, dtype=np.float32)
    data = np.where(np.isfinite(data), data, 0)

    sx, sy, sz = (
        float(x)
        for x in can.header.get_zooms()[:3]
    )

    positive = data[data > 0]
    if positive.size == 0:
        raise RuntimeError("T1 contains no positive voxels")

    vmin, vmax = np.percentile(
        positive,
        [1.0, 99.5],
    )

    mask = data > np.percentile(positive, 10.0)
    coords = np.argwhere(mask)

    if coords.size == 0:
        raise RuntimeError("Foreground mask is empty")

    lo = coords.min(axis=0)
    hi = coords.max(axis=0)

    center = np.round(
        (lo + hi) / 2
    ).astype(int)

    x = int(center[0])
    y = int(center[1])

    # Slightly superior axial slice gives useful ventricular,
    # cortical and deep-gray anatomical context.
    z = int(
        round(
            lo[2]
            + 0.58 * (hi[2] - lo[2])
        )
    )

    sagittal = np.rot90(data[x, :, :])
    coronal = np.rot90(data[:, y, :])
    axial = np.rot90(data[:, :, z])

    panels = [
        (
            "Sagittal",
            sagittal,
            sy * data.shape[1],
            sz * data.shape[2],
        ),
        (
            "Coronal",
            coronal,
            sx * data.shape[0],
            sz * data.shape[2],
        ),
        (
            "Axial",
            axial,
            sx * data.shape[0],
            sy * data.shape[1],
        ),
    ]

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(12.8, 4.8),
    )

    for ax, (
        title,
        slc,
        width_mm,
        height_mm,
    ) in zip(axes, panels):
        ax.imshow(
            slc,
            cmap="gray",
            vmin=vmin,
            vmax=vmax,
            interpolation="nearest",
            extent=[
                0,
                width_mm,
                0,
                height_mm,
            ],
            aspect="equal",
        )

        ax.set_title(
            title,
            fontsize=13,
        )
        ax.set_xlim(0, width_mm)
        ax.set_ylim(0, height_mm)
        ax.axis("off")

    fig.suptitle(
        "Original T1-weighted MRI — sub-01 / ses-test",
        fontsize=15,
        y=0.97,
    )

    fig.tight_layout(
        rect=[0, 0, 1, 0.92]
    )

    args.output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    fig.savefig(
        args.output,
        dpi=220,
        bbox_inches="tight",
        facecolor="white",
    )

    plt.close(fig)

    print(f"T1={args.t1}")
    print(f"T1_SHA256={sha256(args.t1)}")
    print(f"AXCODES={axcodes}")
    print(f"SHAPE={can.shape}")
    print(
        "VOXEL_SIZES_MM="
        f"{(sx, sy, sz)}"
    )
    print(f"SLICES={(x, y, z)}")
    print(
        "DISPLAY_RANGE="
        f"{(float(vmin), float(vmax))}"
    )
    print(f"OUTPUT={args.output}")
    print(
        "OUTPUT_SHA256="
        f"{sha256(args.output)}"
    )


if __name__ == "__main__":
    main()
