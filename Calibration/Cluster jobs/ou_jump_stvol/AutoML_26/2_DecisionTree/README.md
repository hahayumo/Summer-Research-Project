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

5.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.10083  | nan         |
| auc       | 0.823545 | nan         |
| f1        | 0.822222 |   0.0114943 |
| accuracy  | 0.816092 |   0.0114943 |
| precision | 1        |   0.967742  |
| recall    | 0.911111 |   0         |
| mcc       | 0.639561 |   0.489618  |


## Confusion matrix (at threshold=0.011494)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  34 |                        8 |
| Labeled as simulated |                   8 |                       37 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag1 <= 0.024) and (sqreturn_correlation_ts1_lag_0 > 0.266) and (return_sd2 > 1.561) then class: simulated (proba: 96.77%) | based on 124 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.024) and (return_kurtosis1 > 0.67) and (sqreturn_autocorrelation_ts1_lag1 > 0.007) then class: real (proba: 98.85%) | based on 87 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.024) and (return_kurtosis1 > 0.67) and (sqreturn_autocorrelation_ts1_lag1 <= 0.007) then class: real (proba: 57.89%) | based on 19 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.024) and (sqreturn_correlation_ts1_lag_0 <= 0.266) then class: real (proba: 100.0%) | based on 15 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.024) and (return_kurtosis1 <= 0.67) and (return_sd2 <= 2.027) then class: simulated (proba: 100.0%) | based on 7 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.024) and (sqreturn_correlation_ts1_lag_0 > 0.266) and (return_sd2 <= 1.561) then class: real (proba: 100.0%) | based on 6 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.024) and (return_kurtosis1 <= 0.67) and (return_sd2 > 2.027) then class: real (proba: 100.0%) | based on 2 samples





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
