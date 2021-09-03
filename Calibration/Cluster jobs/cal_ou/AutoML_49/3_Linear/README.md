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

4.1 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0200373 | nan          |
| auc       | 1         | nan          |
| f1        | 1         |   0.483091   |
| accuracy  | 1         |   0.483091   |
| precision | 1         |   0.977218   |
| recall    | 1         |   3.2713e-05 |
| mcc       | 1         |   0.483091   |


## Confusion matrix (at threshold=0.483091)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag1     |   1.17086   |
| sqreturn_autocorrelation_ts2_lag3 |   1.16011   |
| sqreturn_autocorrelation_ts2_lag2 |   1.12453   |
| return_autocorrelation_2_lag3     |   1.12247   |
| return_autocorrelation_2_lag2     |   1.09868   |
| sqreturn_autocorrelation_ts2_lag1 |   1.00183   |
| return_correlation_ts1_lag_1      |   0.308859  |
| sqreturn_correlation_ts1_lag_1    |   0.308859  |
| sqreturn_correlation_ts2_lag_3    |   0.259656  |
| return_correlation_ts2_lag_3      |   0.259656  |
| return_correlation_ts1_lag_3      |   0.236035  |
| sqreturn_correlation_ts1_lag_3    |   0.236035  |
| return_autocorrelation_1_lag1     |   0.228357  |
| sqreturn_correlation_ts2_lag_1    |   0.227234  |
| return_correlation_ts2_lag_1      |   0.227234  |
| return_correlation_ts1_lag_2      |   0.21382   |
| sqreturn_correlation_ts1_lag_2    |   0.21382   |
| return_autocorrelation_1_lag3     |   0.204939  |
| skewness1                         |   0.158527  |
| sqreturn_correlation_ts2_lag_2    |   0.0766265 |
| return_correlation_ts2_lag_2      |   0.0766265 |
| return_autocorrelation_1_lag2     |   0.0762514 |
| return_correlation_ts1_lag_0      |  -0.066141  |
| sqreturn_correlation_ts1_lag_0    |  -0.066141  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.237303  |
| price2_granger_cause_price1       |  -0.257989  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.286945  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.320263  |
| skewness2                         |  -0.487415  |
| price1_granger_cause_price2       |  -0.5138    |
| sd2                               |  -0.53916   |
| sd1                               |  -0.651631  |
| mean2                             |  -0.828431  |
| kurtosis2                         |  -0.844316  |
| kurtosis1                         |  -1.39044   |
| mean1                             |  -1.82171   |
| intercept                         |  -3.17415   |


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
