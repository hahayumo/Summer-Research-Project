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

6.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.20267  |  nan        |
| auc       | 0.783669 |  nan        |
| f1        | 0.795181 |    0.196839 |
| accuracy  | 0.804598 |    0.196839 |
| precision | 0.785714 |    0.196839 |
| recall    | 0.95122  |    0        |
| mcc       | 0.608581 |    0.196839 |


## Confusion matrix (at threshold=0.196839)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  37 |                        9 |
| Labeled as simulated |                   8 |                       33 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (sqreturn_autocorrelation_ts1_lag3 <= 0.087) and (sqreturn_autocorrelation_ts2_lag2 <= 0.116) and (sqreturn_correlation_ts1_lag_2 <= 0.149) then class: real (proba: 93.97%) | based on 116 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.087) and (return_correlation_ts1_lag_0 > 0.384) and (return_mean2 > -0.052) then class: simulated (proba: 98.94%) | based on 94 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.087) and (sqreturn_autocorrelation_ts2_lag2 > 0.116) and (sqreturn_autocorrelation_ts2_lag3 > 0.075) then class: simulated (proba: 88.24%) | based on 17 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.087) and (return_correlation_ts1_lag_0 <= 0.384) and (sqreturn_autocorrelation_ts1_lag3 <= 0.266) then class: real (proba: 100.0%) | based on 12 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.087) and (sqreturn_autocorrelation_ts2_lag2 > 0.116) and (sqreturn_autocorrelation_ts2_lag3 <= 0.075) then class: real (proba: 75.0%) | based on 12 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.087) and (return_correlation_ts1_lag_0 > 0.384) and (return_mean2 <= -0.052) then class: real (proba: 66.67%) | based on 6 samples

if (sqreturn_autocorrelation_ts1_lag3 <= 0.087) and (sqreturn_autocorrelation_ts2_lag2 <= 0.116) and (sqreturn_correlation_ts1_lag_2 > 0.149) then class: simulated (proba: 100.0%) | based on 2 samples

if (sqreturn_autocorrelation_ts1_lag3 > 0.087) and (return_correlation_ts1_lag_0 <= 0.384) and (sqreturn_autocorrelation_ts1_lag3 > 0.266) then class: simulated (proba: 100.0%) | based on 1 samples





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
