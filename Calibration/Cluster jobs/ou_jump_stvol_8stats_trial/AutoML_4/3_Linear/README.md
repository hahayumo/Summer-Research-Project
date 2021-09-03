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

4.2 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0190163 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.49617     |
| accuracy  | 1         |   0.49617     |
| precision | 1         |   0.49617     |
| recall    | 1         |   3.95418e-09 |
| mcc       | 1         |   0.49617     |


## Confusion matrix (at threshold=0.49617)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_correlation_ts1_lag_0    |  2.19353    |
| return_correlation_ts1_lag_0      |  2.19353    |
| return_skew2                      |  0.864148   |
| return_skew1                      |  0.758048   |
| return_autocorrelation_1_lag2     |  0.112786   |
| sqreturn_correlation_ts1_lag_2    |  0.110314   |
| return_correlation_ts1_lag_2      |  0.110314   |
| return_correlation_ts2_lag_2      |  0.0902324  |
| sqreturn_correlation_ts2_lag_2    |  0.0902324  |
| return_autocorrelation_1_lag1     |  0.0879781  |
| return_autocorrelation_2_lag2     |  0.0805461  |
| return_correlation_ts1_lag_1      |  0.0276369  |
| sqreturn_correlation_ts1_lag_1    |  0.0276369  |
| sqreturn_correlation_ts2_lag_1    |  0.00710003 |
| return_correlation_ts2_lag_1      |  0.00710003 |
| return_autocorrelation_2_lag1     |  0.0061407  |
| return_mean2                      | -0.0409453  |
| price1_granger_cause_price2       | -0.0480602  |
| return_sd2                        | -0.161981   |
| return_autocorrelation_1_lag3     | -0.185736   |
| return_mean1                      | -0.186255   |
| sqreturn_correlation_ts2_lag_3    | -0.204833   |
| return_correlation_ts2_lag_3      | -0.204833   |
| sqreturn_autocorrelation_ts1_lag2 | -0.211529   |
| return_autocorrelation_2_lag3     | -0.212854   |
| sqreturn_correlation_ts1_lag_3    | -0.237616   |
| return_correlation_ts1_lag_3      | -0.237616   |
| sqreturn_autocorrelation_ts2_lag2 | -0.247426   |
| sqreturn_autocorrelation_ts2_lag1 | -0.263746   |
| sqreturn_autocorrelation_ts1_lag3 | -0.290486   |
| sqreturn_autocorrelation_ts2_lag3 | -0.299578   |
| sqreturn_autocorrelation_ts1_lag1 | -0.303142   |
| price2_granger_cause_price1       | -0.468964   |
| return_sd1                        | -0.653949   |
| return_kurtosis2                  | -0.854676   |
| return_kurtosis1                  | -1.00228    |
| intercept                         | -1.15986    |


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
