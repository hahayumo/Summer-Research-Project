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

4.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.386819 |  nan        |
| auc       | 0.884514 |  nan        |
| f1        | 0.888889 |    0.448439 |
| accuracy  | 0.885057 |    0.448439 |
| precision | 0.863636 |    0.75436  |
| recall    | 1        |    0        |
| mcc       | 0.773599 |    0.448439 |


## Confusion matrix (at threshold=0.448439)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  37 |                        7 |
| Labeled as simulated |                   3 |                       40 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag3 > 0.053) and (kurtosis1 <= 3.73) and (return_correlation_ts1_lag_0 <= 0.458) then class: simulated (proba: 88.37%) | based on 129 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.053) and (kurtosis1 > 0.986) and (return_autocorrelation_1_lag1 <= 0.08) then class: real (proba: 98.68%) | based on 76 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.053) and (kurtosis1 > 3.73) and (mean2 <= 0.13) then class: real (proba: 95.83%) | based on 24 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.053) and (kurtosis1 <= 3.73) and (return_correlation_ts1_lag_0 > 0.458) then class: real (proba: 88.89%) | based on 9 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.053) and (kurtosis1 > 3.73) and (mean2 > 0.13) then class: simulated (proba: 62.5%) | based on 8 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.053) and (kurtosis1 > 0.986) and (return_autocorrelation_1_lag1 > 0.08) then class: real (proba: 66.67%) | based on 6 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.053) and (kurtosis1 <= 0.986) and (sqreturn_autocorrelation_ts2_lag1 > 0.054) then class: simulated (proba: 100.0%) | based on 5 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.053) and (kurtosis1 <= 0.986) and (sqreturn_autocorrelation_ts2_lag1 <= 0.054) then class: real (proba: 100.0%) | based on 3 samples





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
