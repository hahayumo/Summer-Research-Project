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

3.1 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0187401 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.491979    |
| accuracy  | 1         |   0.491979    |
| precision | 1         |   0.983105    |
| recall    | 1         |   2.04087e-09 |
| mcc       | 1         |   0.491979    |


## Confusion matrix (at threshold=0.491979)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        0 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_correlation_ts1_lag_0    |  2.28632    |
| return_correlation_ts1_lag_0      |  2.28632    |
| return_skew1                      |  0.804518   |
| return_skew2                      |  0.499945   |
| return_autocorrelation_1_lag2     |  0.0569115  |
| sqreturn_correlation_ts2_lag_2    |  0.0477816  |
| return_correlation_ts2_lag_2      |  0.0477816  |
| return_autocorrelation_1_lag1     |  0.0466878  |
| return_correlation_ts1_lag_2      |  0.0428728  |
| sqreturn_correlation_ts1_lag_2    |  0.0428728  |
| return_autocorrelation_2_lag1     |  0.0198105  |
| return_sd2                        |  0.012732   |
| return_autocorrelation_2_lag2     |  0.0107238  |
| sqreturn_correlation_ts2_lag_1    | -0.00223625 |
| return_correlation_ts2_lag_1      | -0.00223625 |
| return_mean2                      | -0.0170095  |
| sqreturn_correlation_ts1_lag_1    | -0.0173916  |
| return_correlation_ts1_lag_1      | -0.0173916  |
| price1_granger_cause_price2       | -0.0657163  |
| return_mean1                      | -0.176552   |
| return_autocorrelation_2_lag3     | -0.182799   |
| return_correlation_ts2_lag_3      | -0.19766    |
| sqreturn_correlation_ts2_lag_3    | -0.19766    |
| sqreturn_correlation_ts1_lag_3    | -0.206223   |
| return_correlation_ts1_lag_3      | -0.206223   |
| sqreturn_autocorrelation_ts2_lag1 | -0.206462   |
| return_autocorrelation_1_lag3     | -0.213551   |
| sqreturn_autocorrelation_ts2_lag2 | -0.244703   |
| sqreturn_autocorrelation_ts2_lag3 | -0.249021   |
| sqreturn_autocorrelation_ts1_lag3 | -0.251909   |
| sqreturn_autocorrelation_ts1_lag2 | -0.292056   |
| sqreturn_autocorrelation_ts1_lag1 | -0.348705   |
| price2_granger_cause_price1       | -0.409671   |
| return_sd1                        | -0.576115   |
| return_kurtosis2                  | -0.881755   |
| return_kurtosis1                  | -0.932241   |
| intercept                         | -1.22004    |


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
