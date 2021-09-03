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
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.163895 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.733568    |
| accuracy  | 1        |   0.733568    |
| precision | 1        |   0.893074    |
| recall    | 1        |   3.77387e-29 |
| mcc       | 1        |   0.733568    |


## Confusion matrix (at threshold=0.733568)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  45 |                        0 |
| Labeled as simulated |                   0 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.806803  |
| sqreturn_correlation_ts1_lag_1    |   0.481871  |
| return_correlation_ts1_lag_1      |   0.481871  |
| sd1                               |   0.46833   |
| skewness1                         |   0.363799  |
| return_autocorrelation_2_lag1     |   0.320645  |
| return_correlation_ts1_lag_2      |   0.292971  |
| sqreturn_correlation_ts1_lag_2    |   0.292971  |
| return_correlation_ts1_lag_3      |   0.291672  |
| sqreturn_correlation_ts1_lag_3    |   0.291672  |
| return_autocorrelation_1_lag2     |   0.268544  |
| sqreturn_correlation_ts2_lag_1    |   0.259557  |
| return_correlation_ts2_lag_1      |   0.259557  |
| return_autocorrelation_2_lag2     |   0.253181  |
| return_correlation_ts2_lag_3      |   0.222087  |
| sqreturn_correlation_ts2_lag_3    |   0.222087  |
| return_autocorrelation_1_lag1     |   0.17793   |
| return_autocorrelation_2_lag3     |   0.156378  |
| sqreturn_correlation_ts1_lag_0    |   0.142972  |
| return_correlation_ts1_lag_0      |   0.142972  |
| sqreturn_correlation_ts2_lag_2    |   0.136558  |
| return_correlation_ts2_lag_2      |   0.136558  |
| mean2                             |   0.125862  |
| return_autocorrelation_1_lag3     |   0.103017  |
| price1_granger_cause_price2       |   0.0157212 |
| mean1                             |  -0.102905  |
| price2_granger_cause_price1       |  -0.215554  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.549051  |
| sd2                               |  -0.714172  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.76127   |
| sqreturn_autocorrelation_ts1_lag2 |  -0.843589  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.952001  |
| sqreturn_autocorrelation_ts2_lag2 |  -1.00452   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.09734   |
| intercept                         |  -1.97558   |
| kurtosis2                         |  -3.70975   |
| kurtosis1                         |  -3.90603   |


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
