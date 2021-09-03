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

8.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.107306 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.735438    |
| accuracy  | 1        |   0.735438    |
| precision | 1        |   0.735438    |
| recall    | 1        |   2.89024e-47 |
| mcc       | 1        |   0.735438    |


## Confusion matrix (at threshold=0.735438)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  40 |                        0 |
| Labeled as simulated |                   0 |                       47 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew2                      |  0.53594    |
| return_skew1                      |  0.416073   |
| return_autocorrelation_2_lag1     |  0.380593   |
| sqreturn_correlation_ts1_lag_0    |  0.378146   |
| return_correlation_ts1_lag_0      |  0.378146   |
| return_correlation_ts1_lag_1      |  0.345871   |
| sqreturn_correlation_ts1_lag_1    |  0.345871   |
| return_autocorrelation_1_lag2     |  0.337068   |
| sqreturn_correlation_ts1_lag_2    |  0.199946   |
| return_correlation_ts1_lag_2      |  0.199946   |
| return_autocorrelation_2_lag3     |  0.187647   |
| return_autocorrelation_2_lag2     |  0.178074   |
| return_correlation_ts2_lag_1      |  0.166422   |
| sqreturn_correlation_ts2_lag_1    |  0.166422   |
| sqreturn_correlation_ts2_lag_3    |  0.145639   |
| return_correlation_ts2_lag_3      |  0.145639   |
| return_autocorrelation_1_lag3     |  0.06404    |
| return_autocorrelation_1_lag1     |  0.0410526  |
| sqreturn_correlation_ts1_lag_3    |  0.0234769  |
| return_correlation_ts1_lag_3      |  0.0234769  |
| return_sd1                        |  0.0200778  |
| sqreturn_correlation_ts2_lag_2    |  0.00749259 |
| return_correlation_ts2_lag_2      |  0.00749259 |
| return_mean1                      | -0.158955   |
| price2_granger_cause_price1       | -0.228245   |
| return_mean2                      | -0.3361     |
| return_sd2                        | -0.452681   |
| sqreturn_autocorrelation_ts2_lag3 | -0.474255   |
| sqreturn_autocorrelation_ts1_lag3 | -0.613192   |
| price1_granger_cause_price2       | -0.683925   |
| sqreturn_autocorrelation_ts1_lag1 | -0.791855   |
| sqreturn_autocorrelation_ts1_lag2 | -0.819341   |
| sqreturn_autocorrelation_ts2_lag2 | -0.819386   |
| sqreturn_autocorrelation_ts2_lag1 | -0.95216    |
| intercept                         | -1.75877    |
| return_kurtosis1                  | -3.77959    |
| return_kurtosis2                  | -4.08985    |


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
