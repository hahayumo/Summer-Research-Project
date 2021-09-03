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

20.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.54095  |  nan        |
| auc       | 0.936839 |  nan        |
| f1        | 0.915663 |    0.504065 |
| accuracy  | 0.91954  |    0.504065 |
| precision | 0.95     |    0.504065 |
| recall    | 1        |    0        |
| mcc       | 0.840937 |    0.504065 |


## Confusion matrix (at threshold=0.504065)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        2 |
| Labeled as simulated |                   5 |                       38 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 > 0.856) and (sqreturn_autocorrelation_ts2_lag1 > -0.007) and (return_kurtosis2 > 0.308) then class: real (proba: 99.19%) | based on 123 samples

if (return_kurtosis1 <= 0.856) and (return_sd1 > 1.204) and (return_sd2 > 1.354) then class: simulated (proba: 100.0%) | based on 116 samples

if (return_kurtosis1 > 0.856) and (sqreturn_autocorrelation_ts2_lag1 <= -0.007) and (sqreturn_autocorrelation_ts1_lag1 > 0.005) then class: real (proba: 87.5%) | based on 8 samples

if (return_kurtosis1 > 0.856) and (sqreturn_autocorrelation_ts2_lag1 <= -0.007) and (sqreturn_autocorrelation_ts1_lag1 <= 0.005) then class: simulated (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 <= 0.856) and (return_sd1 <= 1.204) then class: real (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 > 0.856) and (sqreturn_autocorrelation_ts2_lag1 > -0.007) and (return_kurtosis2 <= 0.308) then class: simulated (proba: 100.0%) | based on 1 samples

if (return_kurtosis1 <= 0.856) and (return_sd1 > 1.204) and (return_sd2 <= 1.354) then class: real (proba: 100.0%) | based on 1 samples





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
