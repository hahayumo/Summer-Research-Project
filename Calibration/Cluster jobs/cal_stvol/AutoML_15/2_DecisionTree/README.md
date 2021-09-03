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

13.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.753575 |      nan    |
| auc       | 0.810254 |      nan    |
| f1        | 0.814815 |        0    |
| accuracy  | 0.793103 |        0.66 |
| precision | 0.76     |        0.66 |
| recall    | 1        |        0    |
| mcc       | 0.60641  |        0    |


## Confusion matrix (at threshold=0.66)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  31 |                       12 |
| Labeled as simulated |                   6 |                       38 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 3.346) and (sqreturn_autocorrelation_ts2_lag3 > 0.023) and (kurtosis2 <= 3.093) then class: simulated (proba: 92.0%) | based on 125 samples

if (kurtosis1 > 3.346) and (return_correlation_ts1_lag_2 <= 0.113) and (price1_granger_cause_price2 <= 0.798) then class: real (proba: 100.0%) | based on 74 samples

if (kurtosis1 <= 3.346) and (sqreturn_autocorrelation_ts2_lag3 > 0.023) and (kurtosis2 > 3.093) then class: real (proba: 56.67%) | based on 30 samples

if (kurtosis1 <= 3.346) and (sqreturn_autocorrelation_ts2_lag3 <= 0.023) and (return_autocorrelation_1_lag2 <= 0.045) then class: real (proba: 100.0%) | based on 24 samples

if (kurtosis1 > 3.346) and (return_correlation_ts1_lag_2 <= 0.113) and (price1_granger_cause_price2 > 0.798) then class: real (proba: 60.0%) | based on 5 samples

if (kurtosis1 > 3.346) and (return_correlation_ts1_lag_2 > 0.113) then class: simulated (proba: 100.0%) | based on 1 samples

if (kurtosis1 <= 3.346) and (sqreturn_autocorrelation_ts2_lag3 <= 0.023) and (return_autocorrelation_1_lag2 > 0.045) then class: simulated (proba: 100.0%) | based on 1 samples





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
