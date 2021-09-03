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

3.7 seconds

## Metric details
|           |   score |     threshold |
|:----------|--------:|--------------:|
| logloss   | 0.02681 | nan           |
| auc       | 1       | nan           |
| f1        | 1       |   0.495845    |
| accuracy  | 1       |   0.495845    |
| precision | 1       |   0.495845    |
| recall    | 1       |   3.47851e-05 |
| mcc       | 1       |   0.495845    |


## Confusion matrix (at threshold=0.495845)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  46 |                        0 |
| Labeled as simulated |                   0 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_autocorrelation_lag1_1           |    2.91104  |
| return_correlation_ts1_lag_0            |    1.18486  |
| return_correlation_ts1_lag_1            |    0.900712 |
| return_correlation_ts2_lag_2            |    0.895587 |
| return_correlation_ts1_lag_2            |    0.857998 |
| return_correlation_ts2_lag_1            |    0.850944 |
| return_correlation_ts2_lag_3            |    0.795362 |
| return_correlation_ts1_lag_3            |    0.75652  |
| return_skew2                            |    0.496645 |
| return_autocorrelation_lag1_2           |    0.276864 |
| return_sd2                              |    0.27084  |
| return_skew1                            |   -0.283333 |
| return_autocorrelation_lag1_rolling_sd2 |   -0.407597 |
| price1_granger_cause_price2             |   -0.428603 |
| return_mean1                            |   -0.4662   |
| return_kurtosis2                        |   -0.537696 |
| return_sd1                              |   -0.629255 |
| return_autocorrelation_lag1_rolling_sd1 |   -0.701633 |
| price2_granger_cause_price1             |   -0.969891 |
| return_mean2                            |   -1.00631  |
| return_kurtosis1                        |   -1.73378  |
| intercept                               |   -2.98446  |


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
