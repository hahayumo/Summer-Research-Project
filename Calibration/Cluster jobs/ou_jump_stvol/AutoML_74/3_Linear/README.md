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

14.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.215112 | nan           |
| auc       | 0.997357 | nan           |
| f1        | 0.976744 |   0.734206    |
| accuracy  | 0.977011 |   0.734206    |
| precision | 1        |   0.734206    |
| recall    | 1        |   1.32921e-08 |
| mcc       | 0.95505  |   0.734206    |


## Confusion matrix (at threshold=0.734206)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   2 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag1     |   0.77153   |
| return_autocorrelation_2_lag2     |   0.694313  |
| return_autocorrelation_2_lag3     |   0.452835  |
| return_correlation_ts1_lag_1      |   0.344865  |
| sqreturn_correlation_ts1_lag_1    |   0.344865  |
| return_autocorrelation_1_lag3     |   0.335992  |
| sqreturn_correlation_ts2_lag_1    |   0.318397  |
| return_correlation_ts2_lag_1      |   0.318397  |
| sqreturn_correlation_ts1_lag_2    |   0.280237  |
| return_correlation_ts1_lag_2      |   0.280237  |
| return_autocorrelation_1_lag2     |   0.261446  |
| sqreturn_correlation_ts2_lag_3    |   0.0958747 |
| return_correlation_ts2_lag_3      |   0.0958747 |
| return_correlation_ts2_lag_2      |   0.0922219 |
| sqreturn_correlation_ts2_lag_2    |   0.0922219 |
| return_correlation_ts1_lag_3      |   0.0911542 |
| sqreturn_correlation_ts1_lag_3    |   0.0911542 |
| return_autocorrelation_1_lag1     |   0.0366855 |
| return_mean2                      |   0.0170144 |
| return_sd1                        |  -0.192236  |
| return_correlation_ts1_lag_0      |  -0.24495   |
| sqreturn_correlation_ts1_lag_0    |  -0.24495   |
| return_skew2                      |  -0.293285  |
| return_sd2                        |  -0.428341  |
| return_skew1                      |  -0.456019  |
| price2_granger_cause_price1       |  -0.551432  |
| price1_granger_cause_price2       |  -0.718727  |
| intercept                         |  -0.775684  |
| return_mean1                      |  -0.779814  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.782835  |
| sqreturn_autocorrelation_ts1_lag3 |  -1.06122   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.11917   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.18771   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.53242   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.55176   |
| return_kurtosis2                  |  -3.08379   |
| return_kurtosis1                  |  -3.70594   |


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
