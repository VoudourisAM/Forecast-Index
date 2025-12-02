# Forecast-Index
End-to-end ML pipeline for financial forecasting using yfinance data. Features: Percentage Return, EMA. Models: Linear Regression, DecisionTree, XGB. Metrics: MSE, RMSE.

📈 ML Forecasting Project
This project implements a complete Machine Learning pipeline for financial time-series forecasting. It includes:

1. Extract Data

Uses yfinance to download historical market data.

2. Preprocessing
– Data cleaning
– Handling missing values

3. Feature Engineering
Two engineered features are generated:
- Percentage_Return
- Exponential_Moving_Average (EMA)

4. Train–Test Split
– Time-based split appropriate for time-series data

5. Grid Search
– GridSearchCV for hyperparameter optimization
– Model comparison

6. Visualization
– Train vs Test prediction plots
– Model fit visualization
– Missing data visualization
– Checks for overfitting and underfitting

7. ML Forecast
Implementation and comparison of the following models:
- Linear Regression
- DecisionTreeRegressor
- XGBRegressor
Evaluation metrics:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
