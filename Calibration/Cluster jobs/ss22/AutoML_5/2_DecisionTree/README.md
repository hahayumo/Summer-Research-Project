# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
accuracy

## Training time

6.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.476398 |       nan   |
| auc       | 0.965909 |       nan   |
| f1        | 0.966292 |         0   |
| accuracy  | 0.965517 |         0   |
| precision | 0.934783 |         0   |
| recall    | 1        |         0   |
| mcc       | 0.933299 |         0.5 |


## Confusion matrix (at threshold=0.0)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        3 |
| Labeled as simulated |                   0 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_autocorrelation_lag1_rolling_sd2 > 0.979) and (co_integration_statistic > 0.016) and (durbin_watson_statistic1 <= 2.273) then class: simulated (proba: 100.0%) | based on 125 samples

if (return_autocorrelation_lag1_rolling_sd2 <= 0.979) and (return_correlation_ts1_lag_0 > -0.133) then class: real (proba: 100.0%) | based on 125 samples

if (return_autocorrelation_lag1_rolling_sd2 > 0.979) and (co_integration_statistic <= 0.016) and (standardised_price_mean1 <= 118.461) then class: real (proba: 100.0%) | based on 6 samples

if (return_autocorrelation_lag1_rolling_sd2 > 0.979) and (co_integration_statistic <= 0.016) and (standardised_price_mean1 > 118.461) then class: simulated (proba: 100.0%) | based on 2 samples

if (return_autocorrelation_lag1_rolling_sd2 > 0.979) and (co_integration_statistic > 0.016) and (durbin_watson_statistic1 > 2.273) then class: real (proba: 100.0%) | based on 1 samples

if (return_autocorrelation_lag1_rolling_sd2 <= 0.979) and (return_correlation_ts1_lag_0 <= -0.133) then class: simulated (proba: 100.0%) | based on 1 samples





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
