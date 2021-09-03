# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model      |   Weight |
|:-----------|---------:|
| 1_Baseline |        1 |
| 3_Linear   |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.33541  |  nan        |
| auc       | 0.997884 |  nan        |
| f1        | 0.989011 |    0.493602 |
| accuracy  | 0.988506 |    0.493602 |
| precision | 1        |    0.701575 |
| recall    | 1        |    0.230195 |
| mcc       | 0.977225 |    0.493602 |


## Confusion matrix (at threshold=0.493602)
|                      |   Predicted as real |   Predicted as simulated |
|:---------------------|--------------------:|-------------------------:|
| Labeled as real      |                  41 |                        1 |
| Labeled as simulated |                   0 |                       45 |

## Learning curves
![Learning curves](learning_curves.png)
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



[<< Go back](../README.md)
