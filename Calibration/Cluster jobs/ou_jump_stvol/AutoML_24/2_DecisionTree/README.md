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

4.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.346793 |  nan        |
| auc       | 0.948732 |  nan        |
| f1        | 0.895833 |    0.470588 |
| accuracy  | 0.885057 |    0.470588 |
| precision | 0.826923 |    0.470588 |
| recall    | 1        |    0        |
| mcc       | 0.783014 |    0.470588 |


## Confusion matrix (at threshold=0.470588)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  34 |                        9 |
| Labeled as simulated |                   1 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= 2.094) and (return_sd1 > 1.394) and (return_sd1 <= 1.844) then class: simulated (proba: 94.12%) | based on 119 samples

if (return_kurtosis1 > 2.094) and (return_skew2 <= 0.226) and (sqreturn_autocorrelation_ts1_lag1 > -0.01) then class: real (proba: 97.67%) | based on 86 samples

if (return_kurtosis1 > 2.094) and (return_skew2 > 0.226) and (return_skew1 > -0.141) then class: simulated (proba: 93.33%) | based on 15 samples

if (return_kurtosis1 <= 2.094) and (return_sd1 <= 1.394) then class: real (proba: 100.0%) | based on 15 samples

if (return_kurtosis1 <= 2.094) and (return_sd1 > 1.394) and (return_sd1 > 1.844) then class: real (proba: 100.0%) | based on 10 samples

if (return_kurtosis1 > 2.094) and (return_skew2 > 0.226) and (return_skew1 <= -0.141) then class: real (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 > 2.094) and (return_skew2 <= 0.226) and (sqreturn_autocorrelation_ts1_lag1 <= -0.01) then class: simulated (proba: 57.14%) | based on 7 samples





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
