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

4.3 seconds

## Metric details
|           |      score |     threshold |
|:----------|-----------:|--------------:|
| logloss   | 0.00596431 | nan           |
| auc       | 1          | nan           |
| f1        | 1          |   0.498233    |
| accuracy  | 1          |   0.498233    |
| precision | 1          |   0.498233    |
| recall    | 1          |   0.000353446 |
| mcc       | 1          |   0.498233    |


## Confusion matrix (at threshold=0.498233)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        0 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| intercept                         |   4.05692   |
| return_sd1                        |   0.570786  |
| return_sd2                        |   0.503409  |
| price2_granger_cause_price1       |   0.0985449 |
| return_skew2                      |   0.0493287 |
| price1_granger_cause_price2       |   0.0133511 |
| return_correlation_ts1_lag_3      |  -0.0762093 |
| sqreturn_correlation_ts1_lag_3    |  -0.0762093 |
| return_correlation_ts1_lag_1      |  -0.0765678 |
| sqreturn_correlation_ts1_lag_1    |  -0.0765678 |
| sqreturn_correlation_ts2_lag_2    |  -0.0780329 |
| return_correlation_ts2_lag_2      |  -0.0780329 |
| sqreturn_correlation_ts1_lag_2    |  -0.0805542 |
| return_correlation_ts1_lag_2      |  -0.0805542 |
| sqreturn_correlation_ts2_lag_3    |  -0.0806237 |
| return_correlation_ts2_lag_3      |  -0.0806237 |
| return_correlation_ts1_lag_0      |  -0.0848439 |
| sqreturn_correlation_ts1_lag_0    |  -0.0848439 |
| sqreturn_correlation_ts2_lag_1    |  -0.0869318 |
| return_correlation_ts2_lag_1      |  -0.0869318 |
| return_skew1                      |  -0.128899  |
| return_mean1                      |  -0.280043  |
| return_mean2                      |  -0.29624   |
| return_kurtosis1                  |  -0.449091  |
| return_kurtosis2                  |  -0.519824  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.668471  |
| return_autocorrelation_2_lag3     |  -0.670858  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.671154  |
| return_autocorrelation_1_lag3     |  -0.672342  |
| return_autocorrelation_2_lag2     |  -0.680328  |
| sqreturn_autocorrelation_ts2_lag2 |  -0.681126  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.682115  |
| return_autocorrelation_1_lag2     |  -0.682698  |
| sqreturn_autocorrelation_ts2_lag1 |  -0.687678  |
| return_autocorrelation_1_lag1     |  -0.688406  |
| return_autocorrelation_2_lag1     |  -0.688719  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.688767  |


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
