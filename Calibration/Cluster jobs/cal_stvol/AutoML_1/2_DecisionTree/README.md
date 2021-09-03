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

9.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.164742 |  nan        |
| auc       | 0.988636 |  nan        |
| f1        | 0.988506 |    0        |
| accuracy  | 0.988506 |    0        |
| precision | 1        |    0        |
| recall    | 0.977273 |    0        |
| mcc       | 0.977273 |    0.496032 |


## Confusion matrix (at threshold=0.0)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  43 |                        0 |
| Labeled as simulated |                   1 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (mean2 > 0.138) and (sqreturn_correlation_ts1_lag_0 > 0.356) and (sd2 <= 2.636) then class: simulated (proba: 99.21%) | based on 126 samples

if (mean2 <= 0.138) and (kurtosis1 > 1.037) then class: real (proba: 100.0%) | based on 106 samples

if (mean2 > 0.138) and (sqreturn_correlation_ts1_lag_0 <= 0.356) and (return_correlation_ts1_lag_2 > -0.064) then class: real (proba: 100.0%) | based on 12 samples

if (mean2 <= 0.138) and (kurtosis1 <= 1.037) and (sqreturn_correlation_ts1_lag_0 > 0.439) then class: simulated (proba: 83.33%) | based on 6 samples

if (mean2 <= 0.138) and (kurtosis1 <= 1.037) and (sqreturn_correlation_ts1_lag_0 <= 0.439) then class: real (proba: 100.0%) | based on 6 samples

if (mean2 > 0.138) and (sqreturn_correlation_ts1_lag_0 > 0.356) and (sd2 > 2.636) then class: real (proba: 100.0%) | based on 3 samples

if (mean2 > 0.138) and (sqreturn_correlation_ts1_lag_0 <= 0.356) and (return_correlation_ts1_lag_2 <= -0.064) then class: simulated (proba: 100.0%) | based on 1 samples





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
