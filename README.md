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
<img width="1475" height="590" alt="Screenshot 2025-12-02 161832" src="https://github.com/user-attachments/assets/8b084dfc-969e-4116-9aaf-e358290471f7" />
– Checks for overfitting and underfitting

8. ML Forecast
Implementation and comparison of the following models:
- Linear Regression
- DecisionTreeRegressor
- XGBRegressor
Evaluation metrics:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)

<img width="1477" height="484" alt="Screenshot 2025-12-02 160548" src="https://github.com/user-attachments/assets/68727f84-431a-413b-bac8-ec80c95fe41c" />
<img width="1473" height="483" alt="Screenshot 2025-12-02 160606" src="https://github.com/user-attachments/assets/d164c79d-dff7-4721-b0a3-a8e59515f4d7" />
<img width="1475" height="486" alt="Screenshot 2025-12-02 160621" src="https://github.com/user-attachments/assets/7da6fd34-e3b5-4f63-b410-47b78e3dc74e" />
