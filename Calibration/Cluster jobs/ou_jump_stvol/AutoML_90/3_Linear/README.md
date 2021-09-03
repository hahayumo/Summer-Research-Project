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

13.5 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.184583 | nan           |
| auc       | 0.998943 | nan           |
| f1        | 0.988764 |   0.536808    |
| accuracy  | 0.988506 |   0.536808    |
| precision | 1        |   0.894359    |
| recall    | 1        |   4.73397e-16 |
| mcc       | 0.977261 |   0.536808    |


## Confusion matrix (at threshold=0.536808)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        1 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag2     |   0.688194  |
| return_autocorrelation_2_lag3     |   0.648572  |
| return_autocorrelation_2_lag1     |   0.63275   |
| sqreturn_correlation_ts1_lag_1    |   0.605008  |
| return_correlation_ts1_lag_1      |   0.605008  |
| return_mean2                      |   0.500109  |
| sqreturn_correlation_ts1_lag_3    |   0.485662  |
| return_correlation_ts1_lag_3      |   0.485662  |
| return_autocorrelation_1_lag1     |   0.456447  |
| sqreturn_correlation_ts2_lag_1    |   0.307188  |
| return_correlation_ts2_lag_1      |   0.307188  |
| return_correlation_ts1_lag_2      |   0.292902  |
| sqreturn_correlation_ts1_lag_2    |   0.292902  |
| sqreturn_correlation_ts2_lag_3    |   0.285213  |
| return_correlation_ts2_lag_3      |   0.285213  |
| sqreturn_correlation_ts2_lag_2    |   0.214492  |
| return_correlation_ts2_lag_2      |   0.214492  |
| return_autocorrelation_1_lag2     |   0.209007  |
| return_autocorrelation_1_lag3     |   0.0674006 |
| return_sd1                        |   0.048901  |
| price2_granger_cause_price1       |  -0.355995  |
| sqreturn_correlation_ts1_lag_0    |  -0.404838  |
| return_correlation_ts1_lag_0      |  -0.404838  |
| intercept                         |  -0.451863  |
| return_skew1                      |  -0.625263  |
| return_skew2                      |  -0.62892   |
| return_sd2                        |  -0.664046  |
| return_mean1                      |  -0.760914  |
| price1_granger_cause_price2       |  -0.775827  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.910868  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.990658  |
| sqreturn_autocorrelation_ts2_lag2 |  -1.2713    |
| sqreturn_autocorrelation_ts1_lag2 |  -1.36332   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.42252   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.61173   |
| return_kurtosis2                  |  -2.2697    |
| return_kurtosis1                  |  -3.25955   |


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
