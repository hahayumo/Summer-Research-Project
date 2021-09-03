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

7.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.701244 |  nan        |
| auc       | 0.861786 |  nan        |
| f1        | 0.853933 |    0.464233 |
| accuracy  | 0.850575 |    0.464233 |
| precision | 0.844444 |    0.464233 |
| recall    | 1        |    0        |
| mcc       | 0.701216 |    0.464233 |


## Confusion matrix (at threshold=0.464233)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  36 |                        7 |
| Labeled as simulated |                   6 |                       38 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 2.935) and (sqreturn_autocorrelation_ts2_lag2 > 0.06) and (sd1 > 1.205) then class: simulated (proba: 91.6%) | based on 119 samples

if (kurtosis1 > 2.935) and (sqreturn_autocorrelation_ts2_lag3 <= 0.221) and (return_correlation_ts1_lag_1 <= 0.134) then class: real (proba: 98.75%) | based on 80 samples

if (kurtosis1 <= 2.935) and (sqreturn_autocorrelation_ts2_lag2 <= 0.06) and (sqreturn_autocorrelation_ts2_lag3 <= 0.131) then class: real (proba: 83.78%) | based on 37 samples

if (kurtosis1 > 2.935) and (sqreturn_autocorrelation_ts2_lag3 > 0.221) and (mean2 > 0.074) then class: simulated (proba: 100.0%) | based on 7 samples

if (kurtosis1 <= 2.935) and (sqreturn_autocorrelation_ts2_lag2 > 0.06) and (sd1 <= 1.205) then class: real (proba: 100.0%) | based on 6 samples

if (kurtosis1 <= 2.935) and (sqreturn_autocorrelation_ts2_lag2 <= 0.06) and (sqreturn_autocorrelation_ts2_lag3 > 0.131) then class: simulated (proba: 100.0%) | based on 6 samples

if (kurtosis1 > 2.935) and (sqreturn_autocorrelation_ts2_lag3 > 0.221) and (mean2 <= 0.074) then class: real (proba: 100.0%) | based on 4 samples

if (kurtosis1 > 2.935) and (sqreturn_autocorrelation_ts2_lag3 <= 0.221) and (return_correlation_ts1_lag_1 > 0.134) then class: simulated (proba: 100.0%) | based on 1 samples





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
