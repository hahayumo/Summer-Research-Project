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

6.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.134579 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.727147    |
| accuracy  | 1        |   0.727147    |
| precision | 1        |   0.727147    |
| recall    | 1        |   2.56827e-16 |
| mcc       | 1        |   0.727147    |


## Confusion matrix (at threshold=0.727147)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew1                      |  1.59251    |
| return_skew2                      |  1.00954    |
| return_autocorrelation_1_lag2     |  0.699713   |
| return_autocorrelation_1_lag1     |  0.463843   |
| sqreturn_correlation_ts1_lag_2    |  0.397192   |
| return_correlation_ts1_lag_2      |  0.397192   |
| sqreturn_correlation_ts1_lag_1    |  0.340658   |
| return_correlation_ts1_lag_1      |  0.340658   |
| sqreturn_correlation_ts2_lag_1    |  0.31702    |
| return_correlation_ts2_lag_1      |  0.31702    |
| sqreturn_correlation_ts2_lag_2    |  0.292526   |
| return_correlation_ts2_lag_2      |  0.292526   |
| return_autocorrelation_2_lag2     |  0.269085   |
| return_autocorrelation_2_lag1     |  0.229294   |
| return_correlation_ts2_lag_3      |  0.13083    |
| sqreturn_correlation_ts2_lag_3    |  0.13083    |
| sqreturn_correlation_ts1_lag_3    |  0.0630687  |
| return_correlation_ts1_lag_3      |  0.0630687  |
| return_autocorrelation_1_lag3     |  0.0342687  |
| return_autocorrelation_2_lag3     |  0.00732586 |
| return_sd2                        | -0.0310006  |
| return_correlation_ts1_lag_0      | -0.0514076  |
| sqreturn_correlation_ts1_lag_0    | -0.0514076  |
| return_mean1                      | -0.21674    |
| price1_granger_cause_price2       | -0.297233   |
| price2_granger_cause_price1       | -0.303277   |
| sqreturn_autocorrelation_ts1_lag3 | -0.409487   |
| sqreturn_autocorrelation_ts2_lag3 | -0.455642   |
| return_sd1                        | -0.471695   |
| sqreturn_autocorrelation_ts1_lag2 | -0.649432   |
| sqreturn_autocorrelation_ts2_lag2 | -0.71653    |
| sqreturn_autocorrelation_ts2_lag1 | -0.812686   |
| return_mean2                      | -1.02043    |
| sqreturn_autocorrelation_ts1_lag1 | -1.10786    |
| intercept                         | -1.48391    |
| return_kurtosis2                  | -3.45059    |
| return_kurtosis1                  | -4.14926    |


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
