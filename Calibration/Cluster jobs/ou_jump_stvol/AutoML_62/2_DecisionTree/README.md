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

5.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.498852 |     nan     |
| auc       | 0.938161 |     nan     |
| f1        | 0.928571 |       0.512 |
| accuracy  | 0.931034 |       0.512 |
| precision | 0.95122  |       0.512 |
| recall    | 1        |       0     |
| mcc       | 0.862892 |       0.512 |


## Confusion matrix (at threshold=0.512)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  42 |                        2 |
| Labeled as simulated |                   4 |                       39 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 > 1.029) and (sqreturn_autocorrelation_ts2_lag1 > -0.019) and (price2_granger_cause_price1 > 0.001) then class: real (proba: 97.6%) | based on 125 samples

if (return_kurtosis1 <= 1.029) and (return_sd1 > 1.355) and (sqreturn_autocorrelation_ts1_lag3 <= 0.132) then class: simulated (proba: 100.0%) | based on 118 samples

if (return_kurtosis1 > 1.029) and (sqreturn_autocorrelation_ts2_lag1 <= -0.019) and (sqreturn_autocorrelation_ts1_lag3 <= 0.027) then class: simulated (proba: 100.0%) | based on 5 samples

if (return_kurtosis1 <= 1.029) and (return_sd1 <= 1.355) and (return_kurtosis2 > -0.101) then class: real (proba: 100.0%) | based on 5 samples

if (return_kurtosis1 > 1.029) and (sqreturn_autocorrelation_ts2_lag1 > -0.019) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 2 samples

if (return_kurtosis1 > 1.029) and (sqreturn_autocorrelation_ts2_lag1 <= -0.019) and (sqreturn_autocorrelation_ts1_lag3 > 0.027) then class: real (proba: 100.0%) | based on 2 samples

if (return_kurtosis1 <= 1.029) and (return_sd1 > 1.355) and (sqreturn_autocorrelation_ts1_lag3 > 0.132) then class: real (proba: 100.0%) | based on 2 samples

if (return_kurtosis1 <= 1.029) and (return_sd1 <= 1.355) and (return_kurtosis2 <= -0.101) then class: simulated (proba: 100.0%) | based on 1 samples





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
