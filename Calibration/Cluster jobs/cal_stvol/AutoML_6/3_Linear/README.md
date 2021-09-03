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

3.3 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.35733  | nan           |
| auc       | 0.947146 | nan           |
| f1        | 0.893617 |   0.459092    |
| accuracy  | 0.885057 |   0.459092    |
| precision | 1        |   0.813464    |
| recall    | 1        |   8.60608e-06 |
| mcc       | 0.783887 |   0.459092    |


## Confusion matrix (at threshold=0.459092)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  35 |                        9 |
| Labeled as simulated |                   1 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| mean2                             |   1.96909   |
| sqreturn_autocorrelation_ts2_lag3 |   1.7367    |
| mean1                             |   1.45145   |
| sqreturn_autocorrelation_ts1_lag3 |   1.32373   |
| return_autocorrelation_2_lag1     |   0.915313  |
| sqreturn_autocorrelation_ts2_lag2 |   0.850717  |
| sqreturn_autocorrelation_ts1_lag2 |   0.768614  |
| sqreturn_autocorrelation_ts2_lag1 |   0.728463  |
| return_autocorrelation_1_lag1     |   0.633688  |
| sqreturn_correlation_ts1_lag_1    |   0.621265  |
| return_correlation_ts1_lag_1      |   0.621265  |
| return_correlation_ts2_lag_1      |   0.549992  |
| sqreturn_correlation_ts2_lag_1    |   0.549992  |
| sqreturn_autocorrelation_ts1_lag1 |   0.537911  |
| return_autocorrelation_2_lag2     |   0.517966  |
| return_autocorrelation_2_lag3     |   0.43187   |
| return_correlation_ts2_lag_3      |   0.390707  |
| sqreturn_correlation_ts2_lag_3    |   0.390707  |
| sd1                               |   0.322128  |
| price1_granger_cause_price2       |   0.303199  |
| return_autocorrelation_1_lag3     |   0.21831   |
| return_autocorrelation_1_lag2     |   0.134174  |
| sqreturn_correlation_ts1_lag_3    |   0.0466577 |
| return_correlation_ts1_lag_3      |   0.0466577 |
| return_correlation_ts2_lag_2      |  -0.0760928 |
| sqreturn_correlation_ts2_lag_2    |  -0.0760928 |
| return_correlation_ts1_lag_0      |  -0.0886719 |
| sqreturn_correlation_ts1_lag_0    |  -0.0886719 |
| sd2                               |  -0.131883  |
| return_correlation_ts1_lag_2      |  -0.326395  |
| sqreturn_correlation_ts1_lag_2    |  -0.326395  |
| price2_granger_cause_price1       |  -0.858192  |
| skewness2                         |  -0.875452  |
| skewness1                         |  -0.932964  |
| intercept                         |  -1.97761   |
| kurtosis1                         |  -2.47052   |
| kurtosis2                         |  -2.72663   |


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
