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

4.1 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.124806 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.542566    |
| accuracy  | 1        |   0.542566    |
| precision | 1        |   0.908751    |
| recall    | 1        |   1.62673e-10 |
| mcc       | 1        |   0.542566    |


## Confusion matrix (at threshold=0.542566)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.540596  |
| return_autocorrelation_2_lag1     |   0.400378  |
| return_autocorrelation_2_lag2     |   0.374262  |
| sd1                               |   0.35459   |
| sqreturn_correlation_ts2_lag_1    |   0.321094  |
| return_correlation_ts2_lag_1      |   0.321094  |
| return_correlation_ts1_lag_1      |   0.296396  |
| sqreturn_correlation_ts1_lag_1    |   0.296396  |
| return_autocorrelation_2_lag3     |   0.292468  |
| return_autocorrelation_1_lag3     |   0.254754  |
| sqreturn_correlation_ts2_lag_3    |   0.237186  |
| return_correlation_ts2_lag_3      |   0.237186  |
| return_autocorrelation_1_lag2     |   0.224329  |
| mean2                             |   0.215683  |
| return_autocorrelation_1_lag1     |   0.206785  |
| sqreturn_correlation_ts1_lag_3    |   0.13354   |
| return_correlation_ts1_lag_3      |   0.13354   |
| sqreturn_correlation_ts1_lag_2    |   0.128311  |
| return_correlation_ts1_lag_2      |   0.128311  |
| return_correlation_ts2_lag_2      |   0.0800584 |
| sqreturn_correlation_ts2_lag_2    |   0.0800584 |
| return_correlation_ts1_lag_0      |  -0.0323044 |
| sqreturn_correlation_ts1_lag_0    |  -0.0323044 |
| skewness1                         |  -0.0380322 |
| mean1                             |  -0.112074  |
| sd2                               |  -0.428189  |
| price2_granger_cause_price1       |  -0.470269  |
| price1_granger_cause_price2       |  -0.478314  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.791717  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.909841  |
| sqreturn_autocorrelation_ts2_lag2 |  -1.03489   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.20659   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.30209   |
| intercept                         |  -1.34429   |
| sqreturn_autocorrelation_ts1_lag1 |  -1.35802   |
| kurtosis2                         |  -3.41931   |
| kurtosis1                         |  -4.35132   |


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
