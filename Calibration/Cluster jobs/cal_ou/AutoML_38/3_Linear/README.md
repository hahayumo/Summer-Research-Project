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

5.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0307712 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.185674    |
| accuracy  | 1         |   0.185674    |
| precision | 1         |   0.498605    |
| recall    | 1         |   6.40736e-10 |
| mcc       | 1         |   0.185674    |


## Confusion matrix (at threshold=0.185674)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag1     |   1.01291   |
| sqreturn_autocorrelation_ts2_lag3 |   0.934995  |
| return_autocorrelation_2_lag3     |   0.934664  |
| return_autocorrelation_2_lag2     |   0.875125  |
| sqreturn_autocorrelation_ts2_lag2 |   0.84738   |
| sqreturn_autocorrelation_ts2_lag1 |   0.829207  |
| return_correlation_ts1_lag_1      |   0.376067  |
| sqreturn_correlation_ts1_lag_1    |   0.376067  |
| sqreturn_correlation_ts2_lag_1    |   0.330495  |
| return_correlation_ts2_lag_1      |   0.330495  |
| sqreturn_correlation_ts2_lag_3    |   0.317596  |
| return_correlation_ts2_lag_3      |   0.317596  |
| return_correlation_ts1_lag_3      |   0.26151   |
| sqreturn_correlation_ts1_lag_3    |   0.26151   |
| return_correlation_ts1_lag_2      |   0.245803  |
| sqreturn_correlation_ts1_lag_2    |   0.245803  |
| return_autocorrelation_1_lag1     |   0.224401  |
| return_correlation_ts2_lag_2      |   0.22348   |
| sqreturn_correlation_ts2_lag_2    |   0.22348   |
| skewness1                         |   0.192339  |
| return_autocorrelation_1_lag3     |   0.183649  |
| return_autocorrelation_1_lag2     |   0.128676  |
| return_correlation_ts1_lag_0      |  -0.0386415 |
| sqreturn_correlation_ts1_lag_0    |  -0.0386415 |
| sqreturn_autocorrelation_ts1_lag3 |  -0.152619  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.195467  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.205579  |
| price2_granger_cause_price1       |  -0.306209  |
| sd2                               |  -0.57762   |
| price1_granger_cause_price2       |  -0.610339  |
| sd1                               |  -0.636726  |
| mean2                             |  -0.916498  |
| skewness2                         |  -0.921502  |
| kurtosis2                         |  -1.04333   |
| kurtosis1                         |  -1.55249   |
| mean1                             |  -1.64081   |
| intercept                         |  -2.91288   |


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
