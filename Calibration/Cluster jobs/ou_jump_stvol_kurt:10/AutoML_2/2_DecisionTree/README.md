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
| logloss   | 0.708716 | nan         |
| auc       | 0.897463 | nan         |
| f1        | 0.891566 |   0.0543478 |
| accuracy  | 0.896552 |   0.0543478 |
| precision | 0.970588 |   0.527174  |
| recall    | 0.953488 |   0         |
| mcc       | 0.794808 |   0.0543478 |


## Confusion matrix (at threshold=0.054348)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        3 |
| Labeled as simulated |                   6 |                       37 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts1_lag3 > 0.083) and (return_correlation_ts1_lag_0 > 0.381) and (return_mean2 > -0.056) then class: simulated (proba: 100.0%) | based on 95 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.083) and (sqreturn_correlation_ts1_lag_0 <= 0.473) and (return_correlation_ts2_lag_3 > -0.101) then class: real (proba: 94.57%) | based on 92 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.083) and (sqreturn_correlation_ts1_lag_0 > 0.473) and (return_kurtosis2 > 1.127) then class: real (proba: 75.0%) | based on 28 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.083) and (return_correlation_ts1_lag_0 <= 0.381) and (sqreturn_autocorrelation_ts2_lag2 <= 0.111) then class: real (proba: 100.0%) | based on 18 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.083) and (sqreturn_correlation_ts1_lag_0 > 0.473) and (return_kurtosis2 <= 1.127) then class: simulated (proba: 93.33%) | based on 15 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.083) and (return_correlation_ts1_lag_0 > 0.381) and (return_mean2 <= -0.056) then class: real (proba: 80.0%) | based on 5 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.083) and (return_correlation_ts1_lag_0 <= 0.381) and (sqreturn_autocorrelation_ts2_lag2 > 0.111) then class: simulated (proba: 100.0%) | based on 5 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.083) and (sqreturn_correlation_ts1_lag_0 <= 0.473) and (return_correlation_ts2_lag_3 <= -0.101) then class: simulated (proba: 100.0%) | based on 2 samples





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
