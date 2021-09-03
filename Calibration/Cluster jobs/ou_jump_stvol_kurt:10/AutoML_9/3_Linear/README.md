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

4.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.126531 | nan           |
| auc       | 1        | nan           |
| f1        | 0.988764 |   0.693438    |
| accuracy  | 0.988506 |   0.693438    |
| precision | 1        |   0.916744    |
| recall    | 1        |   1.17829e-18 |
| mcc       | 0.977261 |   0.693438    |


## Confusion matrix (at threshold=0.693438)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        1 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew1                      |   1.35014   |
| return_skew2                      |   1.29801   |
| return_autocorrelation_1_lag2     |   0.516065  |
| return_autocorrelation_2_lag2     |   0.515683  |
| return_correlation_ts2_lag_2      |   0.502394  |
| sqreturn_correlation_ts2_lag_2    |   0.502394  |
| sqreturn_correlation_ts2_lag_1    |   0.451393  |
| return_correlation_ts2_lag_1      |   0.451393  |
| return_correlation_ts1_lag_2      |   0.390276  |
| sqreturn_correlation_ts1_lag_2    |   0.390276  |
| return_autocorrelation_2_lag1     |   0.376846  |
| return_autocorrelation_1_lag1     |   0.358589  |
| return_correlation_ts1_lag_1      |   0.341396  |
| sqreturn_correlation_ts1_lag_1    |   0.341396  |
| return_autocorrelation_1_lag3     |   0.185646  |
| return_sd2                        |   0.106206  |
| return_autocorrelation_2_lag3     |  -0.0203538 |
| sqreturn_correlation_ts1_lag_3    |  -0.147759  |
| return_correlation_ts1_lag_3      |  -0.147759  |
| sqreturn_correlation_ts2_lag_3    |  -0.207608  |
| return_correlation_ts2_lag_3      |  -0.207608  |
| return_sd1                        |  -0.284095  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.294872  |
| return_mean1                      |  -0.302255  |
| sqreturn_correlation_ts1_lag_0    |  -0.307328  |
| return_correlation_ts1_lag_0      |  -0.307328  |
| sqreturn_autocorrelation_ts2_lag2 |  -0.315563  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.353976  |
| price2_granger_cause_price1       |  -0.397015  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.456929  |
| price1_granger_cause_price2       |  -0.531746  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.794358  |
| return_mean2                      |  -0.891712  |
| sqreturn_autocorrelation_ts2_lag1 |  -0.905458  |
| intercept                         |  -1.07404   |
| return_kurtosis2                  |  -3.81937   |
| return_kurtosis1                  |  -3.84703   |


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
