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

16.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.354802 |  nan        |
| auc       | 0.92574  |  nan        |
| f1        | 0.891304 |    0.501117 |
| accuracy  | 0.885057 |    0.501117 |
| precision | 0.836735 |    0.501117 |
| recall    | 1        |    0        |
| mcc       | 0.777862 |    0.501117 |


## Confusion matrix (at threshold=0.501117)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  36 |                        8 |
| Labeled as simulated |                   2 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_sd2 > 1.652) and (return_sd2 <= 1.924) and (sqreturn_autocorrelation_ts1_lag1 <= 0.085) then class: simulated (proba: 97.52%) | based on 121 samples

if (return_sd2 <= 1.652) then class: real (proba: 100.0%) | based on 77 samples

if (return_sd2 > 1.652) and (return_sd2 > 1.924) and (sqreturn_autocorrelation_ts2_lag3 > -0.008) then class: real (proba: 97.3%) | based on 37 samples

if (return_sd2 > 1.652) and (return_sd2 <= 1.924) and (sqreturn_autocorrelation_ts1_lag1 > 0.085) then class: real (proba: 75.0%) | based on 16 samples

if (return_sd2 > 1.652) and (return_sd2 > 1.924) and (sqreturn_autocorrelation_ts2_lag3 <= -0.008) then class: simulated (proba: 77.78%) | based on 9 samples





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
