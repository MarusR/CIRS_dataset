# Research Plan: Economic and Social Divergence in Post-Soviet Slavic Countries Following EU Integration

This document presents a structured, decision-oriented plan built around the **Post-Soviet Slavic / EU-integration** theme.  
It outlines (1) plausible conclusions, and (2) a set of **distinct, non-overlapping research questions**, each with indicators, plots, and statistical methods (OLS/LSE, MLE/GLM, DiD, FE, etc.), plus pitfalls to avoid.

---

## Likely, Defensible Conclusions (Working Hypotheses)

1. **EU entrants (POL, CZE, SVK)** show **stronger, more stable GDP-per-capita growth** post-2004/2007, accompanied by **higher FDI inflows (% GDP)** and **lower unemployment**—with a visible dip in 2008–09 and rebound afterward.  
2. **Non-EU (RUS, UKR, BLR)** exhibit **greater macro volatility**; **UKR** experiences clear disruptions after **2014** (conflict shock) and **2022** (if covered).  
3. **Poverty headcount** declines faster in EU entrants; **net migration** turns more positive/less negative relative to non-EU peers after 2004–2007 (opportunity effects).  
4. **CO₂ intensity (CO₂/GDP)** improves more in EU entrants, consistent with **rising renewables shares** under EU policy alignment; **absolute CO₂ (kt)** may still rise or flatten depending on industry mix.  
5. **Life expectancy** improves steadily in EU entrants but stagnates or reverses in non-EU states during crisis/conflict windows.  

> All of the above are **associations**, not causality proofs.  
> EU membership is a **bundle** (funds, market access, acquis reforms); careful **DiD/event-study** designs help isolate timing-coincident changes.

---

## Questions that Move the Ball (Each Adds a New Insight)

**Countries:**  
EU: *POL, CZE, SVK*  
Non-EU: *RUS, UKR, BLR*  

**Years:** 1990–2024 (suggested working window: 1995–2023 for stability).  
**Indicators:** GDP per capita, GDP growth, FDI%GDP, Unemployment (ILO), Life expectancy, Poverty $3/day (PPP), CO₂ (kt), Renewables %TFEC, Net migration.  
Use **interest_rate.csv** as a macro control where possible.

---

### Q1. Did EU accession coincide with a structural shift in GDP-per-capita growth?

- **Purpose:** Test macro divergence linked to 2004/2007 enlargements.  
- **Plot:** *Event-study lines* (year 0 = accession) of GDP growth; group means ±95 % CI.  
- **Method:** **Difference-in-Differences (DiD)** with country and year fixed effects (LSE/OLS):

  $$
  y_{c,t} = \alpha_c + \delta_t + \beta (EU_c \times Post_t) + \gamma X_{c,t} + \varepsilon_{c,t}
  $$

  - *y*: GDP growth  
  - *EU₍c₎*: entrants indicator  
  - *Post₍t₎*: t ≥ 2004/2007  
  - *X*: controls (interest rate, global cycle)

- **Test:** $H_0: \beta = 0$ (no differential post-trend).  
- **Expected sign:** $\beta > 0$.  
- **Pitfall:** Check **parallel-trends** assumption; show **pre-trend** coefficients.

---

### Q2. Is FDI %GDP a robust predictor of GDP growth—and did its role change after accession?

- **Purpose:** Mechanism probe (capital, know-how).  
- **Plot:** *Partial-residu1al scatter* (growth vs FDI %GDP) with LOESS by period (pre/post).  
- **Method:** **Panel FE OLS** (within estimator; LSE) + interaction with Post:

    $$
    y_{c,t} = \alpha_c + \delta_t + \beta_1 \text{FDI}_{c,t} + \beta_2 (\text{FDI}_{c,t} \times \text{Post}_t) + \varepsilon_{c,t}
    $$

- **Test:** $H_0: \beta_1 = \beta_2 = 0$.  
- **Expected:** Positive $\beta_1$; larger post-accession.  
- **Pitfall:** Simultaneity (growth → FDI); include **lagged FDI**.

---

### Q3. Did unemployment converge faster in EU entrants, conditional on growth and FDI?

- **Purpose:** Assess social outcomes beyond GDP.  
- **Plot:** *Small-multiples* of unemployment trends + *slopegraph* 2000→2010→2020.  
- **Method:** **FE OLS** with growth and FDI controls; cluster-robust SE by country.  
- **Test:** Entrant × Post on unemployment; $H_0: \beta=0$.  
- **Expected:** Faster decline in entrants.  
- **Pitfall:** ILO model uncertainty in early 1990s → start 1995+.

---

### Q4. Did poverty headcount ($3/day PPP) fall more rapidly in EU entrants?

- **Purpose:** Distributional effects.  
- **Plot:** *Percent-change bars* (2000→latest) with bootstrap CIs.  
- **Method:** **FE OLS** on Δ poverty (first difference), controls = GDPpc growth + unemployment.  
- **Test:** DiD on poverty change; $H_0:\beta=0$.  
- **Expected:** Larger decline in entrants.  
- **Pitfall:** Missingness—interpolate ≤ 2-year gaps.

---

### Q5. Did life-expectancy gains accelerate in EU entrants, controlling for GDPpc and unemployment?

