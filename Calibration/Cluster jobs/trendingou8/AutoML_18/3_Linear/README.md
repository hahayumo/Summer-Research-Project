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
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0899327 | nan          |
| auc       | 0.998409  | nan          |
| f1        | 0.987952  |   0.497747   |
| accuracy  | 0.988506  |   0.497747   |
| precision | 1         |   0.896599   |
| recall    | 1         |   1.5316e-11 |
| mcc       | 0.977225  |   0.497747   |


## Confusion matrix (at threshold=0.497747)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  45 |                        1 |
| Labeled as simulated |                   0 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_skew1                            |   1.77694   |
| return_correlation_ts1_lag_0            |   1.02124   |
| return_skew2                            |   0.921431  |
| return_mean1                            |   0.88722   |
| return_correlation_ts1_lag_2            |   0.337916  |
| return_autocorrelation_lag1_2           |   0.306076  |
| return_sd2                              |   0.2998    |
| return_autocorrelation_lag1_1           |   0.270093  |
| return_correlation_ts2_lag_2            |   0.263514  |
| return_correlation_ts1_lag_1            |   0.232673  |
| return_correlation_ts2_lag_1            |   0.175568  |
| return_correlation_ts1_lag_3            |   0.0463198 |
| return_correlation_ts2_lag_3            |  -0.0421663 |
| return_sd1                              |  -0.215339  |
| price1_granger_cause_price2             |  -0.386847  |
| return_autocorrelation_lag1_rolling_sd1 |  -0.655589  |
| price2_granger_cause_price1             |  -0.720035  |
| return_mean2                            |  -0.822563  |
| return_autocorrelation_lag1_rolling_sd2 |  -1.00256   |
| intercept                               |  -1.61342   |
| return_kurtosis2                        |  -2.99543   |
| return_kurtosis1                        |  -3.58376   |


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
