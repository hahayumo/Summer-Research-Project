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

7.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.549432 |  nan        |
| auc       | 0.953488 |  nan        |
| f1        | 0.94382  |    0.516129 |
| accuracy  | 0.942529 |    0.516129 |
| precision | 0.913043 |    0.516129 |
| recall    | 1        |    0        |
| mcc       | 0.887243 |    0.516129 |


## Confusion matrix (at threshold=0.516129)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  40 |                        4 |
| Labeled as simulated |                   1 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis2 > 0.843) and (return_kurtosis1 > 0.7) and (sqreturn_autocorrelation_ts1_lag2 > -0.059) then class: real (proba: 96.77%) | based on 124 samples

if (return_kurtosis2 <= 0.843) and (return_kurtosis1 <= 1.353) then class: simulated (proba: 100.0%) | based on 115 samples

if (return_kurtosis2 <= 0.843) and (return_kurtosis1 > 1.353) and (sqreturn_correlation_ts1_lag_0 > 0.317) then class: real (proba: 100.0%) | based on 7 samples

if (return_kurtosis2 > 0.843) and (return_kurtosis1 <= 0.7) and (return_autocorrelation_2_lag2 > -0.046) then class: simulated (proba: 100.0%) | based on 5 samples

if (return_kurtosis2 > 0.843) and (return_kurtosis1 <= 0.7) and (return_autocorrelation_2_lag2 <= -0.046) then class: real (proba: 100.0%) | based on 4 samples

if (return_kurtosis2 <= 0.843) and (return_kurtosis1 > 1.353) and (sqreturn_correlation_ts1_lag_0 <= 0.317) then class: simulated (proba: 75.0%) | based on 4 samples

if (return_kurtosis2 > 0.843) and (return_kurtosis1 > 0.7) and (sqreturn_autocorrelation_ts1_lag2 <= -0.059) then class: simulated (proba: 100.0%) | based on 1 samples





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
