# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
accuracy

## Training time

11.8 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.185218 | nan          |
| auc       | 0.989362 | nan          |
| f1        | 0.958333 |   0.529012   |
| accuracy  | 0.954023 |   0.529012   |
| precision | 1        |   0.80333    |
| recall    | 1        |   3.6953e-22 |
| mcc       | 0.908081 |   0.529012   |


## Confusion matrix (at threshold=0.529012)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  37 |                        3 |
| Labeled as simulated |                   1 |                       46 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag1     |   0.674461  |
| return_autocorrelation_2_lag2     |   0.534746  |
| return_autocorrelation_2_lag3     |   0.522526  |
| return_correlation_ts1_lag_1      |   0.470187  |
| sqreturn_correlation_ts1_lag_1    |   0.470187  |
| sqreturn_correlation_ts1_lag_2    |   0.426184  |
| return_correlation_ts1_lag_2      |   0.426184  |
| sqreturn_correlation_ts2_lag_1    |   0.397476  |
| return_correlation_ts2_lag_1      |   0.397476  |
| return_autocorrelation_1_lag2     |   0.314174  |
| return_autocorrelation_1_lag1     |   0.231229  |
| return_correlation_ts1_lag_3      |   0.192216  |
| sqreturn_correlation_ts1_lag_3    |   0.192216  |
| sqreturn_correlation_ts2_lag_3    |   0.143031  |
| return_correlation_ts2_lag_3      |   0.143031  |
| sqreturn_correlation_ts2_lag_2    |   0.124845  |
| return_correlation_ts2_lag_2      |   0.124845  |
| return_autocorrelation_1_lag3     |   0.0976494 |
| return_correlation_ts1_lag_0      |   0.0597638 |
| sqreturn_correlation_ts1_lag_0    |   0.0597638 |
| return_mean2                      |   0.0488405 |
| return_skew1                      |  -0.107888  |
| return_sd1                        |  -0.216196  |
| return_sd2                        |  -0.302416  |
| price2_granger_cause_price1       |  -0.498296  |
| return_skew2                      |  -0.559824  |
| intercept                         |  -0.63189   |
| price1_granger_cause_price2       |  -0.672643  |
| return_mean1                      |  -0.744416  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.747206  |
| sqreturn_autocorrelation_ts1_lag3 |  -1.18263   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.21721   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.2367    |
| sqreturn_autocorrelation_ts1_lag1 |  -1.45588   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.73113   |
| return_kurtosis2                  |  -2.14218   |
| return_kurtosis1                  |  -3.33796   |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
