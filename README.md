# ASA International Data Quest 2025 — "The EU Effect"

## Overview

Team entry for **ASA International Data Quest 2025 (Türkiye)**, METU.  
Research question:

> **Does EU membership correlate with stronger macroeconomic and social development
> outcomes compared to non-member peers from the same region?**

We compare three EU members (Czech Republic, Poland, Slovakia) against three
non-members (Russia, Belarus, Ukraine) using World Bank WDI data spanning 1990–2024.

**Team:** Samuil Datsenko, Petr Datsenko, Elizaveta Polyakova, Vladislav Pulin

---

## Key Findings

- **GDP per capita (PPP):** EU group sustained a ~15–20% advantage over non-EU
  peers by 2024, with divergence accelerating post-2004 accession
- **Trade openness:** EU group trade-to-GDP ratio roughly doubled post-accession;
  non-EU group stagnated and declined
- **Internet adoption:** EU members established a decade-long lead,
  converging only by ~2022

---

## Methodology

**Modeling (Python — `notebooks/00_did_analysis.ipynb`):**
- Two-way fixed-effects DiD: `GDP_growth ~ treat + C(country_code) + C(year)`
  with cluster-robust SEs by country
- Event-study design with relative-year dummies (leads/lags around 2004 accession)
- FDI interaction model: `GDP_growth ~ FDI_share * Post + C(country_code) + C(year)`
- Robustness check excluding Ukraine conflict years (2014, 2022)

**Visualization (R — `scripts/`):**
- Population-weighted group means across 1990–2024
- Pre/post-2004 t-tests on GDP growth rates
- Event markers: EU enlargement (2004), Global Financial Crisis (2008),
  Crimea annexation (2014), Russia–Ukraine war (2022)

**Data:** World Bank WDI — `NY.GDP.PCAP.PP.KD`, `NE.TRD.GNFS.ZS`, `IT.NET.USER.ZS`

---

## Repository Structure

```
├── data/
│   ├── raw/                  # Original WDI CSVs (read-only)
│   └── processed/            # Cleaned datasets
├── notebooks/
│   ├── 00_did_analysis.ipynb         # DiD & event-study models (main analysis)
│   ├── 01_poverty_headcount.ipynb    # Poverty headcount analysis
│   ├── 02_net_migration.ipynb        # Net migration analysis
│   └── 03_life_expectancy.ipynb      # Life expectancy analysis
├── scripts/
│   └── downloadRawData.py            # WDI data download
├── docs/                             # Project documentation
└── env/
    └── requirements.txt              # Python dependencies
```

---

## Deliverables

- [▶ Watch the project presentation](https://youtu.be/8o2hoTEMNlg)
- Slide deck: 4 content slides + cover + references
- 5-minute video submission (submitted October 31, 2025)
