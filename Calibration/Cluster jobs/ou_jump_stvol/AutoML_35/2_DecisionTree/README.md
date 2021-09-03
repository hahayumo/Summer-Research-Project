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

17.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.221665 |  nan        |
| auc       | 0.94556  |  nan        |
| f1        | 0.942529 |    0.478927 |
| accuracy  | 0.942529 |    0.478927 |
| precision | 1        |    0.96875  |
| recall    | 1        |    0        |
| mcc       | 0.885307 |    0.478927 |


## Confusion matrix (at threshold=0.478927)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        2 |
| Labeled as simulated |                   3 |                       41 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 > 1.52) and (sqreturn_autocorrelation_ts2_lag1 > -0.005) and (price2_granger_cause_price1 > 0.001) then class: real (proba: 93.1%) | based on 116 samples

if (return_kurtosis1 <= 1.52) and (return_sd1 > 1.41) and (return_sd1 <= 1.829) then class: simulated (proba: 96.88%) | based on 96 samples

if (return_kurtosis1 > 1.52) and (sqreturn_autocorrelation_ts2_lag1 <= -0.005) and (return_sd2 > 1.732) then class: simulated (proba: 88.89%) | based on 27 samples

if (return_kurtosis1 <= 1.52) and (return_sd1 <= 1.41) then class: real (proba: 100.0%) | based on 8 samples

if (return_kurtosis1 > 1.52) and (sqreturn_autocorrelation_ts2_lag1 > -0.005) and (price2_granger_cause_price1 <= 0.001) then class: simulated (proba: 100.0%) | based on 5 samples

if (return_kurtosis1 > 1.52) and (sqreturn_autocorrelation_ts2_lag1 <= -0.005) and (return_sd2 <= 1.732) then class: real (proba: 100.0%) | based on 4 samples

if (return_kurtosis1 <= 1.52) and (return_sd1 > 1.41) and (return_sd1 > 1.829) then class: real (proba: 100.0%) | based on 4 samples





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
