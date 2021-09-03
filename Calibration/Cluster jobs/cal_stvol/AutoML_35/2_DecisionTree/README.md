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

14.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.95773  |  nan        |
| auc       | 0.830867 |  nan        |
| f1        | 0.82     |    0        |
| accuracy  | 0.793103 |    0        |
| precision | 0.76087  |    0.485294 |
| recall    | 0.931818 |    0        |
| mcc       | 0.608611 |    0        |


## Confusion matrix (at threshold=0.0)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  28 |                       15 |
| Labeled as simulated |                   3 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 2.342) and (kurtosis2 <= 2.808) and (sd1 > 1.722) then class: simulated (proba: 97.06%) | based on 102 samples

if (kurtosis1 > 2.342) and (sqreturn_autocorrelation_ts2_lag3 <= 0.144) and (kurtosis2 > 0.517) then class: real (proba: 100.0%) | based on 77 samples

if (kurtosis1 <= 2.342) and (kurtosis2 > 2.808) and (mean2 <= 0.099) then class: real (proba: 100.0%) | based on 23 samples

if (kurtosis1 > 2.342) and (sqreturn_autocorrelation_ts2_lag3 > 0.144) and (sqreturn_correlation_ts1_lag_0 <= 0.467) then class: simulated (proba: 88.89%) | based on 18 samples

if (kurtosis1 <= 2.342) and (kurtosis2 <= 2.808) and (sd1 <= 1.722) then class: real (proba: 55.56%) | based on 18 samples

if (kurtosis1 > 2.342) and (sqreturn_autocorrelation_ts2_lag3 > 0.144) and (sqreturn_correlation_ts1_lag_0 > 0.467) then class: real (proba: 100.0%) | based on 13 samples

if (kurtosis1 <= 2.342) and (kurtosis2 > 2.808) and (mean2 > 0.099) then class: simulated (proba: 75.0%) | based on 8 samples

if (kurtosis1 > 2.342) and (sqreturn_autocorrelation_ts2_lag3 <= 0.144) and (kurtosis2 <= 0.517) then class: simulated (proba: 100.0%) | based on 1 samples





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
