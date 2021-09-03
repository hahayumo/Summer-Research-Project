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

4.6 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.217733 | nan           |
| auc       | 0.986786 | nan           |
| f1        | 0.964706 |   0.660661    |
| accuracy  | 0.965517 |   0.660661    |
| precision | 1        |   0.805502    |
| recall    | 1        |   5.96007e-15 |
| mcc       | 0.931253 |   0.660661    |


## Confusion matrix (at threshold=0.660661)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        1 |
| Labeled as simulated |                   2 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_skew1                      |   0.919791  |
| return_skew2                      |   0.870864  |
| return_autocorrelation_1_lag2     |   0.635487  |
| sqreturn_correlation_ts1_lag_1    |   0.593182  |
| return_correlation_ts1_lag_1      |   0.593182  |
| return_autocorrelation_1_lag1     |   0.580372  |
| sqreturn_correlation_ts1_lag_2    |   0.390346  |
| return_correlation_ts1_lag_2      |   0.390346  |
| return_correlation_ts2_lag_2      |   0.370535  |
| sqreturn_correlation_ts2_lag_2    |   0.370535  |
| return_autocorrelation_2_lag2     |   0.353622  |
| return_autocorrelation_2_lag1     |   0.343646  |
| sqreturn_correlation_ts2_lag_1    |   0.315952  |
| return_correlation_ts2_lag_1      |   0.315952  |
| return_autocorrelation_1_lag3     |   0.249448  |
| return_correlation_ts2_lag_3      |   0.222918  |
| sqreturn_correlation_ts2_lag_3    |   0.222918  |
| return_sd2                        |   0.167119  |
| return_sd1                        |   0.12727   |
| sqreturn_correlation_ts1_lag_3    |   0.122395  |
| return_correlation_ts1_lag_3      |   0.122395  |
| return_autocorrelation_2_lag3     |   0.0791303 |
| return_mean1                      |   0.0646694 |
| sqreturn_autocorrelation_ts2_lag3 |  -0.356776  |
| intercept                         |  -0.432625  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.439481  |
| price2_granger_cause_price1       |  -0.484758  |
| sqreturn_correlation_ts1_lag_0    |  -0.615579  |
| return_correlation_ts1_lag_0      |  -0.615579  |
| return_mean2                      |  -0.630811  |
| price1_granger_cause_price2       |  -0.76864   |
| sqreturn_autocorrelation_ts2_lag2 |  -0.805981  |
| sqreturn_autocorrelation_ts2_lag1 |  -1.03258   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.03838   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.55972   |
| return_kurtosis1                  |  -2.43779   |
| return_kurtosis2                  |  -3.57546   |


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
