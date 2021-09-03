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

21.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.159175 | nan           |
| auc       | 1        | nan           |
| f1        | 0.988764 |   0.758369    |
| accuracy  | 0.988506 |   0.758369    |
| precision | 1        |   0.868111    |
| recall    | 1        |   3.19713e-13 |
| mcc       | 0.977261 |   0.758369    |


## Confusion matrix (at threshold=0.758369)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        1 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.725686  |
| return_autocorrelation_2_lag3     |   0.367796  |
| return_autocorrelation_2_lag1     |   0.363283  |
| sqreturn_correlation_ts2_lag_3    |   0.317368  |
| return_correlation_ts2_lag_3      |   0.317368  |
| sd1                               |   0.273146  |
| return_autocorrelation_1_lag3     |   0.256481  |
| sqreturn_correlation_ts2_lag_1    |   0.235353  |
| return_correlation_ts2_lag_1      |   0.235353  |
| return_autocorrelation_1_lag2     |   0.212259  |
| sqreturn_correlation_ts1_lag_2    |   0.1929    |
| return_correlation_ts1_lag_2      |   0.1929    |
| return_correlation_ts1_lag_3      |   0.184803  |
| sqreturn_correlation_ts1_lag_3    |   0.184803  |
| return_correlation_ts1_lag_1      |   0.153398  |
| sqreturn_correlation_ts1_lag_1    |   0.153398  |
| mean2                             |   0.142644  |
| skewness1                         |   0.137083  |
| return_autocorrelation_2_lag2     |   0.127092  |
| return_autocorrelation_1_lag1     |   0.0307106 |
| return_correlation_ts2_lag_2      |  -0.0912305 |
| sqreturn_correlation_ts2_lag_2    |  -0.0912305 |
| return_correlation_ts1_lag_0      |  -0.138527  |
| sqreturn_correlation_ts1_lag_0    |  -0.138527  |
| mean1                             |  -0.182978  |
| sd2                               |  -0.488873  |
| price1_granger_cause_price2       |  -0.526634  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.694174  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.750176  |
| price2_granger_cause_price1       |  -0.828972  |
| sqreturn_autocorrelation_ts1_lag1 |  -1.00242   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.0331    |
| sqreturn_autocorrelation_ts2_lag2 |  -1.0404    |
| intercept                         |  -1.17326   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.18166   |
| kurtosis2                         |  -3.48323   |
| kurtosis1                         |  -4.53179   |


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
