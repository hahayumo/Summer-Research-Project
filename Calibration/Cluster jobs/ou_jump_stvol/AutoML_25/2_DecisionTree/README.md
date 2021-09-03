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

5.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.912403 |  nan        |
| auc       | 0.84963  |  nan        |
| f1        | 0.891566 |    0.433865 |
| accuracy  | 0.896552 |    0.433865 |
| precision | 0.925    |    0.433865 |
| recall    | 0.906977 |    0        |
| mcc       | 0.794808 |    0.433865 |


## Confusion matrix (at threshold=0.433865)
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

if (return_kurtosis1 > 1.192) and (sqreturn_autocorrelation_ts2_lag1 > 0.011) and (sqreturn_autocorrelation_ts1_lag1 > -0.033) then class: real (proba: 96.15%) | based on 104 samples

if (return_kurtosis1 <= 1.192) and (sqreturn_autocorrelation_ts1_lag2 <= 0.066) and (sqreturn_autocorrelation_ts2_lag2 <= 0.109) then class: simulated (proba: 98.81%) | based on 84 samples

if (return_kurtosis1 > 1.192) and (sqreturn_autocorrelation_ts2_lag1 <= 0.011) and (return_correlation_ts1_lag_0 > 0.296) then class: simulated (proba: 82.93%) | based on 41 samples

if (return_kurtosis1 > 1.192) and (sqreturn_autocorrelation_ts2_lag1 <= 0.011) and (return_correlation_ts1_lag_0 <= 0.296) then class: real (proba: 100.0%) | based on 13 samples

if (return_kurtosis1 <= 1.192) and (sqreturn_autocorrelation_ts1_lag2 > 0.066) and (sqreturn_autocorrelation_ts2_lag1 > -0.013) then class: real (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 > 1.192) and (sqreturn_autocorrelation_ts2_lag1 > 0.011) and (sqreturn_autocorrelation_ts1_lag1 <= -0.033) then class: simulated (proba: 100.0%) | based on 4 samples

if (return_kurtosis1 <= 1.192) and (sqreturn_autocorrelation_ts1_lag2 > 0.066) and (sqreturn_autocorrelation_ts2_lag1 <= -0.013) then class: simulated (proba: 100.0%) | based on 3 samples

if (return_kurtosis1 <= 1.192) and (sqreturn_autocorrelation_ts1_lag2 <= 0.066) and (sqreturn_autocorrelation_ts2_lag2 > 0.109) then class: real (proba: 100.0%) | based on 3 samples





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
