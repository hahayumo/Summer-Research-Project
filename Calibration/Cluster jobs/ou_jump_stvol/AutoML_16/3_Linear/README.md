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

17.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.104734 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.471146    |
| accuracy  | 1        |   0.471146    |
| precision | 1        |   0.891376    |
| recall    | 1        |   2.68294e-10 |
| mcc       | 1        |   0.471146    |


## Confusion matrix (at threshold=0.471146)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        0 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew1                      |   0.689276  |
| return_skew2                      |   0.676112  |
| return_autocorrelation_2_lag2     |   0.472367  |
| return_autocorrelation_1_lag3     |   0.362826  |
| return_autocorrelation_2_lag1     |   0.348069  |
| return_autocorrelation_1_lag2     |   0.305845  |
| sqreturn_correlation_ts1_lag_2    |   0.300658  |
| return_correlation_ts1_lag_2      |   0.300658  |
| return_autocorrelation_2_lag3     |   0.273152  |
| return_correlation_ts1_lag_1      |   0.238886  |
| sqreturn_correlation_ts1_lag_1    |   0.238886  |
| sqreturn_correlation_ts1_lag_3    |   0.216896  |
| return_correlation_ts1_lag_3      |   0.216896  |
| return_correlation_ts2_lag_1      |   0.207802  |
| sqreturn_correlation_ts2_lag_1    |   0.207802  |
| sqreturn_correlation_ts2_lag_3    |   0.197161  |
| return_correlation_ts2_lag_3      |   0.197161  |
| return_sd1                        |   0.147638  |
| sqreturn_correlation_ts1_lag_0    |   0.087266  |
| return_correlation_ts1_lag_0      |   0.087266  |
| return_autocorrelation_1_lag1     |   0.0243341 |
| return_correlation_ts2_lag_2      |  -0.0103255 |
| sqreturn_correlation_ts2_lag_2    |  -0.0103255 |
| return_mean1                      |  -0.234593  |
| return_mean2                      |  -0.350782  |
| return_sd2                        |  -0.364333  |
| price2_granger_cause_price1       |  -0.422033  |
| price1_granger_cause_price2       |  -0.444979  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.825162  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.859875  |
| sqreturn_autocorrelation_ts1_lag3 |  -1.1443    |
| intercept                         |  -1.20722   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.20894   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.26751   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.29597   |
| return_kurtosis2                  |  -3.24698   |
| return_kurtosis1                  |  -4.30151   |


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
