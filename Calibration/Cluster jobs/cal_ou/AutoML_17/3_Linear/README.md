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

28.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.148959 | nan           |
| auc       | 1        | nan           |
| f1        | 1        |   0.71366     |
| accuracy  | 1        |   0.71366     |
| precision | 1        |   0.898263    |
| recall    | 1        |   1.77956e-12 |
| mcc       | 1        |   0.71366     |


## Confusion matrix (at threshold=0.71366)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  46 |                        0 |
| Labeled as simulated |                   0 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                           |   Learner_1 |
|:----------------------------------|------------:|
| skewness2                         |   0.534767  |
| return_correlation_ts2_lag_1      |   0.446781  |
| sqreturn_correlation_ts2_lag_1    |   0.446781  |
| sd1                               |   0.397587  |
| return_autocorrelation_2_lag1     |   0.351446  |
| return_correlation_ts1_lag_1      |   0.343586  |
| sqreturn_correlation_ts1_lag_1    |   0.343586  |
| return_autocorrelation_2_lag2     |   0.342789  |
| return_autocorrelation_2_lag3     |   0.30063   |
| skewness1                         |   0.276954  |
| mean2                             |   0.26665   |
| sqreturn_correlation_ts2_lag_3    |   0.172287  |
| return_correlation_ts2_lag_3      |   0.172287  |
| return_correlation_ts2_lag_2      |   0.167927  |
| sqreturn_correlation_ts2_lag_2    |   0.167927  |
| sqreturn_correlation_ts1_lag_3    |   0.134703  |
| return_correlation_ts1_lag_3      |   0.134703  |
| return_autocorrelation_1_lag1     |   0.120844  |
| return_autocorrelation_1_lag3     |   0.0987413 |
| return_correlation_ts1_lag_2      |   0.0942158 |
| sqreturn_correlation_ts1_lag_2    |   0.0942158 |
| return_autocorrelation_1_lag2     |   0.0801202 |
| mean1                             |  -0.0286608 |
| return_correlation_ts1_lag_0      |  -0.0842242 |
| sqreturn_correlation_ts1_lag_0    |  -0.0842242 |
| price1_granger_cause_price2       |  -0.179841  |
| price2_granger_cause_price1       |  -0.21208   |
| sd2                               |  -0.355162  |
| sqreturn_autocorrelation_ts2_lag3 |  -0.795882  |
| sqreturn_autocorrelation_ts1_lag3 |  -0.894179  |
| sqreturn_autocorrelation_ts2_lag2 |  -0.941348  |
| sqreturn_autocorrelation_ts1_lag1 |  -1.12961   |
| sqreturn_autocorrelation_ts1_lag2 |  -1.29737   |
| sqreturn_autocorrelation_ts2_lag1 |  -1.42385   |
| intercept                         |  -1.8026    |
| kurtosis2                         |  -3.36166   |
| kurtosis1                         |  -4.54932   |


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
