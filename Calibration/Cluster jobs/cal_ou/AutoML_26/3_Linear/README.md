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

149.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.127229 | nan           |
| auc       | 1        | nan           |
| f1        | 0.988506 |   0.56161     |
| accuracy  | 0.988506 |   0.56161     |
| precision | 1        |   0.88289     |
| recall    | 1        |   1.47408e-20 |
| mcc       | 0.977273 |   0.56161     |


## Confusion matrix (at threshold=0.56161)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        1 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| sd1                               |   0.455518  |
| skewness2                         |   0.428571  |
| return_autocorrelation_2_lag3     |   0.372627  |
| return_correlation_ts1_lag_1      |   0.361343  |
| sqreturn_correlation_ts1_lag_1    |   0.361343  |
| return_correlation_ts2_lag_1      |   0.342965  |
| sqreturn_correlation_ts2_lag_1    |   0.342965  |
| mean2                             |   0.260742  |
| return_autocorrelation_2_lag2     |   0.259307  |
| return_correlation_ts1_lag_3      |   0.253153  |
| sqreturn_correlation_ts1_lag_3    |   0.253153  |
| return_autocorrelation_2_lag1     |   0.230243  |
| return_autocorrelation_1_lag2     |   0.192472  |
| return_correlation_ts2_lag_3      |   0.165178  |
| sqreturn_correlation_ts2_lag_3    |   0.165178  |
| skewness1                         |   0.143152  |
| return_autocorrelation_1_lag3     |   0.121067  |
| sqreturn_correlation_ts2_lag_2    |   0.11173   |
| return_correlation_ts2_lag_2      |   0.11173   |
| return_correlation_ts1_lag_2      |   0.0977635 |
| sqreturn_correlation_ts1_lag_2    |   0.0977635 |
| return_autocorrelation_1_lag1     |   0.0972184 |
| price1_granger_cause_price2       |  -0.0227307 |
| sqreturn_correlation_ts1_lag_0    |  -0.189132  |
| return_correlation_ts1_lag_0      |  -0.189132  |
| mean1                             |  -0.238297  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.39901   |
| sd2                               |  -0.407676  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.710847  |
| sqreturn_autocorrelation_ts2_lag2 |  -0.734405  |
| sqreturn_autocorrelation_ts1_lag1 |  -0.769024  |
| price2_granger_cause_price1       |  -0.790665  |
| sqreturn_autocorrelation_ts2_lag1 |  -0.822011  |
| sqreturn_autocorrelation_ts1_lag2 |  -0.926717  |
| intercept                         |  -1.57765   |
| kurtosis2                         |  -3.92271   |
| kurtosis1                         |  -3.94731   |


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
