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

2.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0841791 | nan           |
| auc       | 0.997884  | nan           |
| f1        | 0.989011  |   0.475665    |
| accuracy  | 0.988506  |   0.475665    |
| precision | 1         |   0.891612    |
| recall    | 1         |   5.84238e-06 |
| mcc       | 0.977225  |   0.475665    |


## Confusion matrix (at threshold=0.475665)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        1 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_autocorrelation_lag1_rolling_sd2 |  2.93659    |
| return_autocorrelation_lag1_rolling_sd1 |  2.31068    |
| return_sd1                              |  0.908752   |
| return_autocorrelation_lag1_1           |  0.270657   |
| return_sd2                              |  0.160609   |
| return_autocorrelation_lag1_2           |  0.145445   |
| return_correlation_ts2_lag_1            |  0.138159   |
| return_kurtosis2                        |  0.117729   |
| return_skew1                            |  0.116651   |
| return_correlation_ts1_lag_1            |  0.111933   |
| return_correlation_ts2_lag_2            |  0.0620887  |
| return_skew2                            |  0.0286651  |
| return_correlation_ts1_lag_2            | -0.00507429 |
| price1_granger_cause_price2             | -0.0365938  |
| return_correlation_ts1_lag_3            | -0.0807856  |
| return_correlation_ts1_lag_0            | -0.0960598  |
| return_kurtosis1                        | -0.219233   |
| intercept                               | -0.236509   |
| return_correlation_ts2_lag_3            | -0.265529   |
| price2_granger_cause_price1             | -0.313686   |
| return_mean1                            | -0.441559   |
| return_mean2                            | -1.06123    |


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
