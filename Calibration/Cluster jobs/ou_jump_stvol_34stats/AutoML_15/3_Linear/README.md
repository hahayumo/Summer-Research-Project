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
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.153448 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.532304    |
| accuracy  | 1        |   0.532304    |
| precision | 1        |   0.690842    |
| recall    | 1        |   2.03724e-12 |
| mcc       | 1        |   0.532304    |


## Confusion matrix (at threshold=0.532304)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_mean1                      |   1.59045   |
| return_skew1                      |   0.869297  |
| return_sd1                        |   0.708237  |
| price1_granger_cause_price2       |   0.705638  |
| return_kurtosis2                  |   0.445017  |
| return_autocorrelation_2_lag2     |   0.407507  |
| return_correlation_ts1_lag_1      |   0.36498   |
| sqreturn_correlation_ts1_lag_1    |   0.36498   |
| return_autocorrelation_2_lag1     |   0.3541    |
| return_autocorrelation_1_lag1     |   0.31085   |
| return_skew2                      |   0.281277  |
| sqreturn_correlation_ts1_lag_2    |   0.252495  |
| return_correlation_ts1_lag_2      |   0.252495  |
| return_autocorrelation_1_lag2     |   0.186475  |
| sqreturn_correlation_ts2_lag_2    |   0.138334  |
| return_correlation_ts2_lag_2      |   0.138334  |
| return_autocorrelation_1_lag3     |   0.0586123 |
| price2_granger_cause_price1       |   0.0120673 |
| return_autocorrelation_2_lag3     |  -0.0080451 |
| return_correlation_ts2_lag_1      |  -0.0522411 |
| sqreturn_correlation_ts2_lag_1    |  -0.0522411 |
| return_sd2                        |  -0.0733935 |
| sqreturn_correlation_ts2_lag_3    |  -0.13887   |
| return_correlation_ts2_lag_3      |  -0.13887   |
| sqreturn_autocorrelation_ts2_lag3 |  -0.153416  |
| sqreturn_correlation_ts1_lag_3    |  -0.28209   |
| return_correlation_ts1_lag_3      |  -0.28209   |
| sqreturn_autocorrelation_ts2_lag2 |  -0.583507  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.584086  |
| sqreturn_correlation_ts1_lag_0    |  -0.627199  |
| return_correlation_ts1_lag_0      |  -0.627199  |
| intercept                         |  -0.899292  |
| sqreturn_autocorrelation_ts2_lag1 |  -0.946054  |
| sqreturn_autocorrelation_ts1_lag2 |  -1.21249   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.50033   |
| return_kurtosis1                  |  -3.59852   |
| return_mean2                      |  -4.02071   |


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
