# Ethics and Reproducibility

## Principles (ASA Ethical Guidelines)
- **Transparency:** disclose data source, transformations, and assumptions.
- **Integrity:** avoid cherry-picking or data manipulation.
- **Respect:** interpret results responsibly; avoid harmful generalizations.
- **Uncertainty:** always communicate limitations and confidence intervals.
- **Reproducibility:** allow others to replicate results exactly.

## Implementation in This Project
- Data license: CC BY 4.0 (World Bank WDI).
- Each notebook outputs fixed-seed results.
- Environment defined via `requirements.txt` and virtual environment instructions.
- All figures regenerated via scripts; no manual edits.
- Ethical Appendix (summary slide) explicitly mentions these commitments.

## Risks & Mitigation
| Risk | Mitigation |
|------|-------------|
| Misinterpretation of correlation as causation | Emphasize “association,” not “causality.” |
| Omitted uncertainty | Display CIs and residual variability. |
| Reproducibility drift | Freeze dependencies; include random seeds. |
| Attribution omission | Citation on every slide and report. |