# Structural MRI segmentation report

## Objective

To demonstrate a reproducible single-subject structural MRI processing workflow
using CAT26 and SPM25.

## Data

A T1-weighted structural MRI image from participant `sub-01`, session
`ses-test`, from OpenNeuro dataset `ds000114` was processed.

## Software environment

- MATLAB R2025b
- SPM25 25.01.02
- CAT26.0.rc3, build 3250
- macOS on Apple Silicon
- MATLAB architecture: maca64

## Methods

The T1-weighted image was processed with CAT tissue segmentation. The workflow
included bias-field correction, tissue classification, spatial normalization
and modulation.

The principal VBM outputs were:

- Modulated normalized grey matter: `mwp1`
- Modulated normalized white matter: `mwp2`
- Grey matter smoothed using a 6 mm FWHM Gaussian kernel: `s6mwp1`

## Global volumes

| Tissue | Volume (cm³) | Relative volume |
|---|---:|---:|
| Grey matter | 510 | 43.8% |
| White matter | 384 | 32.9% |
| Cerebrospinal fluid | 271 | 23.3% |
| Total intracranial volume | 1166 | 100.0% |

## Image quality

| Measure | Value | Rating |
|---|---:|---|
| Resolution | 82.82 | B- |
| Edge contrast | 69.79 | D+ |
| Noise contrast | 80.88 | B- |
| Inhomogeneity contrast | 86.14 | B |
| Fast Euler characteristic | 89.77 | B+ |
| Weighted average quality | 77.86 | C+ |

Processing time was approximately 5.58 minutes (5 minutes 35 seconds).

## Interpretation

The segmentation completed successfully and generated the expected normalized
and modulated tissue maps. The C+ global quality category requires visual review
but does not by itself indicate processing failure.

## Reproducibility note

The quantitative CAT outputs archived in this repository were validated against
the original CAT XML, log and PDF report. The original large CAT NIfTI
derivatives (`p0`, `mwp1`, `mwp2` and `s6mwp1`) are not distributed in this
repository and were not available on the Linux cross-audit workstation.
Figures derived from those files are therefore retained as archived CAT
processing outputs rather than claimed as newly regenerated results.

The original-T1 figure was regenerated during the cross-audit from the verified
source T1 using `scripts/make_original_t1_figure.py`, preserving physical voxel
aspect ratios and avoiding the crosshairs of the historical SPM screenshot.

The archived CAT quality-report image displays a processing-time field of
05:14 min, whereas the original CAT XML and text log both state that CAT
preprocessing took 5 minutes 35 seconds. The public numerical table reports
5.58 minutes from the XML/log evidence; both original provenance records are
retained rather than silently reconciled.

## Limitations

A single participant cannot support inferential VBM statistics.
