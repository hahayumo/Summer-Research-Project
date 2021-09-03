# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | accuracy      |       0.505747 |         3.24 |
| **the best** | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | accuracy      |       0.977011 |         8.48 |
|              | [3_Linear](3_Linear/README.md)                               | Linear         | accuracy      |       0.977011 |         7.27 |
|              | [4_Default_Xgboost](4_Default_Xgboost/README.md)             | Xgboost        | accuracy      |       0.977011 |         8.81 |
|              | [5_Default_NeuralNetwork](5_Default_NeuralNetwork/README.md) | Neural Network | accuracy      |       0.965517 |         4.32 |
|              | [6_Default_RandomForest](6_Default_RandomForest/README.md)   | Random Forest  | accuracy      |       0.977011 |        10.69 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | accuracy      |       0.977011 |         0.18 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

