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

6.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.672856 |  nan        |
| auc       | 0.875661 |  nan        |
| f1        | 0.873563 |    0.500598 |
| accuracy  | 0.873563 |    0.500598 |
| precision | 0.925    |    0.796094 |
| recall    | 1        |    0        |
| mcc       | 0.752788 |    0.796094 |


## Confusion matrix (at threshold=0.500598)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  38 |                        4 |
| Labeled as simulated |                   7 |                       38 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= 1.176) and (return_sd1 > 1.354) and (sqreturn_autocorrelation_ts2_lag1 <= 0.162) then class: simulated (proba: 99.22%) | based on 128 samples

if (return_kurtosis1 > 1.176) and (sqreturn_autocorrelation_ts1_lag1 > -0.038) and (price1_granger_cause_price2 > 0.001) then class: real (proba: 99.1%) | based on 111 samples

if (return_kurtosis1 <= 1.176) and (return_sd1 <= 1.354) and (return_autocorrelation_1_lag3 <= 0.063) then class: real (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 > 1.176) and (sqreturn_autocorrelation_ts1_lag1 > -0.038) and (price1_granger_cause_price2 <= 0.001) then class: simulated (proba: 60.0%) | based on 5 samples

if (return_kurtosis1 > 1.176) and (sqreturn_autocorrelation_ts1_lag1 <= -0.038) and (price1_granger_cause_price2 <= 0.828) then class: simulated (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 <= 1.176) and (return_sd1 > 1.354) and (sqreturn_autocorrelation_ts2_lag1 > 0.162) then class: real (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 > 1.176) and (sqreturn_autocorrelation_ts1_lag1 <= -0.038) and (price1_granger_cause_price2 > 0.828) then class: real (proba: 100.0%) | based on 1 samples

if (return_kurtosis1 <= 1.176) and (return_sd1 <= 1.354) and (return_autocorrelation_1_lag3 > 0.063) then class: simulated (proba: 100.0%) | based on 1 samples





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
