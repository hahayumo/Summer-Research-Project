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

8.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.328702 |         nan |
| auc       | 0.929365 |         nan |
| f1        | 0.672    |           0 |
| accuracy  | 0.528736 |           0 |
| precision | 0.506024 |           0 |
| recall    | 1        |           0 |
| mcc       | 0        |           0 |


## Confusion matrix (at threshold=0.0)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                   4 |                       41 |
| Labeled as simulated |                   0 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 > 1.514) and (sqreturn_autocorrelation_ts1_lag1 > 0.008) and (return_mean1 > -0.115) then class: real (proba: 95.24%) | based on 105 samples

if (return_kurtosis1 <= 1.514) and (return_sd2 > 1.64) and (return_sd2 <= 2.054) then class: simulated (proba: 97.8%) | based on 91 samples

if (return_kurtosis1 > 1.514) and (sqreturn_autocorrelation_ts1_lag1 <= 0.008) and (sqreturn_autocorrelation_ts2_lag1 <= 0.033) then class: simulated (proba: 95.83%) | based on 24 samples

if (return_kurtosis1 > 1.514) and (sqreturn_autocorrelation_ts1_lag1 <= 0.008) and (sqreturn_autocorrelation_ts2_lag1 > 0.033) then class: real (proba: 73.33%) | based on 15 samples

if (return_kurtosis1 <= 1.514) and (return_sd2 <= 1.64) then class: real (proba: 100.0%) | based on 13 samples

if (return_kurtosis1 > 1.514) and (sqreturn_autocorrelation_ts1_lag1 > 0.008) and (return_mean1 <= -0.115) then class: simulated (proba: 75.0%) | based on 8 samples

if (return_kurtosis1 <= 1.514) and (return_sd2 > 1.64) and (return_sd2 > 2.054) then class: real (proba: 100.0%) | based on 4 samples





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
