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

5.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.881504 |  nan        |
| auc       | 0.921512 |  nan        |
| f1        | 0.921348 |    0.636364 |
| accuracy  | 0.91954  |    0.636364 |
| precision | 0.911111 |    0.636364 |
| recall    | 0.977273 |    0        |
| mcc       | 0.839239 |    0.636364 |


## Confusion matrix (at threshold=0.636364)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  39 |                        4 |
| Labeled as simulated |                   3 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= 1.276) and (return_sd1 > 1.679) and (sqreturn_correlation_ts1_lag_0 <= 0.398) then class: simulated (proba: 100.0%) | based on 122 samples

if (return_kurtosis1 > 1.276) and (return_mean2 > -0.263) and (sqreturn_autocorrelation_ts2_lag2 > -0.031) then class: real (proba: 99.05%) | based on 105 samples

if (return_kurtosis1 <= 1.276) and (return_sd1 <= 1.679) then class: real (proba: 100.0%) | based on 13 samples

if (return_kurtosis1 > 1.276) and (return_mean2 > -0.263) and (sqreturn_autocorrelation_ts2_lag2 <= -0.031) then class: real (proba: 72.73%) | based on 11 samples

if (return_kurtosis1 <= 1.276) and (return_sd1 > 1.679) and (sqreturn_correlation_ts1_lag_0 > 0.398) then class: real (proba: 60.0%) | based on 5 samples

if (return_kurtosis1 > 1.276) and (return_mean2 <= -0.263) then class: simulated (proba: 100.0%) | based on 4 samples





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
