# Analysis Strategy

## 1. Purpose
Transform WDI data into interpretable, evidence-based insights connecting energy, air quality, and health.

## 2. Data Preparation
- Combine `WDICSV.csv` with country (`WDICountry.csv`) and series (`WDISeries.csv`) metadata.
- Filter indicators:
  - Life expectancy (SP.DYN.LE00.IN)
  - PM2.5 (EN.ATM.PM25.MC.M3)
  - Renewables share (EG.ELC.RNEW.ZS)
  - GDP per capita (NY.GDP.PCAP.PP.KD)
- Restrict years: 2000–2023, drop >40 % missing.

## 3. Exploratory Data Analysis
- Coverage heatmap: indicator × year non-null matrix.
- Trends: small-multiples per region.
- Cross-section scatter (LE vs GDPpc).
- Correlation heatmap for main variables.

## 4. Modeling
**Primary:** Fixed-effects panel regression (country + year FE).  
**Backup:** Cross-sectional LASSO or XGBoost for explainable global model.

## 5. Diagnostics
- Residual plots, Cook’s distance.
- VIF < 5 for multicollinearity.
- Cluster-robust SEs.
- Placebo: shuffle renewables within region-year.

## 6. Output
- β-coefficients with 95 % CIs.
- Country residual map.
- Robustness tables.

## 7. Reproducibility
- Deterministic random seed.
- All code in `/src/` with modular functions.
- Jupyter notebooks numbered and documented.