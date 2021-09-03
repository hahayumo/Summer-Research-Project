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

11.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.530861 |  nan        |
| auc       | 0.945767 |  nan        |
| f1        | 0.952381 |    0.507874 |
| accuracy  | 0.954023 |    0.507874 |
| precision | 0.952381 |    0.507874 |
| recall    | 0.97619  |    0        |
| mcc       | 0.907937 |    0.507874 |


## Confusion matrix (at threshold=0.507874)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        2 |
| Labeled as simulated |                   2 |                       40 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 > 1.011) and (sqreturn_autocorrelation_ts2_lag1 > -0.031) and (return_autocorrelation_2_lag1 <= 0.13) then class: real (proba: 98.43%) | based on 127 samples

if (return_kurtosis1 <= 1.011) and (return_sd1 > 1.259) and (return_sd1 <= 1.578) then class: simulated (proba: 100.0%) | based on 121 samples

if (return_kurtosis1 > 1.011) and (sqreturn_autocorrelation_ts2_lag1 <= -0.031) and (return_sd2 <= 1.668) then class: simulated (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 <= 1.011) and (return_sd1 > 1.259) and (return_sd1 > 1.578) then class: real (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 <= 1.011) and (return_sd1 <= 1.259) then class: real (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 > 1.011) and (sqreturn_autocorrelation_ts2_lag1 <= -0.031) and (return_sd2 > 1.668) then class: real (proba: 100.0%) | based on 2 samples

if (return_kurtosis1 > 1.011) and (sqreturn_autocorrelation_ts2_lag1 > -0.031) and (return_autocorrelation_2_lag1 > 0.13) then class: simulated (proba: 100.0%) | based on 1 samples





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
