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
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0260795 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.497987    |
| accuracy  | 1         |   0.497987    |
| precision | 1         |   0.497987    |
| recall    | 1         |   4.38302e-08 |
| mcc       | 1         |   0.497987    |


## Confusion matrix (at threshold=0.497987)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_autocorrelation_ts2_lag3 |   1.21754   |
| return_autocorrelation_2_lag3     |   1.12446   |
| return_autocorrelation_2_lag1     |   1.11664   |
| sqreturn_autocorrelation_ts2_lag2 |   1.11537   |
| return_autocorrelation_2_lag2     |   1.07427   |
| sqreturn_autocorrelation_ts2_lag1 |   1.02931   |
| sqreturn_correlation_ts1_lag_3    |   0.276854  |
| return_correlation_ts1_lag_3      |   0.276854  |
| return_autocorrelation_1_lag1     |   0.272336  |
| skewness1                         |   0.24702   |
| sqreturn_correlation_ts2_lag_1    |   0.231347  |
| return_correlation_ts2_lag_1      |   0.231347  |
| return_correlation_ts1_lag_1      |   0.226858  |
| sqreturn_correlation_ts1_lag_1    |   0.226858  |
| return_autocorrelation_1_lag2     |   0.224294  |
| sqreturn_correlation_ts1_lag_2    |   0.223523  |
| return_correlation_ts1_lag_2      |   0.223523  |
| sqreturn_correlation_ts2_lag_3    |   0.203731  |
| return_correlation_ts2_lag_3      |   0.203731  |
| return_autocorrelation_1_lag3     |   0.174596  |
| sqreturn_correlation_ts2_lag_2    |   0.149073  |
| return_correlation_ts2_lag_2      |   0.149073  |
| return_correlation_ts1_lag_0      |  -0.0585829 |
| sqreturn_correlation_ts1_lag_0    |  -0.0585829 |
| price2_granger_cause_price1       |  -0.135497  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.138259  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.167026  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.251872  |
| price1_granger_cause_price2       |  -0.490022  |
| sd2                               |  -0.547965  |
| sd1                               |  -0.591188  |
| skewness2                         |  -0.653011  |
| kurtosis2                         |  -0.658895  |
| mean2                             |  -0.741845  |
| kurtosis1                         |  -1.43772   |
| mean1                             |  -1.71511   |
| intercept                         |  -3.09725   |


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
