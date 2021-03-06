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

4.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.343363 |  nan        |
| auc       | 0.918081 |  nan        |
| f1        | 0.883721 |    0.442033 |
| accuracy  | 0.885057 |    0.442033 |
| precision | 0.844444 |    0.442033 |
| recall    | 1        |    0        |
| mcc       | 0.773835 |    0.442033 |


## Confusion matrix (at threshold=0.442033)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  39 |                        7 |
| Labeled as simulated |                   3 |                       38 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis2 <= 3.676) and (sqreturn_autocorrelation_ts1_lag3 > 0.046) and (sqreturn_correlation_ts1_lag_0 <= 0.477) then class: simulated (proba: 85.94%) | based on 128 samples

if (kurtosis2 > 3.676) and (sqreturn_autocorrelation_ts2_lag3 <= 0.317) and (price2_granger_cause_price1 > 0.001) then class: real (proba: 97.53%) | based on 81 samples

if (kurtosis2 <= 3.676) and (sqreturn_autocorrelation_ts1_lag3 <= 0.046) and (kurtosis1 > 1.292) then class: real (proba: 96.43%) | based on 28 samples

if (kurtosis2 <= 3.676) and (sqreturn_autocorrelation_ts1_lag3 <= 0.046) and (kurtosis1 <= 1.292) then class: simulated (proba: 72.73%) | based on 11 samples

if (kurtosis2 <= 3.676) and (sqreturn_autocorrelation_ts1_lag3 > 0.046) and (sqreturn_correlation_ts1_lag_0 > 0.477) then class: real (proba: 100.0%) | based on 10 samples

if (kurtosis2 > 3.676) and (sqreturn_autocorrelation_ts2_lag3 > 0.317) then class: simulated (proba: 100.0%) | based on 1 samples

if (kurtosis2 > 3.676) and (sqreturn_autocorrelation_ts2_lag3 <= 0.317) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 1 samples





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
