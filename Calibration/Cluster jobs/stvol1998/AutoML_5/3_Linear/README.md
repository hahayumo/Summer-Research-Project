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

3.9 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0908078 | nan         |
| auc       | 0.996829  | nan         |
| f1        | 0.976744  |   0.498006  |
| accuracy  | 0.977011  |   0.498006  |
| precision | 1         |   0.98213   |
| recall    | 1         |   3.077e-06 |
| mcc       | 0.954017  |   0.498006  |


## Confusion matrix (at threshold=0.498006)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        1 |
| Labeled as simulated |                   1 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |   Learner_1 |
|:----------------------------------------|------------:|
| return_autocorrelation_lag1_rolling_sd1 |   2.34021   |
| return_autocorrelation_lag1_rolling_sd2 |   2.21131   |
| return_sd1                              |   1.00257   |
| price2_granger_cause_price1             |   0.667788  |
| return_skew2                            |   0.327473  |
| return_sd2                              |   0.187666  |
| return_autocorrelation_lag1_1           |   0.160084  |
| return_kurtosis1                        |   0.104335  |
| return_correlation_ts1_lag_1            |   0.102232  |
| price1_granger_cause_price2             |   0.0419478 |
| return_kurtosis2                        |   0.0201777 |
| return_correlation_ts1_lag_2            |  -0.0276008 |
| return_correlation_ts2_lag_2            |  -0.146755  |
| return_autocorrelation_lag1_2           |  -0.210606  |
| return_correlation_ts2_lag_1            |  -0.228714  |
| return_correlation_ts1_lag_3            |  -0.262078  |
| return_correlation_ts2_lag_3            |  -0.425672  |
| return_skew1                            |  -0.516088  |
| return_correlation_ts1_lag_0            |  -0.563559  |
| intercept                               |  -0.602955  |
| return_mean1                            |  -0.673305  |
| return_mean2                            |  -1.27126   |


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
