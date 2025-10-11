# Visualization Guidelines

## Design Philosophy
Every figure should answer one question and stand on its own.

## Style Rules
- **Background:** white or light gray (#f9f9f9)
- **Font:** sans-serif, ≥ 18 pt
- **Color palette:** Okabe–Ito or Viridis (color-blind safe)
- **Axes:** labeled with units and readable ticks
- **Annotations:** direct labeling preferred over legends

## Chart Toolkit
| Purpose | Chart | Notes |
|----------|-------|-------|
| Coverage | Heatmap | non-null counts by year |
| Trend | Line/small multiples | by region/income |
| Relationship | Scatter + LOESS | LE vs GDPpc |
| Change | Slopegraph | ΔRenewables ↔ ΔPM2.5 |
| Residuals | Diverging bars | model errors |

## Accessibility
- Contrast ratio ≥ 3 : 1.
- Avoid red–green combinations.
- Provide alt-text in captions for video slides.

## Animation Tips
- ≤ 12 seconds, single highlight message.
- Sync to narration timing.