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

12.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.366535 |  nan        |
| auc       | 0.922569 |  nan        |
| f1        | 0.880952 |    0.694444 |
| accuracy  | 0.885057 |    0.694444 |
| precision | 0.925    |    0.694444 |
| recall    | 1        |    0        |
| mcc       | 0.773599 |    0.694444 |


## Confusion matrix (at threshold=0.694444)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  40 |                        3 |
| Labeled as simulated |                   7 |                       37 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= 2.096) and (return_sd1 > 1.441) and (sqreturn_autocorrelation_ts1_lag2 <= 0.061) then class: simulated (proba: 98.18%) | based on 110 samples

if (return_kurtosis1 > 2.096) and (sqreturn_autocorrelation_ts1_lag1 > 0.01) and (sqreturn_autocorrelation_ts1_lag3 > -0.018) then class: real (proba: 98.84%) | based on 86 samples

if (return_kurtosis1 > 2.096) and (sqreturn_autocorrelation_ts1_lag1 <= 0.01) and (return_sd2 > 1.681) then class: simulated (proba: 88.89%) | based on 18 samples

if (return_kurtosis1 <= 2.096) and (return_sd1 <= 1.441) then class: real (proba: 100.0%) | based on 18 samples

if (return_kurtosis1 <= 2.096) and (return_sd1 > 1.441) and (sqreturn_autocorrelation_ts1_lag2 > 0.061) then class: real (proba: 68.75%) | based on 16 samples

if (return_kurtosis1 > 2.096) and (sqreturn_autocorrelation_ts1_lag1 > 0.01) and (sqreturn_autocorrelation_ts1_lag3 <= -0.018) then class: real (proba: 50.0%) | based on 6 samples

if (return_kurtosis1 > 2.096) and (sqreturn_autocorrelation_ts1_lag1 <= 0.01) and (return_sd2 <= 1.681) then class: real (proba: 100.0%) | based on 6 samples





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
