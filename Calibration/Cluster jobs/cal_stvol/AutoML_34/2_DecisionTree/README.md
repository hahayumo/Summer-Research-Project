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
| logloss   | 0.904779 | nan         |
| auc       | 0.80814  | nan         |
| f1        | 0.808081 |   0.108108  |
| accuracy  | 0.793103 |   0.506435  |
| precision | 0.770833 |   0.506435  |
| recall    | 1        |   0.0123288 |
| mcc       | 0.588212 |   0.506435  |


## Confusion matrix (at threshold=0.506435)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  32 |                       11 |
| Labeled as simulated |                   7 |                       37 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis2 <= 3.665) and (kurtosis1 <= 2.815) and (sd1 > 1.412) then class: simulated (proba: 90.48%) | based on 126 samples

if (kurtosis2 > 3.665) and (sqreturn_autocorrelation_ts2_lag3 <= 0.27) and (price2_granger_cause_price1 > 0.001) then class: real (proba: 98.63%) | based on 73 samples

if (kurtosis2 <= 3.665) and (kurtosis1 > 2.815) and (return_correlation_ts1_lag_2 <= 0.074) then class: real (proba: 89.19%) | based on 37 samples

if (kurtosis2 <= 3.665) and (kurtosis1 <= 2.815) and (sd1 <= 1.412) then class: real (proba: 64.71%) | based on 17 samples

if (kurtosis2 <= 3.665) and (kurtosis1 > 2.815) and (return_correlation_ts1_lag_2 > 0.074) then class: simulated (proba: 100.0%) | based on 4 samples

if (kurtosis2 > 3.665) and (sqreturn_autocorrelation_ts2_lag3 > 0.27) then class: simulated (proba: 100.0%) | based on 2 samples

if (kurtosis2 > 3.665) and (sqreturn_autocorrelation_ts2_lag3 <= 0.27) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 1 samples





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
