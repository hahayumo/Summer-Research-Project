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

6.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.120926 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.747581    |
| accuracy  | 1        |   0.747581    |
| precision | 1        |   0.889266    |
| recall    | 1        |   1.84662e-14 |
| mcc       | 1        |   0.747581    |


## Confusion matrix (at threshold=0.747581)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  46 |                        0 |
| Labeled as simulated |                   0 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.64776   |
| sd1                               |   0.63007   |
| return_autocorrelation_2_lag1     |   0.452793  |
| return_autocorrelation_1_lag2     |   0.308154  |
| mean2                             |   0.268154  |
| return_autocorrelation_1_lag1     |   0.264467  |
| sqreturn_correlation_ts1_lag_2    |   0.259285  |
| return_correlation_ts1_lag_2      |   0.259285  |
| sqreturn_correlation_ts1_lag_3    |   0.259234  |
| return_correlation_ts1_lag_3      |   0.259234  |
| sqreturn_correlation_ts2_lag_1    |   0.257043  |
| return_correlation_ts2_lag_1      |   0.257043  |
| return_correlation_ts2_lag_3      |   0.247827  |
| sqreturn_correlation_ts2_lag_3    |   0.247827  |
| return_autocorrelation_2_lag3     |   0.243956  |
| return_correlation_ts1_lag_1      |   0.243362  |
| sqreturn_correlation_ts1_lag_1    |   0.243362  |
| return_autocorrelation_1_lag3     |   0.208094  |
| sqreturn_correlation_ts1_lag_0    |   0.106245  |
| return_correlation_ts1_lag_0      |   0.106245  |
| return_autocorrelation_2_lag2     |   0.0970904 |
| sqreturn_correlation_ts2_lag_2    |   0.0929225 |
| return_correlation_ts2_lag_2      |   0.0929225 |
| mean1                             |  -0.0569294 |
| skewness1                         |  -0.0787714 |
| price1_granger_cause_price2       |  -0.178312  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.574868  |
| sd2                               |  -0.596429  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.730325  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.73519   |
| price2_granger_cause_price1       |  -0.755243  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.769218  |
| sqreturn_autocorrelation_ts2_lag2 |  -0.889444  |
| sqreturn_autocorrelation_ts2_lag1 |  -0.905872  |
| intercept                         |  -1.95195   |
| kurtosis2                         |  -3.63107   |
| kurtosis1                         |  -3.73952   |


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
