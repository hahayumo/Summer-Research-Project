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

11.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.7646   |  nan        |
| auc       | 0.882664 |  nan        |
| f1        | 0.869565 |    0        |
| accuracy  | 0.862069 |    0        |
| precision | 0.816327 |    0        |
| recall    | 0.930233 |    0        |
| mcc       | 0.706174 |    0.456349 |


## Confusion matrix (at threshold=0.0)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  35 |                        9 |
| Labeled as simulated |                   3 |                       40 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag3 > 0.067) and (kurtosis1 <= 3.352) and (mean2 > 0.018) then class: simulated (proba: 91.27%) | based on 126 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.067) and (kurtosis2 > 1.176) and (sqreturn_autocorrelation_ts2_lag3 <= 0.057) then class: real (proba: 100.0%) | based on 72 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.067) and (kurtosis1 > 3.352) and (mean2 <= 0.099) then class: real (proba: 100.0%) | based on 21 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.067) and (kurtosis2 > 1.176) and (sqreturn_autocorrelation_ts2_lag3 > 0.057) then class: real (proba: 76.92%) | based on 13 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.067) and (kurtosis2 <= 1.176) and (sd2 > 1.521) then class: simulated (proba: 72.73%) | based on 11 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.067) and (kurtosis1 <= 3.352) and (mean2 <= 0.018) then class: real (proba: 100.0%) | based on 6 samples

if (sqreturn_autocorrelation_ts2_lag3 <= 0.067) and (kurtosis2 <= 1.176) and (sd2 <= 1.521) then class: real (proba: 100.0%) | based on 6 samples

if (sqreturn_autocorrelation_ts2_lag3 > 0.067) and (kurtosis1 > 3.352) and (mean2 > 0.099) then class: simulated (proba: 80.0%) | based on 5 samples





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
