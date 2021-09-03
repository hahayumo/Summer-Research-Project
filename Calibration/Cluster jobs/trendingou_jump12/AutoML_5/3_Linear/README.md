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

4.6 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0309534 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.530253    |
| accuracy  | 1         |   0.530253    |
| precision | 1         |   0.530253    |
| recall    | 1         |   3.78414e-07 |
| mcc       | 1         |   0.530253    |


## Confusion matrix (at threshold=0.530253)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_autocorrelation_lag1_1           |    2.99521  |
| return_correlation_ts1_lag_0            |    1.2695   |
| return_correlation_ts1_lag_1            |    0.877181 |
| return_correlation_ts2_lag_2            |    0.868612 |
| return_correlation_ts2_lag_1            |    0.85631  |
| return_correlation_ts2_lag_3            |    0.839534 |
| return_correlation_ts1_lag_2            |    0.779348 |
| return_correlation_ts1_lag_3            |    0.761721 |
| return_sd2                              |    0.323235 |
| return_autocorrelation_lag1_2           |    0.282858 |
| return_skew2                            |    0.266404 |
| return_skew1                            |   -0.129737 |
| return_autocorrelation_lag1_rolling_sd2 |   -0.491611 |
| return_kurtosis2                        |   -0.528626 |
| return_sd1                              |   -0.579434 |
| price1_granger_cause_price2             |   -0.586015 |
| return_autocorrelation_lag1_rolling_sd1 |   -0.670401 |
| return_mean1                            |   -0.677629 |
| return_mean2                            |   -0.927907 |
| price2_granger_cause_price1             |   -0.940467 |
| return_kurtosis1                        |   -1.68222  |
| intercept                               |   -2.71498  |


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
