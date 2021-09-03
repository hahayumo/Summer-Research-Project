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

16.0 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.230608 | nan           |
| auc       | 0.989429 | nan           |
| f1        | 0.964706 |   0.65325     |
| accuracy  | 0.965517 |   0.70826     |
| precision | 1        |   0.878847    |
| recall    | 1        |   1.20625e-07 |
| mcc       | 0.933197 |   0.70826     |


## Confusion matrix (at threshold=0.70826)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   3 |                       40 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag2     |   0.73133   |
| sqreturn_correlation_ts1_lag_2    |   0.497227  |
| return_correlation_ts1_lag_2      |   0.497227  |
| return_autocorrelation_2_lag1     |   0.457494  |
| return_autocorrelation_1_lag2     |   0.424679  |
| sqreturn_correlation_ts2_lag_1    |   0.420022  |
| return_correlation_ts2_lag_1      |   0.420022  |
| return_autocorrelation_2_lag3     |   0.414506  |
| return_correlation_ts1_lag_1      |   0.382088  |
| sqreturn_correlation_ts1_lag_1    |   0.382088  |
| sqreturn_correlation_ts1_lag_3    |   0.341373  |
| return_correlation_ts1_lag_3      |   0.341373  |
| return_autocorrelation_1_lag3     |   0.333444  |
| return_mean2                      |   0.293752  |
| sqreturn_correlation_ts2_lag_3    |   0.259297  |
| return_correlation_ts2_lag_3      |   0.259297  |
| return_autocorrelation_1_lag1     |   0.226257  |
| sqreturn_correlation_ts1_lag_0    |   0.159413  |
| return_correlation_ts1_lag_0      |   0.159413  |
| sqreturn_correlation_ts2_lag_2    |   0.0770866 |
| return_correlation_ts2_lag_2      |   0.0770866 |
| return_skew2                      |  -0.0138209 |
| price2_granger_cause_price1       |  -0.026441  |
| return_skew1                      |  -0.116844  |
| return_sd2                        |  -0.31281   |
| return_sd1                        |  -0.316383  |
| intercept                         |  -0.771835  |
| price1_granger_cause_price2       |  -0.836923  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.8984    |
| return_mean1                      |  -0.954298  |
| sqreturn_autocorrelation_ts1_lag3 |  -1.12602   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.18193   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.339     |
| sqreturn_autocorrelation_ts2_lag1 |  -1.63194   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.77049   |
| return_kurtosis2                  |  -2.19843   |
| return_kurtosis1                  |  -3.23414   |


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
