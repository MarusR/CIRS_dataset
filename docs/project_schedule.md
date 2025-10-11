# Project Schedule and Roles

## Timeline (Oct 11 – 31 2025)

| Week       | Focus                               | Deliverables                                      |
|------------|-------------------------------------|--------------------------------------------------|
| Oct 13–19  | Data triage & EDA                  | Coverage heatmaps, missingness summary           |
| Oct 20–26  | Modeling & Visualization             | FE model results, first draft slides             |
| Oct 27–31  | Finalization                        | Robustness checks, video, submission             |

## Roles

| Role               | Responsibilities                                      |
|--------------------|------------------------------------------------------|
| Lead Analyst        | Modeling, diagnostics, statistical validation        |
| Visualization Lead  | Chart design, animation, slide layout                |
| Ethics / QA Lead    | Compliance, uncertainty reporting                     |
| Producer / PM      | Timeline, coordination, video editing                |

## Daily Checklist

- Update notebook and data logs  
- Review one figure for clarity  
- Commit reproducible outputs  
- Keep slides within 4 content limit  

## Risk Register

| Risk                                         | Mitigation                                           |
|----------------------------------------------|-----------------------------------------------------|
| Sparse data                                  | Use 10-year medians; drop high-missing indicators   |
| Confounding                                  | Year FE and within-country differencing             |
| Outliers                                     | Winsorize 1 % tails                                 |
| Slide bloat                                  | Enforce ≤ 4 content slides                          |
| Audio issues                                 | Script timing + backup mic                           |
| Attribution errors                           | Template citation in final slide                    |