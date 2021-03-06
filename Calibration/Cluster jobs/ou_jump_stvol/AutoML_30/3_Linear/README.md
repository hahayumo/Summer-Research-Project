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

11.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.300275 | nan           |
| auc       | 0.995772 | nan           |
| f1        | 0.966292 |   0.571003    |
| accuracy  | 0.965517 |   0.656119    |
| precision | 1        |   0.656119    |
| recall    | 1        |   0.000108252 |
| mcc       | 0.933299 |   0.656119    |


## Confusion matrix (at threshold=0.656119)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   3 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| return_mean2                      |   1.65319   |
| return_correlation_ts1_lag_0      |   0.981303  |
| sqreturn_correlation_ts1_lag_0    |   0.981303  |
| return_autocorrelation_1_lag1     |   0.750846  |
| return_autocorrelation_1_lag3     |   0.736567  |
| sqreturn_correlation_ts1_lag_1    |   0.65827   |
| return_correlation_ts1_lag_1      |   0.65827   |
| return_autocorrelation_1_lag2     |   0.583342  |
| return_autocorrelation_2_lag1     |   0.543979  |
| sqreturn_correlation_ts2_lag_1    |   0.496938  |
| return_correlation_ts2_lag_1      |   0.496938  |
| return_autocorrelation_2_lag2     |   0.455863  |
| return_autocorrelation_2_lag3     |   0.436903  |
| return_correlation_ts1_lag_2      |   0.406518  |
| sqreturn_correlation_ts1_lag_2    |   0.406518  |
| sqreturn_correlation_ts2_lag_3    |   0.404476  |
| return_correlation_ts2_lag_3      |   0.404476  |
| sqreturn_correlation_ts1_lag_3    |   0.345639  |
| return_correlation_ts1_lag_3      |   0.345639  |
| sqreturn_correlation_ts2_lag_2    |   0.258442  |
| return_correlation_ts2_lag_2      |   0.258442  |
| return_skew2                      |   0.0617824 |
| return_sd2                        |   0.0134051 |
| return_sd1                        |  -0.0205853 |
| intercept                         |  -0.271798  |
| return_skew1                      |  -0.327659  |
| price1_granger_cause_price2       |  -0.510886  |
| return_kurtosis2                  |  -0.811474  |
| price2_granger_cause_price1       |  -0.970882  |
| sqreturn_autocorrelation_ts2_lag3 |  -1.25001   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.411     |
| return_mean1                      |  -1.55138   |
| return_kurtosis1                  |  -1.59909   |
| sqreturn_autocorrelation_ts1_lag3 |  -1.75128   |
| sqreturn_autocorrelation_ts1_lag1 |  -2.38799   |
| sqreturn_autocorrelation_ts2_lag1 |  -2.41106   |
| sqreturn_autocorrelation_ts1_lag2 |  -2.44385   |


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
