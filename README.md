# ASA International Data Quest 2025 — World Development Indicators Project

## Overview

This repository contains our team's entry for the **ASA International Data Quest 2025 (Türkiye)**.  
We explore the **World Bank's World Development Indicators (WDI)** to answer:

> **Do countries that expand renewable energy use experience cleaner air and longer life expectancy?**

---

## Project Structure

```
cirsDataSet/
│
├── data/
│   ├── raw/                  # Original WDI CSVs (read-only, not modified)
│   └── processed/            # Cleaned datasets ready for analysis
│
├── docs/                     # Project documentation
│   ├── analysis_strategy.md           # Step-by-step analytical workflow
│   ├── dataset_overview.pdf           # WDI variable descriptions
│   ├── ethics_reproducibility.md      # Transparency and fairness guidelines
│   ├── project_schedule.md            # Timeline, roles, and milestones
│   └── visualization_guidelines.md    # Chart design standards
│
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory data analysis and visualizations
│   ├── 02_model_fe.ipynb     # Fixed-effects regression models
│   └── 03_backup_xgb.ipynb   # XGBoost explainability analysis (backup)
│
├── src/
│   ├── etl/                  # Data extraction, transformation, and loading
│   ├── models/               # Model training and evaluation scripts
│   └── viz/                  # Reusable plotting and chart generation functions
│
├── reports/
│   ├── figures/              # Exported plots (PNG, SVG) for publication
│   ├── slides/               # Presentation slide deck files
│   └── video/                # Final 5-minute video submission
├── scripts/
│   ├── downloadRawData.py    # Script that downloads archive
│
├── env/
│   ├── requirements.txt      # Python package dependencies (uv-compatible)
│   └── setup_instructions.md # Environment setup and installation guide
│
├── .gitignore                # Files and folders to exclude from version control
└── README.md                 # Project overview and quick start guide
```

---

## Quick Start

[instructions for set up](env/setup_instructions.md)
---

## Documentation

| Document | Description |
|----------|-------------|
| [Analysis Strategy](docs/analysis_strategy.md) | Step-by-step workflow from EDA to modeling |
| [Ethics & Reproducibility](docs/ethics_reproducibility.md) | Transparency and fairness guidelines |
| [Visualization Guidelines](docs/visualization_guidelines.md) | Chart design and accessibility standards |
| [Project Schedule](docs/project_schedule.md) | Timeline, roles, and risk management |
| [Dataset Overview](docs/dataset_overview.pdf) | WDI data description and variables |

---

## Workflow

1. **Data ingestion** → merge WDI tables, clean, check missingness
2. **Exploration** → visualize trends by region and income group
3. **Modeling** → estimate fixed-effects relationships
4. **Visualization** → produce publication-quality charts
5. **Ethics & QA** → verify transparency and reproducibility
6. **Deliverables** → slides + video (by Oct 31, 2025)

---

## Deliverables

- 5-minute video presentation
- Slide deck (4 content slides + cover/references)
- Reproducibility documentation
- Code + data bundle

## Presentation
[▶ Watch the project presentation](https://youtu.be/8o2hoTEMNlg)
