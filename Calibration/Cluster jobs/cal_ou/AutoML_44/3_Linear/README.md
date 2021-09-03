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

2.9 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0308662 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.399663    |
| accuracy  | 1         |   0.399663    |
| precision | 1         |   0.399663    |
| recall    | 1         |   0.000141756 |
| mcc       | 1         |   0.399663    |


## Confusion matrix (at threshold=0.399663)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        0 |
| Labeled as simulated |                   0 |                       46 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_autocorrelation_ts2_lag3 |   1.07451   |
| return_autocorrelation_2_lag1     |   1.03529   |
| return_autocorrelation_2_lag2     |   1.01514   |
| return_autocorrelation_2_lag3     |   0.979445  |
| sqreturn_autocorrelation_ts2_lag2 |   0.969804  |
| sqreturn_autocorrelation_ts2_lag1 |   0.861496  |
| sqreturn_correlation_ts1_lag_1    |   0.350769  |
| return_correlation_ts1_lag_1      |   0.350769  |
| sqreturn_correlation_ts1_lag_3    |   0.32475   |
| return_correlation_ts1_lag_3      |   0.32475   |
| sqreturn_correlation_ts1_lag_2    |   0.294786  |
| return_correlation_ts1_lag_2      |   0.294786  |
| return_correlation_ts2_lag_1      |   0.293638  |
| sqreturn_correlation_ts2_lag_1    |   0.293638  |
| return_correlation_ts2_lag_2      |   0.27199   |
| sqreturn_correlation_ts2_lag_2    |   0.27199   |
| sqreturn_correlation_ts2_lag_3    |   0.247093  |
| return_correlation_ts2_lag_3      |   0.247093  |
| return_autocorrelation_1_lag1     |   0.22181   |
| return_autocorrelation_1_lag2     |   0.220339  |
| return_autocorrelation_1_lag3     |   0.170315  |
| skewness1                         |   0.16444   |
| sqreturn_correlation_ts1_lag_0    |   0.0486329 |
| return_correlation_ts1_lag_0      |   0.0486329 |
| sqreturn_autocorrelation_ts1_lag2 |  -0.103001  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.139624  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.160607  |
| price2_granger_cause_price1       |  -0.306693  |
| sd2                               |  -0.563288  |
| sd1                               |  -0.618674  |
| price1_granger_cause_price2       |  -0.712981  |
| skewness2                         |  -0.906165  |
| mean2                             |  -0.968756  |
| kurtosis2                         |  -0.97626   |
| kurtosis1                         |  -1.16826   |
| mean1                             |  -1.57801   |
| intercept                         |  -2.86139   |


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
