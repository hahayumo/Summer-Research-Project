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

5.1 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0206625 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.399646    |
| accuracy  | 1         |   0.399646    |
| precision | 1         |   0.399646    |
| recall    | 1         |   0.000157864 |
| mcc       | 1         |   0.399646    |


## Confusion matrix (at threshold=0.399646)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_autocorrelation_ts2_lag3 |   1.2157    |
| return_autocorrelation_2_lag1     |   1.19979   |
| sqreturn_autocorrelation_ts2_lag2 |   1.1781    |
| return_autocorrelation_2_lag2     |   1.11324   |
| sqreturn_autocorrelation_ts2_lag1 |   1.08917   |
| return_autocorrelation_2_lag3     |   1.08007   |
| sqreturn_correlation_ts1_lag_1    |   0.33411   |
| return_correlation_ts1_lag_1      |   0.33411   |
| sqreturn_correlation_ts2_lag_3    |   0.286889  |
| return_correlation_ts2_lag_3      |   0.286889  |
| sqreturn_correlation_ts2_lag_1    |   0.263119  |
| return_correlation_ts2_lag_1      |   0.263119  |
| sqreturn_correlation_ts2_lag_2    |   0.256626  |
| return_correlation_ts2_lag_2      |   0.256626  |
| return_autocorrelation_1_lag1     |   0.246791  |
| return_autocorrelation_1_lag2     |   0.235844  |
| return_autocorrelation_1_lag3     |   0.232032  |
| return_correlation_ts1_lag_2      |   0.219509  |
| sqreturn_correlation_ts1_lag_2    |   0.219509  |
| return_correlation_ts1_lag_3      |   0.212443  |
| sqreturn_correlation_ts1_lag_3    |   0.212443  |
| skewness1                         |   0.0280409 |
| return_correlation_ts1_lag_0      |   0.0234994 |
| sqreturn_correlation_ts1_lag_0    |   0.0234994 |
| sqreturn_autocorrelation_ts1_lag3 |  -0.161101  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.222731  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.23954   |
| price2_granger_cause_price1       |  -0.416185  |
| sd2                               |  -0.451485  |
| price1_granger_cause_price2       |  -0.529562  |
| sd1                               |  -0.553566  |
| skewness2                         |  -0.571331  |
| kurtosis2                         |  -0.748542  |
| mean2                             |  -0.789034  |
| kurtosis1                         |  -1.26231   |
| mean1                             |  -1.73645   |
| intercept                         |  -3.13183   |


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
