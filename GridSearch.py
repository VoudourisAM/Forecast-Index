#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV


# In[2]:


def DecisionTree_GridSearch(X_train, y_train):

    param_grid = {
        "max_depth": [3, 5, 7, 9, None],
        "min_samples_split": [2, 5, 10, 20],
        "min_samples_leaf": [1, 2, 4, 8, 10],
        "criterion": ["squared_error", "friedman_mse"]
    }

    model = DecisionTreeRegressor(random_state=42)

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="neg_mean_squared_error",  # καλύτερο για regression
        cv=5,
        n_jobs=-1,
        verbose=1
    )

    grid.fit(X_train, y_train)

    print("🟢 Best parameters:", grid.best_params_)
    #print("🟢 Best score (MSE):", abs(grid.best_score_))


# In[3]:


def XGB_GridSearch(X_train, y_train):

    param_grid = {
        "n_estimators": [200, 300, 500],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [3, 5, 7],
        "subsample": [0.7, 0.9, 1.0],
        "colsample_bytree": [0.7, 0.9, 1.0],
        "gamma": [0, 1, 5]
    }

    model = XGBRegressor(
        objective="reg:squarederror",
        random_state=42,
        tree_method="hist"
    )

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring="neg_mean_squared_error",
        cv=5,
        n_jobs=-1,
        verbose=1
    )

    grid.fit(X_train, y_train)

    print("🟢 Best parameters:", grid.best_params_)
    #print("🟢 Best score (MSE):", abs(grid.best_score_))


# In[ ]:




