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

4.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.65799  | nan         |
| auc       | 0.895349 | nan         |
| f1        | 0.924731 |   0.468673  |
| accuracy  | 0.91954  |   0.468673  |
| precision | 0.877551 |   0.468673  |
| recall    | 1        |   0.0111111 |
| mcc       | 0.84446  |   0.468673  |


## Confusion matrix (at threshold=0.468673)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  37 |                        6 |
| Labeled as simulated |                   1 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis2 <= 2.905) and (sqreturn_correlation_ts1_lag_0 > 0.343) and (sqreturn_correlation_ts1_lag_0 <= 0.486) then class: simulated (proba: 92.5%) | based on 120 samples

if (kurtosis2 > 2.905) and (mean1 <= 0.139) and (return_correlation_ts1_lag_1 <= 0.138) then class: real (proba: 98.77%) | based on 81 samples

if (kurtosis2 <= 2.905) and (sqreturn_correlation_ts1_lag_0 <= 0.343) and (sqreturn_autocorrelation_ts2_lag2 <= 0.142) then class: real (proba: 89.66%) | based on 29 samples

if (kurtosis2 <= 2.905) and (sqreturn_correlation_ts1_lag_0 > 0.343) and (sqreturn_correlation_ts1_lag_0 > 0.486) then class: real (proba: 77.78%) | based on 9 samples

if (kurtosis2 > 2.905) and (mean1 > 0.139) and (kurtosis2 > 5.55) then class: real (proba: 100.0%) | based on 7 samples

if (kurtosis2 > 2.905) and (mean1 > 0.139) and (kurtosis2 <= 5.55) then class: simulated (proba: 100.0%) | based on 7 samples

if (kurtosis2 <= 2.905) and (sqreturn_correlation_ts1_lag_0 <= 0.343) and (sqreturn_autocorrelation_ts2_lag2 > 0.142) then class: simulated (proba: 100.0%) | based on 6 samples

if (kurtosis2 > 2.905) and (mean1 <= 0.139) and (return_correlation_ts1_lag_1 > 0.138) then class: simulated (proba: 100.0%) | based on 1 samples





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
