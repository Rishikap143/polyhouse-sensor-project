
# Random Forest Tuning Summary

## Parameter Grid

- n_estimators: [50, 100, 200]
- max_depth: [None, 8, 16]
- min_samples_leaf: [1, 3, 5]
## Parameter Grid Rationale

- n_estimators controls the number of trees in the forest. Higher values can improve stability but increase training time.

- max_depth controls how deep each tree can grow. Limiting depth helps reduce overfitting.

- min_samples_leaf controls the minimum samples required in a leaf node. Larger values create smoother predictions and reduce overfitting.

## Best Parameters

{'max_depth': 8, 'min_samples_leaf': 1, 'n_estimators': 100}

## Best CV MAE

-0.1047

## Test Metrics

- MAE: 0.0535
- RMSE: 0.0940
- R²: 0.5307

## Model Comparison

| Model | MAE | RMSE | R² |
|--------|--------|--------|--------|
| Linear Regression | 0.0704 | 0.0995 | 0.8015 |
| Random Forest Default | 0.0800 | 0.1100 | 0.4700 |
| Random Forest Tuned | 0.0535 | 0.0940 | 0.5307 |

## Champion Model

## Champion Model
The Tuned Random Forest model was selected as the champion model because it achieved the lowest MAE and RMSE on the untouched test set. Although Linear Regression achieved a higher R² score, the tuned Random Forest produced smaller prediction errors, making it the preferred model for yield prediction.
## Runtime

Training and tuning completed in 19.55 seconds.

## Limitations

- Predictions may be less reliable when sensor values fall outside the training range.
- Seasonal effects are not explicitly modeled.
- Additional environmental variables may improve prediction accuracy.
