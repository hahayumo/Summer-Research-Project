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

21.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.969209 |  nan        |
| auc       | 0.839059 |  nan        |
| f1        | 0.83871  |    0.452756 |
| accuracy  | 0.827586 |    0.452756 |
| precision | 0.813953 |    0.721987 |
| recall    | 0.931818 |    0        |
| mcc       | 0.659051 |    0.452756 |


## Confusion matrix (at threshold=0.452756)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  33 |                       10 |
| Labeled as simulated |                   5 |                       39 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis2 <= 4.098) and (kurtosis1 <= 2.884) and (sqreturn_autocorrelation_ts2_lag3 > 0.023) then class: simulated (proba: 90.55%) | based on 127 samples

if (kurtosis2 > 4.098) and (price2_granger_cause_price1 > 0.001) and (sqreturn_autocorrelation_ts2_lag3 <= 0.223) then class: real (proba: 100.0%) | based on 70 samples

if (kurtosis2 <= 4.098) and (kurtosis1 > 2.884) and (sqreturn_autocorrelation_ts2_lag3 <= 0.107) then class: real (proba: 100.0%) | based on 24 samples

if (kurtosis2 <= 4.098) and (kurtosis1 <= 2.884) and (sqreturn_autocorrelation_ts2_lag3 <= 0.023) then class: real (proba: 66.67%) | based on 18 samples

if (kurtosis2 <= 4.098) and (kurtosis1 > 2.884) and (sqreturn_autocorrelation_ts2_lag3 > 0.107) then class: simulated (proba: 53.85%) | based on 13 samples

if (kurtosis2 > 4.098) and (price2_granger_cause_price1 > 0.001) and (sqreturn_autocorrelation_ts2_lag3 > 0.223) then class: real (proba: 60.0%) | based on 5 samples

if (kurtosis2 > 4.098) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 3 samples





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
