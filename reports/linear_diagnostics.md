# Linear Regression Diagnostics

## Test Metrics

- MAE: 0.07 kg
- RMSE: 0.10 kg
- R²: 0.802

## Coefficient Interpretation

### Temperature (8.386)
Temperature has the strongest positive influence on mushroom yield. Higher temperature generally leads to higher predicted yield.

### Humidity (4.813)
Humidity positively affects mushroom growth and yield.

### CO₂ (0.287)
CO₂ has a positive but smaller effect on yield compared with temperature and humidity.

## Residual Diagnostics

Residuals were calculated as:

Residual = Actual Yield - Predicted Yield

Diagnostic figure:
- reports/figures/residuals_linear.png

The residuals are generally centered around zero, indicating reasonable model performance.

## Baseline Evaluation

The model achieved an R² score of 0.802.

This means approximately 80.2% of the variation in mushroom yield is explained by the model, making it a strong baseline.

## Recommendation

Keep linear regression as the baseline model.

Future improvements:
- Additional engineered features
- More interaction terms
- Random Forest Regressor
- Gradient Boosting Regressor