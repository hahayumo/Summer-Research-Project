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

6.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.108098 | nan           |
| auc       | 0.999471 | nan           |
| f1        | 0.988764 |   0.624688    |
| accuracy  | 0.988506 |   0.624688    |
| precision | 1        |   0.941595    |
| recall    | 1        |   5.38547e-16 |
| mcc       | 0.977273 |   0.752373    |


## Confusion matrix (at threshold=0.624688)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        1 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_skew1                            |   1.22534   |
| return_skew2                            |   1.15096   |
| return_correlation_ts1_lag_0            |   0.917972  |
| return_autocorrelation_lag1_1           |   0.45948   |
| return_mean1                            |   0.456781  |
| return_correlation_ts2_lag_2            |   0.455092  |
| return_correlation_ts2_lag_1            |   0.410267  |
| return_sd2                              |   0.398952  |
| return_autocorrelation_lag1_2           |   0.353323  |
| return_correlation_ts1_lag_1            |   0.34041   |
| return_correlation_ts1_lag_2            |   0.283771  |
| return_sd1                              |  -0.0798713 |
| return_correlation_ts2_lag_3            |  -0.154505  |
| return_correlation_ts1_lag_3            |  -0.173821  |
| price1_granger_cause_price2             |  -0.369272  |
| price2_granger_cause_price1             |  -0.467355  |
| return_autocorrelation_lag1_rolling_sd1 |  -0.730169  |
| return_autocorrelation_lag1_rolling_sd2 |  -0.775437  |
| return_mean2                            |  -1.07089   |
| intercept                               |  -1.34915   |
| return_kurtosis1                        |  -3.38027   |
| return_kurtosis2                        |  -3.39806   |


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
