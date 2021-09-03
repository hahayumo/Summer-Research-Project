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

18.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.428795 | nan         |
| auc       | 0.873277 | nan         |
| f1        | 0.853659 |   0.406863  |
| accuracy  | 0.862069 |   0.406863  |
| precision | 1        |   0.951923  |
| recall    | 1        |   0.0310345 |
| mcc       | 0.723224 |   0.406863  |


## Confusion matrix (at threshold=0.406863)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  40 |                        6 |
| Labeled as simulated |                   6 |                       35 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 2.795) and (sqreturn_autocorrelation_ts2_lag3 > 0.07) and (sqreturn_correlation_ts1_lag_0 <= 0.438) then class: simulated (proba: 95.19%) | based on 104 samples

if (kurtosis1 > 2.795) and (return_correlation_ts1_lag_2 <= 0.11) and (price1_granger_cause_price2 > 0.0) then class: real (proba: 95.1%) | based on 102 samples

if (kurtosis1 <= 2.795) and (sqreturn_autocorrelation_ts2_lag3 <= 0.07) and (sd1 <= 1.893) then class: real (proba: 96.55%) | based on 29 samples

if (kurtosis1 <= 2.795) and (sqreturn_autocorrelation_ts2_lag3 <= 0.07) and (sd1 > 1.893) then class: simulated (proba: 76.47%) | based on 17 samples

if (kurtosis1 <= 2.795) and (sqreturn_autocorrelation_ts2_lag3 > 0.07) and (sqreturn_correlation_ts1_lag_0 > 0.438) then class: real (proba: 75.0%) | based on 4 samples

if (kurtosis1 > 2.795) and (return_correlation_ts1_lag_2 > 0.11) then class: simulated (proba: 100.0%) | based on 2 samples

if (kurtosis1 > 2.795) and (return_correlation_ts1_lag_2 <= 0.11) and (price1_granger_cause_price2 <= 0.0) then class: simulated (proba: 100.0%) | based on 2 samples





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
