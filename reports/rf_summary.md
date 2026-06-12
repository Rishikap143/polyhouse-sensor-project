# Task 6: Random Forest & Time-Series Cross Validation

## Random Forest Test Results

* Train MAE: 0.028 kg
* Test MAE: 0.053 kg
* Test R²: 0.532

## TimeSeriesSplit Cross Validation

### Random Forest

* Fold MAE Scores:

  * 0.158
  * 0.021
  * 0.129
  * 0.123
  * 0.093

* Mean CV MAE: 0.105

* Std CV MAE: 0.047

### Linear Regression

* Fold MAE Scores:

  * 0.137
  * 0.126
  * 0.109
  * 0.122
  * 0.092

* Mean CV MAE: 0.117

* Std CV MAE: 0.016

## Feature Importance Interpretation

The Random Forest model was trained using temperature, humidity, and CO₂ features. The feature importance chart indicates which environmental factors contribute most strongly to yield prediction. Features with higher importance values have a greater influence on the model's decisions.

## Overfitting Analysis

Train MAE (0.028 kg) is close to Test MAE (0.053 kg), indicating that the model generalizes well and does not exhibit significant overfitting.

## Model Comparison

Random Forest achieved a lower average CV MAE (0.105) than Linear Regression (0.117), suggesting slightly better predictive performance. However, Random Forest also showed higher variance across folds, indicating less stable performance over time.

## Conclusion

Random Forest provides a modest improvement in prediction accuracy compared with Linear Regression. The additional complexity is justified when predictive performance is the primary objective, while Linear Regression remains more interpretable.
