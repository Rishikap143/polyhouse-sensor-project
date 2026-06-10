# Exploratory Data Analysis Summary

## Dataset Overview

- Total observations: 50
- Date range: 2026-06-01 to 2026-06-05
- No missing values detected after cleaning.
- All sensor columns contain valid numeric values.

## Summary Statistics

| Variable | Mean |
|-----------|--------|
| Temperature (°C) | 29.92 |
| Humidity (%) | 62.72 |
| CO₂ (ppm) | 440.90 |
| Yield (kg) | 124.00 |

## Visualizations

The following figures were generated:

1. Correlation Heatmap
2. Humidity vs Yield Scatter Plot
3. CO₂ vs Yield Scatter Plot
4. Temperature vs Yield Scatter Plot

## Key Insights

### Humidity and Yield

Humidity values are concentrated between 57% and 69%. Yield appears relatively stable across this range, indicating only a moderate relationship between humidity and crop yield.

### CO₂ and Yield

Higher CO₂ levels generally correspond to slightly higher yield values. This suggests that increased CO₂ concentration may support plant growth inside the polyhouse environment.

### Temperature and Yield

Temperature remains within a narrow range (26.5°C–32.4°C). Yield does not show extreme variation, suggesting the crop was grown under relatively stable environmental conditions.

## Correlation Notes

- The strongest positive correlations should be identified from the heatmap.
- Correlation does not imply causation.
- The dataset contains only 50 observations, so conclusions should be interpreted carefully.