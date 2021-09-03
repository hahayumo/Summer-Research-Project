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

10.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0204579 | nan           |
| auc       | 1         | nan           |
| f1        | 1         |   0.524954    |
| accuracy  | 1         |   0.524954    |
| precision | 1         |   0.524954    |
| recall    | 1         |   8.28564e-06 |
| mcc       | 1         |   0.524954    |


## Confusion matrix (at threshold=0.524954)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   0 |                       44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                                 |    Learner_1 |
|:----------------------------------------|-------------:|
| return_autocorrelation_lag1_rolling_sd2 |  1.62312     |
| standardised_price_mean1                |  1.33802     |
| return_autocorrelation_lag1_rolling_sd1 |  1.28741     |
| return_sd2                              |  1.15363     |
| co_integration_statistic                |  0.628167    |
| price_adf_p_values                      |  0.379342    |
| return_mean1                            |  0.35504     |
| durbin_watson_statistic2                |  0.245647    |
| price2_granger_cause_price1             |  0.168681    |
| return_sd1                              |  0.0863719   |
| return_correlation_ts1_lag_2            |  0.0407563   |
| return_correlation_ts2_lag_2            |  0.0312645   |
| return_autocorrelation_lag1_1           |  0.0236185   |
| return_autocorrelation_lag1_2           |  0.000955157 |
| return_correlation_ts2_lag_1            |  0.000405672 |
| price1_granger_cause_price2             | -0.00330754  |
| return_correlation_ts1_lag_1            | -0.0034068   |
| return_correlation_ts1_lag_0            | -0.0891018   |
| return_correlation_ts1_lag_3            | -0.124141    |
| return_skew2                            | -0.125589    |
| return_correlation_ts2_lag_3            | -0.153135    |
| durbin_watson_statistic1                | -0.180924    |
| return_skew1                            | -0.191212    |
| return_kurtosis1                        | -0.206807    |
| return_kurtosis2                        | -0.207951    |
| intercept                               | -0.41518     |
| return_mean2                            | -0.475949    |
| standardised_price_mean2                | -2.08573     |


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
