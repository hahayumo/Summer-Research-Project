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

8.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.647894 |  nan        |
| auc       | 0.910148 |  nan        |
| f1        | 0.923077 |    0.501218 |
| accuracy  | 0.91954  |    0.501218 |
| precision | 0.893617 |    0.501218 |
| recall    | 1        |    0        |
| mcc       | 0.840937 |    0.501218 |


## Confusion matrix (at threshold=0.501218)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  38 |                        5 |
| Labeled as simulated |                   2 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag1 <= 0.017) and (sqreturn_autocorrelation_ts1_lag1 <= 0.081) and (sqreturn_correlation_ts1_lag_0 > 0.211) then class: simulated (proba: 98.18%) | based on 110 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.017) and (return_kurtosis1 > 0.894) and (sqreturn_autocorrelation_ts1_lag3 > -0.023) then class: real (proba: 97.94%) | based on 97 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.017) and (return_kurtosis1 <= 0.894) and (return_correlation_ts1_lag_0 > 0.256) then class: simulated (proba: 100.0%) | based on 15 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.017) and (sqreturn_autocorrelation_ts1_lag1 > 0.081) then class: real (proba: 100.0%) | based on 13 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.017) and (return_kurtosis1 > 0.894) and (sqreturn_autocorrelation_ts1_lag3 <= -0.023) then class: simulated (proba: 58.33%) | based on 12 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.017) and (sqreturn_autocorrelation_ts1_lag1 <= 0.081) and (sqreturn_correlation_ts1_lag_0 <= 0.211) then class: real (proba: 100.0%) | based on 7 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.017) and (return_kurtosis1 <= 0.894) and (return_correlation_ts1_lag_0 <= 0.256) then class: real (proba: 83.33%) | based on 6 samples





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
