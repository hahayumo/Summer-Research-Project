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

9.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.72553  |  nan        |
| auc       | 0.57381  |  nan        |
| f1        | 0.651163 |    0.084375 |
| accuracy  | 0.482759 |    0.084375 |
| precision | 0.482759 |    0.084375 |
| recall    | 1        |    0.084375 |
| mcc       | 0        |    0.084375 |


## Confusion matrix (at threshold=0.084375)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                   0 |                       45 |
| Labeled as simulated |                   0 |                       42 |

## Learning curves
![Learning curves](learning_curves.png)

## Decision Tree 

### Tree #1
![Tree 1](learner_fold_0_tree.svg)

### Rules

if (return_kurtosis1 <= -0.135) and (return_autocorrelation_1_lag3 > 0.963) and (return_autocorrelation_2_lag1 <= 0.997) then class: real (proba: 55.71%) | based on 140 samples

if (return_kurtosis1 <= -0.135) and (return_autocorrelation_1_lag3 <= 0.963) and (return_mean2 > 16.515) then class: simulated (proba: 77.27%) | based on 44 samples

if (return_kurtosis1 > -0.135) and (price1_granger_cause_price2 <= 0.905) and (return_sd2 > 1.56) then class: real (proba: 90.62%) | based on 32 samples

if (return_kurtosis1 <= -0.135) and (return_autocorrelation_1_lag3 > 0.963) and (return_autocorrelation_2_lag1 > 0.997) then class: simulated (proba: 76.19%) | based on 21 samples

if (return_kurtosis1 > -0.135) and (price1_granger_cause_price2 <= 0.905) and (return_sd2 <= 1.56) then class: simulated (proba: 55.56%) | based on 9 samples

if (return_kurtosis1 <= -0.135) and (return_autocorrelation_1_lag3 <= 0.963) and (return_mean2 <= 16.515) then class: real (proba: 66.67%) | based on 9 samples

if (return_kurtosis1 > -0.135) and (price1_granger_cause_price2 > 0.905) and (return_autocorrelation_2_lag2 > 0.95) then class: simulated (proba: 100.0%) | based on 4 samples

if (return_kurtosis1 > -0.135) and (price1_granger_cause_price2 > 0.905) and (return_autocorrelation_2_lag2 <= 0.95) then class: real (proba: 100.0%) | based on 1 samples





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
