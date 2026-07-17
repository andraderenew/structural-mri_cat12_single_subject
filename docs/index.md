# Project documentation

This repository documents a single-subject structural MRI workflow using CAT26
and SPM25.

## Workflow

T1-weighted MRI → bias correction → tissue segmentation → spatial normalization
→ modulation → quality control → 6 mm grey-matter smoothing.

## Relevant files

- `reports/report.md`: scientific processing report
- `reports/catreport_*.pdf`: CAT quality-control report
- `results/tables/`: tissue-volume and image-quality tables
- `results/figures/`: visual processing outputs
- `scripts/`: MATLAB processing and visualization scripts
- `env/TOOL_VERSIONS.md`: computational environment

Raw NIfTI images and CAT derivative volumes are excluded from version control.
