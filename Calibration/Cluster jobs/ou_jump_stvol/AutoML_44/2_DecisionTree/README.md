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

5.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.62907  |       nan   |
| auc       | 0.939482 |       nan   |
| f1        | 0.923077 |         0.5 |
| accuracy  | 0.91954  |         0.5 |
| precision | 0.893617 |         0.5 |
| recall    | 1        |         0   |
| mcc       | 0.840937 |         0.5 |


## Confusion matrix (at threshold=0.5)
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

if (return_kurtosis1 <= 0.901) and (return_sd1 > 1.523) and (sqreturn_correlation_ts1_lag_0 > 0.273) then class: simulated (proba: 100.0%) | based on 117 samples

if (return_kurtosis1 > 0.901) and (sqreturn_autocorrelation_ts1_lag1 > -0.01) and (return_kurtosis2 > 0.329) then class: real (proba: 97.41%) | based on 116 samples

if (return_kurtosis1 > 0.901) and (sqreturn_autocorrelation_ts1_lag1 <= -0.01) and (return_correlation_ts1_lag_0 > 0.366) then class: simulated (proba: 90.91%) | based on 11 samples

if (return_kurtosis1 > 0.901) and (sqreturn_autocorrelation_ts1_lag1 <= -0.01) and (return_correlation_ts1_lag_0 <= 0.366) then class: real (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 <= 0.901) and (return_sd1 <= 1.523) then class: real (proba: 100.0%) | based on 5 samples

if (return_kurtosis1 > 0.901) and (sqreturn_autocorrelation_ts1_lag1 > -0.01) and (return_kurtosis2 <= 0.329) then class: simulated (proba: 100.0%) | based on 2 samples

if (return_kurtosis1 <= 0.901) and (return_sd1 > 1.523) and (sqreturn_correlation_ts1_lag_0 <= 0.273) then class: real (proba: 100.0%) | based on 1 samples





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
