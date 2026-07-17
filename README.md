# Structural MRI segmentation with CAT26 and SPM25

Single-subject structural MRI processing project using CAT26 and SPM25.

The project demonstrates tissue segmentation, spatial normalization, modulation,
quality control, extraction of global tissue volumes, and preparation of grey
matter images for voxel-based morphometry (VBM).

## Dataset

- Source: OpenNeuro dataset `ds000114`
- Participant: `sub-01`
- Session: `ses-test`
- Modality: T1-weighted structural MRI
- Input: `sub-01_ses-test_T1w.nii`

Raw neuroimaging data are excluded from GitHub.

## Software

- MATLAB R2025b
- SPM25 (`25.01.02`)
- CAT26 (`26.0.rc3`, build 3250)
- Platform: macOS, Apple Silicon
- MATLAB architecture: `maca64`

## Processing workflow

1. Visual inspection of the T1-weighted image
2. CAT tissue segmentation
3. Bias-field correction
4. Spatial normalization
5. Tissue modulation
6. CAT quality-control report
7. Extraction of GM, WM, CSF and TIV
8. Gaussian smoothing of modulated grey matter with 6 mm FWHM

## Global tissue volumes

| Measure | Volume (cm³) | Percentage |
|---|---:|---:|
| Total intracranial volume | 1166 | 100.0 |
| Grey matter | 510 | 43.8 |
| White matter | 384 | 32.9 |
| Cerebrospinal fluid | 271 | 23.3 |

## Quality control

The CAT weighted-average image-quality score was **77.86%**, corresponding to
category **C+**. The segmentation was also inspected visually.

## Scope and limitations

This is a single-subject processing demonstration. It does not perform
population-level statistical inference.

## Author

Rene Andrade Rey

- GitHub: `andraderenew`
- ORCID: `0000-0001-5627-579X`
