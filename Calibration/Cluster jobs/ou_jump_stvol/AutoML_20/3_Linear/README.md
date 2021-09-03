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

20.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.116834 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.54675     |
| accuracy  | 1        |   0.54675     |
| precision | 1        |   0.878112    |
| recall    | 1        |   8.85895e-15 |
| mcc       | 1        |   0.54675     |


## Confusion matrix (at threshold=0.54675)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew2                      |   0.64406   |
| return_autocorrelation_2_lag1     |   0.506292  |
| return_autocorrelation_2_lag3     |   0.47714   |
| return_autocorrelation_2_lag2     |   0.31594   |
| return_correlation_ts1_lag_1      |   0.297196  |
| sqreturn_correlation_ts1_lag_1    |   0.297196  |
| return_correlation_ts1_lag_0      |   0.27393   |
| sqreturn_correlation_ts1_lag_0    |   0.27393   |
| return_autocorrelation_1_lag1     |   0.222462  |
| return_skew1                      |   0.202748  |
| return_autocorrelation_1_lag2     |   0.186493  |
| sqreturn_correlation_ts2_lag_1    |   0.170378  |
| return_correlation_ts2_lag_1      |   0.170378  |
| return_correlation_ts1_lag_2      |   0.164314  |
| sqreturn_correlation_ts1_lag_2    |   0.164314  |
| sqreturn_correlation_ts2_lag_3    |   0.159853  |
| return_correlation_ts2_lag_3      |   0.159853  |
| return_sd1                        |   0.133884  |
| sqreturn_correlation_ts1_lag_3    |   0.125784  |
| return_correlation_ts1_lag_3      |   0.125784  |
| return_autocorrelation_1_lag3     |   0.109613  |
| sqreturn_correlation_ts2_lag_2    |   0.0643445 |
| return_correlation_ts2_lag_2      |   0.0643445 |
| price2_granger_cause_price1       |  -0.0300479 |
| price1_granger_cause_price2       |  -0.358282  |
| return_mean2                      |  -0.382067  |
| return_mean1                      |  -0.574996  |
| return_sd2                        |  -0.588279  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.873894  |
| sqreturn_autocorrelation_ts1_lag3 |  -1.0081    |
| sqreturn_autocorrelation_ts1_lag2 |  -1.17733   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.20361   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.31652   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.53269   |
| intercept                         |  -1.5942    |
| return_kurtosis2                  |  -3.27071   |
| return_kurtosis1                  |  -4.4961    |


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
