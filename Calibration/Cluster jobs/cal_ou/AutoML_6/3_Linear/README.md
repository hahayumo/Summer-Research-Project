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

10.0 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.106328 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.753404    |
| accuracy  | 1        |   0.753404    |
| precision | 1        |   0.753404    |
| recall    | 1        |   8.50193e-11 |
| mcc       | 1        |   0.753404    |


## Confusion matrix (at threshold=0.753404)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        0 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.990161  |
| sqreturn_correlation_ts1_lag_1    |   0.484589  |
| return_correlation_ts1_lag_1      |   0.484589  |
| return_autocorrelation_2_lag1     |   0.435962  |
| return_autocorrelation_1_lag3     |   0.354362  |
| return_autocorrelation_1_lag2     |   0.349961  |
| return_autocorrelation_1_lag1     |   0.299754  |
| return_autocorrelation_2_lag2     |   0.274638  |
| sqreturn_correlation_ts2_lag_1    |   0.263925  |
| return_correlation_ts2_lag_1      |   0.263925  |
| mean2                             |   0.252292  |
| sd1                               |   0.222903  |
| sqreturn_correlation_ts2_lag_3    |   0.207995  |
| return_correlation_ts2_lag_3      |   0.207995  |
| return_correlation_ts1_lag_2      |   0.198923  |
| sqreturn_correlation_ts1_lag_2    |   0.198923  |
| sqreturn_correlation_ts1_lag_3    |   0.16608   |
| return_correlation_ts1_lag_3      |   0.16608   |
| return_autocorrelation_2_lag3     |   0.154639  |
| return_correlation_ts2_lag_2      |   0.0966372 |
| sqreturn_correlation_ts2_lag_2    |   0.0966372 |
| skewness1                         |   0.0746435 |
| return_correlation_ts1_lag_0      |   0.0643373 |
| sqreturn_correlation_ts1_lag_0    |   0.0643373 |
| price1_granger_cause_price2       |  -0.288007  |
| mean1                             |  -0.291836  |
| sd2                               |  -0.442405  |
| price2_granger_cause_price1       |  -0.497333  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.870261  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.883876  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.929072  |
| sqreturn_autocorrelation_ts1_lag1 |  -1.14478   |
| sqreturn_autocorrelation_ts2_lag2 |  -1.16085   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.27137   |
| intercept                         |  -1.3858    |
| kurtosis2                         |  -3.75856   |
| kurtosis1                         |  -3.86303   |


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