- **Purpose:** Health outcome plausibly tied to institutions/environment.  
- **Plot:** Trend lines (pre/post markers); event-study coefficients for entrants.  
- **Method:** **FE OLS** on Δ life expectancy; controls = log GDPpc + unemployment (+ PM2.5 optional).  
- **Test:** Entrant × Post; $H_0:\beta=0$.  
- **Expected:** Positive, modest.  
- **Pitfall:** Conflict years (UKR 2014/2022); add dummies or omit.

---

### Q6. Did renewables %TFEC and CO₂ intensity (CO₂/GDP) improve faster in EU entrants?

- **Purpose:** Sustainability pathway.  
- **Plot:** *Bivariate slopegraph* (Δ Renewables vs Δ CO₂/GDP); *quad plot* by country.  
- **Method:** **Seemingly-Unrelated Regressions (SUR)** or two separate FE OLS on Δ Renewables and Δ (CO₂/GDP).  
- **Test:** Group difference in mean Δs (Wald test).  
- **Expected:** Entrants ↑ Renewables, ↓ CO₂ intensity.  
- **Pitfall:** Normalize CO₂ by GDP and/or population.

---

### Q7. Did net-migration dynamics diverge in sign and volatility after accession?

- **Purpose:** Human-capital flow signal.  
- **Plot:** *Distribution ribbons* of net migration (per 1 000) by group and period; *spike chart* around 2004/2007/2014.  
- **Method:** **Poisson or NegBin GLM (MLE)** for counts or FE OLS for rates.  
- **Test:** Entrant × Post coefficient; check over-dispersion.  
- **Expected:** Entrants trend less negative/more positive; UKR large negative post-2014.  
- **Pitfall:** Definition differences in modeled migration; document metadata.

---

### Q8. Are macro cycles (interest rates) mediating unemployment and migration differently across groups?

- **Purpose:** Rule out “it’s just the cycle.”  
- **Plot:** *Rolling 5-year correlations* between interest rate and unemployment/migration.  
- **Method:** **Panel FE** adding interest rates; **Chow/Bai-Perron** break tests (2008, 2014).  
- **Test:** Break-test $H_0$: no structural break.  
- **Expected:** Stronger cyclical sensitivity outside EU.  
- **Pitfall:** Harmonize rate definitions (policy vs market).

---

### Q9. Is there long-run cointegration between GDPpc and FDI %GDP within groups?

- **Purpose:** Long-horizon mechanism check.  
- **Plot:** *Residual plots* from Engle-Granger step 1 + ADF tests on residuals.  
- **Method:** **Engle-Granger cointegration** per country; meta-analyze by group.  
- **Test:** ADF $H_0$: unit root (no cointegration).  
- **Expected:** More cointegration in entrants.  
- **Pitfall:** Need ≥ 20–25 annual obs.

---

### Q10. Did variance of GDP growth and unemployment shrink in entrants (stabilization effect)?

- **Purpose:** Institutions as variance-reducers.  
- **Plot:** *Before/after boxplots* of country-level variance; *ridge plot* of volatility.  
- **Method:** **F-tests (variance ratios)** + **Levene’s test** for group equality.  
- **Test:** $H_0:$ equal variances.  
- **Expected:** Lower volatility post-accession.  
- **Pitfall:** Small N; treat as exploratory.

---

## Specific Graphs to Produce (High-Impact)

1. Event-study (Q1): GDP growth $\hat{\beta}$ (lead/lag) ± 90/95 % CI.  
2. Partial residual scatter (Q2): growth vs FDI %GDP (pre vs post).  
3. Slopegraph (Q6): Δ Renewables vs Δ CO₂/GDP (2000 → latest).  
4. Small-multiples (Q3 & Q5): Unemployment and life expectancy.  
5. Volatility comparison (Q10): Boxplots of $\sigma$(GDP growth) pre/post.  
6. NB-GLM (Q7): Migration effect sizes with dispersion check.

---

## Statistical Toolbox Mapping

| Category | Methods |
|-----------|----------|
| **LSE / OLS** | DiD, FE within (Q1–Q6, Q10) |
| **MLE / GLM** | Poisson / NegBin for migration (Q7) |
| **Time-series** | ADF, KPSS, Engle-Granger (Q9), Bai-Perron/Chow (Q8) |
| **Variance tests** | F-test, Levene (Q10) |
| **Robustness** | Cluster SE by country; winsorize 1 % tails; exclude conflict years; leave-one-country-out |

---

## Data / Metadata Checks

- Flag modeled or uncertain years (ILO unemployment, life-expectancy post-conflict Ukraine).  
- Prefer PPP for GDP per capita; confirm conversion-factor notes.  
- Document interest-rate definitions and merge rules.

---

## How to Prioritize (5-Minute Video Flow)

**Main story:**  
Q1 (DiD on growth) → Q2 (FDI mechanism) → Q6 (sustainability delta) → Q5 (health implication).  

**Backup appendix:** Q3, Q4, Q7–Q10.

If pre-trends violate parallel-trend assumption, pivot to **within-country FE event-time** models and frame as “within-country acceleration,” not causal.

---

> For implementation: draft **code templates** (Python + `statsmodels`) for Q1 (DiD), Q2 (FE interaction), Q7 (NB-GLM), and plot recipes (event-study & slopegraph) in `notebooks/02_model_fe.ipynb`.
