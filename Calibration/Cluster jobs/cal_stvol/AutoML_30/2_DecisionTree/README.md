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

17.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.31197  |  nan        |
| auc       | 0.741516 |  nan        |
| f1        | 0.752941 |    0.457274 |
| accuracy  | 0.758621 |    0.457274 |
| precision | 0.738095 |    0.722155 |
| recall    | 0.95122  |    0        |
| mcc       | 0.518794 |    0.457274 |


## Confusion matrix (at threshold=0.457274)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  34 |                       12 |
| Labeled as simulated |                   9 |                       32 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 2.496) and (sqreturn_autocorrelation_ts2_lag3 > 0.029) and (sqreturn_autocorrelation_ts1_lag3 > 0.001) then class: simulated (proba: 87.29%) | based on 118 samples

if (kurtosis1 > 2.496) and (price2_granger_cause_price1 > 0.001) and (return_autocorrelation_1_lag3 <= 0.087) then class: real (proba: 95.83%) | based on 96 samples

if (kurtosis1 <= 2.496) and (sqreturn_autocorrelation_ts2_lag3 <= 0.029) and (kurtosis1 > 0.633) then class: real (proba: 95.24%) | based on 21 samples

if (kurtosis1 > 2.496) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 9 samples

if (kurtosis1 > 2.496) and (price2_granger_cause_price1 > 0.001) and (return_autocorrelation_1_lag3 > 0.087) then class: simulated (proba: 57.14%) | based on 7 samples

if (kurtosis1 <= 2.496) and (sqreturn_autocorrelation_ts2_lag3 > 0.029) and (sqreturn_autocorrelation_ts1_lag3 <= 0.001) then class: real (proba: 100.0%) | based on 7 samples

if (kurtosis1 <= 2.496) and (sqreturn_autocorrelation_ts2_lag3 <= 0.029) and (kurtosis1 <= 0.633) then class: simulated (proba: 100.0%) | based on 2 samples





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
