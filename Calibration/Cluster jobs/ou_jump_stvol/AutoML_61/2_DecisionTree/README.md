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

12.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.375884 |  nan        |
| auc       | 0.965645 |  nan        |
| f1        | 0.965517 |    0.492063 |
| accuracy  | 0.965517 |    0.492063 |
| precision | 1        |    0.984127 |
| recall    | 0.954545 |    0        |
| mcc       | 0.93129  |    0.492063 |


## Confusion matrix (at threshold=0.492063)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        1 |
| Labeled as simulated |                   2 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= 1.201) and (return_sd1 > 1.256) and (return_sd2 <= 1.757) then class: simulated (proba: 98.41%) | based on 126 samples

if (return_kurtosis1 > 1.201) and (return_mean1 > -0.048) and (price2_granger_cause_price1 > 0.007) then class: real (proba: 100.0%) | based on 103 samples

if (return_kurtosis1 > 1.201) and (return_mean1 > -0.048) and (price2_granger_cause_price1 <= 0.007) then class: real (proba: 75.0%) | based on 12 samples

if (return_kurtosis1 <= 1.201) and (return_sd1 <= 1.256) then class: real (proba: 100.0%) | based on 7 samples

if (return_kurtosis1 > 1.201) and (return_mean1 <= -0.048) and (sqreturn_autocorrelation_ts2_lag1 > 0.057) then class: real (proba: 100.0%) | based on 5 samples

if (return_kurtosis1 > 1.201) and (return_mean1 <= -0.048) and (sqreturn_autocorrelation_ts2_lag1 <= 0.057) then class: simulated (proba: 100.0%) | based on 4 samples

if (return_kurtosis1 <= 1.201) and (return_sd1 > 1.256) and (return_sd2 > 1.757) then class: real (proba: 100.0%) | based on 3 samples





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
