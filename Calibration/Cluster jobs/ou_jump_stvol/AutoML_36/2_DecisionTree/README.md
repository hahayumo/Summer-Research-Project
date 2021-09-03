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

18.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.948829 | nan         |
| auc       | 0.828571 | nan         |
| f1        | 0.845361 |   0.0306122 |
| accuracy  | 0.827586 |   0.0306122 |
| precision | 0.808511 |   0.486607  |
| recall    | 0.977778 |   0         |
| mcc       | 0.661573 |   0.0306122 |


## Confusion matrix (at threshold=0.030612)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  31 |                       11 |
| Labeled as simulated |                   4 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts2_lag1 <= 0.025) and (return_sd1 > 1.467) and (return_sd2 > 1.528) then class: simulated (proba: 97.32%) | based on 112 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.025) and (return_kurtosis1 > 0.802) and (sqreturn_autocorrelation_ts1_lag1 > 0.001) then class: real (proba: 96.94%) | based on 98 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.025) and (return_kurtosis1 <= 0.802) and (sqreturn_autocorrelation_ts2_lag1 <= 0.155) then class: simulated (proba: 100.0%) | based on 15 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.025) and (return_kurtosis1 > 0.802) and (sqreturn_autocorrelation_ts1_lag1 <= 0.001) then class: real (proba: 57.14%) | based on 14 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.025) and (return_sd1 <= 1.467) then class: real (proba: 100.0%) | based on 14 samples

if (sqreturn_autocorrelation_ts2_lag1 <= 0.025) and (return_sd1 > 1.467) and (return_sd2 <= 1.528) then class: real (proba: 100.0%) | based on 5 samples

if (sqreturn_autocorrelation_ts2_lag1 > 0.025) and (return_kurtosis1 <= 0.802) and (sqreturn_autocorrelation_ts2_lag1 > 0.155) then class: real (proba: 100.0%) | based on 2 samples





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
