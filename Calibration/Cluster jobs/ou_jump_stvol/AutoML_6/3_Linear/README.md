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

4.8 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.120892 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.766896    |
| accuracy  | 1        |   0.766896    |
| precision | 1        |   0.766896    |
| recall    | 1        |   9.20024e-11 |
| mcc       | 1        |   0.766896    |


## Confusion matrix (at threshold=0.766896)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        0 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew2                      |   1.06383   |
| return_autocorrelation_2_lag1     |   0.445144  |
| return_correlation_ts1_lag_1      |   0.439196  |
| sqreturn_correlation_ts1_lag_1    |   0.439196  |
| return_autocorrelation_1_lag2     |   0.310858  |
| return_autocorrelation_1_lag3     |   0.293802  |
| sqreturn_correlation_ts1_lag_0    |   0.270275  |
| return_correlation_ts1_lag_0      |   0.270275  |
| return_autocorrelation_1_lag1     |   0.247007  |
| return_autocorrelation_2_lag2     |   0.240066  |
| return_correlation_ts2_lag_1      |   0.217917  |
| sqreturn_correlation_ts2_lag_1    |   0.217917  |
| return_skew1                      |   0.211036  |
| sqreturn_correlation_ts1_lag_2    |   0.174015  |
| return_correlation_ts1_lag_2      |   0.174015  |
| return_autocorrelation_2_lag3     |   0.17001   |
| sqreturn_correlation_ts2_lag_3    |   0.165642  |
| return_correlation_ts2_lag_3      |   0.165642  |
| sqreturn_correlation_ts1_lag_3    |   0.11353   |
| return_correlation_ts1_lag_3      |   0.11353   |
| return_correlation_ts2_lag_2      |   0.0248586 |
| sqreturn_correlation_ts2_lag_2    |   0.0248586 |
| return_sd1                        |  -0.122474  |
| price2_granger_cause_price1       |  -0.150009  |
| return_mean2                      |  -0.266705  |
| price1_granger_cause_price2       |  -0.293621  |
| return_sd2                        |  -0.425948  |
| return_mean1                      |  -0.491192  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.834031  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.879061  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.896667  |
| sqreturn_autocorrelation_ts1_lag1 |  -1.11466   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.14836   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.23901   |
| intercept                         |  -1.61145   |
| return_kurtosis1                  |  -3.73263   |
| return_kurtosis2                  |  -3.8364    |


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
