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

14.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.04211  |  nan        |
| auc       | 0.775899 |  nan        |
| f1        | 0.808081 |    0.424138 |
| accuracy  | 0.781609 |    0.424138 |
| precision | 0.727273 |    0.424138 |
| recall    | 0.909091 |    0        |
| mcc       | 0.580883 |    0.424138 |


## Confusion matrix (at threshold=0.424138)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  28 |                       15 |
| Labeled as simulated |                   4 |                       40 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag2 > 0.051) and (sqreturn_correlation_ts1_lag_0 <= 0.451) and (return_correlation_ts1_lag_0 > 0.251) then class: simulated (proba: 84.83%) | based on 145 samples

if (sqreturn_autocorrelation_ts2_lag2 <= 0.051) and (kurtosis2 > 1.612) then class: real (proba: 100.0%) | based on 69 samples

if (sqreturn_autocorrelation_ts2_lag2 > 0.051) and (sqreturn_correlation_ts1_lag_0 > 0.451) then class: real (proba: 100.0%) | based on 18 samples

if (sqreturn_autocorrelation_ts2_lag2 > 0.051) and (sqreturn_correlation_ts1_lag_0 <= 0.451) and (return_correlation_ts1_lag_0 <= 0.251) then class: real (proba: 100.0%) | based on 11 samples

if (sqreturn_autocorrelation_ts2_lag2 <= 0.051) and (kurtosis2 <= 1.612) and (sqreturn_correlation_ts1_lag_0 > 0.354) then class: simulated (proba: 88.89%) | based on 9 samples

if (sqreturn_autocorrelation_ts2_lag2 <= 0.051) and (kurtosis2 <= 1.612) and (sqreturn_correlation_ts1_lag_0 <= 0.354) then class: real (proba: 87.5%) | based on 8 samples





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
