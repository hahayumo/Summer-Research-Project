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

7.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.445838 |   nan       |
| auc       | 0.887685 |   nan       |
| f1        | 0.893617 |     0.44403 |
| accuracy  | 0.885057 |     0.44403 |
| precision | 0.823529 |     0.44403 |
| recall    | 1        |     0       |
| mcc       | 0.783887 |     0.44403 |


## Confusion matrix (at threshold=0.44403)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  35 |                        9 |
| Labeled as simulated |                   1 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (kurtosis1 <= 3.002) and (kurtosis2 <= 4.309) and (sd1 > 1.196) then class: simulated (proba: 88.81%) | based on 134 samples

if (kurtosis1 > 3.002) and (price2_granger_cause_price1 > 0.001) and (sqreturn_autocorrelation_ts2_lag2 <= 0.149) then class: real (proba: 100.0%) | based on 69 samples

if (kurtosis1 <= 3.002) and (kurtosis2 > 4.309) and (sqreturn_correlation_ts2_lag_3 > -0.09) then class: real (proba: 100.0%) | based on 20 samples

if (kurtosis1 > 3.002) and (price2_granger_cause_price1 > 0.001) and (sqreturn_autocorrelation_ts2_lag2 > 0.149) then class: real (proba: 82.35%) | based on 17 samples

if (kurtosis1 <= 3.002) and (kurtosis2 <= 4.309) and (sd1 <= 1.196) then class: real (proba: 100.0%) | based on 12 samples

if (kurtosis1 > 3.002) and (price2_granger_cause_price1 <= 0.001) and (price1_granger_cause_price2 <= 0.238) then class: simulated (proba: 100.0%) | based on 6 samples

if (kurtosis1 > 3.002) and (price2_granger_cause_price1 <= 0.001) and (price1_granger_cause_price2 > 0.238) then class: real (proba: 100.0%) | based on 1 samples

if (kurtosis1 <= 3.002) and (kurtosis2 > 4.309) and (sqreturn_correlation_ts2_lag_3 <= -0.09) then class: simulated (proba: 100.0%) | based on 1 samples





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
