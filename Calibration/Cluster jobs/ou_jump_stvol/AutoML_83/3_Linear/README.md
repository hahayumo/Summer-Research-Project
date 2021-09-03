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

5.6 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.144035 | nan           |
| auc       | 0.995772 | nan           |
| f1        | 0.97619  |   0.674645    |
| accuracy  | 0.977011 |   0.674645    |
| precision | 1        |   0.938588    |
| recall    | 1        |   1.21575e-25 |
| mcc       | 0.955004 |   0.674645    |


## Confusion matrix (at threshold=0.674645)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   2 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_autocorrelation_2_lag1     |   0.729878  |
| return_correlation_ts2_lag_1      |   0.508363  |
| sqreturn_correlation_ts2_lag_1    |   0.508363  |
| return_autocorrelation_2_lag2     |   0.495714  |
| return_correlation_ts1_lag_1      |   0.35949   |
| sqreturn_correlation_ts1_lag_1    |   0.35949   |
| return_autocorrelation_1_lag1     |   0.349484  |
| return_autocorrelation_1_lag2     |   0.243889  |
| return_autocorrelation_1_lag3     |   0.183795  |
| return_autocorrelation_2_lag3     |   0.171573  |
| return_correlation_ts1_lag_3      |   0.157306  |
| sqreturn_correlation_ts1_lag_3    |   0.157306  |
| return_correlation_ts1_lag_2      |   0.144552  |
| sqreturn_correlation_ts1_lag_2    |   0.144552  |
| return_correlation_ts2_lag_3      |   0.0866153 |
| sqreturn_correlation_ts2_lag_3    |   0.0866153 |
| return_mean2                      |  -0.0233061 |
| return_correlation_ts1_lag_0      |  -0.0540877 |
| sqreturn_correlation_ts1_lag_0    |  -0.0540877 |
| return_sd1                        |  -0.101115  |
| return_correlation_ts2_lag_2      |  -0.132004  |
| sqreturn_correlation_ts2_lag_2    |  -0.132004  |
| return_skew1                      |  -0.186168  |
| return_sd2                        |  -0.351869  |
| return_skew2                      |  -0.41949   |
| price1_granger_cause_price2       |  -0.491175  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.787732  |
| return_mean1                      |  -0.800531  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.863214  |
| price2_granger_cause_price1       |  -1.04489   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.06861   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.07488   |
| intercept                         |  -1.08649   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.55497   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.60984   |
| return_kurtosis2                  |  -2.57849   |
| return_kurtosis1                  |  -3.74377   |


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
