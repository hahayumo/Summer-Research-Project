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

3.3 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0101568 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.490813    |
| accuracy  | 1         |   0.490813    |
| precision | 1         |   0.490813    |
| recall    | 1         |   9.66622e-07 |
| mcc       | 1         |   0.490813    |


## Confusion matrix (at threshold=0.490813)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  44 |                        0 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sqreturn_correlation_ts1_lag_0    |  2.58866    |
| return_correlation_ts1_lag_0      |  2.58866    |
| return_sd2                        |  0.339732   |
| return_skew2                      |  0.312202   |
| return_skew1                      |  0.243003   |
| return_autocorrelation_1_lag2     |  0.104222   |
| sqreturn_correlation_ts1_lag_2    |  0.103786   |
| return_correlation_ts1_lag_2      |  0.103786   |
| price1_granger_cause_price2       |  0.094808   |
| return_autocorrelation_1_lag1     |  0.0485959  |
| sqreturn_correlation_ts2_lag_2    |  0.0451892  |
| return_correlation_ts2_lag_2      |  0.0451892  |
| return_autocorrelation_2_lag2     |  0.019258   |
| price2_granger_cause_price1       |  0.00952807 |
| return_correlation_ts1_lag_1      |  0.00467321 |
| sqreturn_correlation_ts1_lag_1    |  0.00467321 |
| return_autocorrelation_2_lag1     | -0.0266968  |
| sqreturn_correlation_ts2_lag_1    | -0.0272111  |
| return_correlation_ts2_lag_1      | -0.0272111  |
| return_autocorrelation_2_lag3     | -0.0421946  |
| sqreturn_correlation_ts2_lag_3    | -0.0501975  |
| return_correlation_ts2_lag_3      | -0.0501975  |
| return_autocorrelation_1_lag3     | -0.0533633  |
| sqreturn_autocorrelation_ts2_lag3 | -0.0719033  |
| sqreturn_correlation_ts1_lag_3    | -0.0888772  |
| return_correlation_ts1_lag_3      | -0.0888772  |
| sqreturn_autocorrelation_ts1_lag2 | -0.116385   |
| sqreturn_autocorrelation_ts2_lag2 | -0.116609   |
| sqreturn_autocorrelation_ts1_lag3 | -0.135167   |
| return_mean1                      | -0.145023   |
| return_mean2                      | -0.147003   |
| return_sd1                        | -0.149599   |
| sqreturn_autocorrelation_ts2_lag1 | -0.20327    |
| sqreturn_autocorrelation_ts1_lag1 | -0.21341    |
| return_kurtosis2                  | -0.421379   |
| return_kurtosis1                  | -0.612581   |
| intercept                         | -1.36837    |


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
