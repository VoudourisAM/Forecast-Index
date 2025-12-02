#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import mplcyberpunk as mplcp
from sklearn.metrics import mean_squared_error
import math


# In[11]:


def ML_model(X_train, y_train, X_test, y_test, model_, title_model):
    index = X_train.index.copy()
    index = pd.to_datetime(index) #y_test index

    forecast_index = X_test.index.copy()
    forecast_index = pd.to_datetime(forecast_index) #y_test index

    model = model_
    model.fit(X_train, y_train)

    x_pred = model.predict(X_train)
    y_pred = model.predict(X_test)

    plt.style.use("cyberpunk") #Background color
    pal_red = sns.color_palette("flare") #Color
    pal_blue = sns.color_palette("Blues") #Color

    fig, ax1 = plt.subplots(figsize=(15,5), tight_layout=True)

    ax1.plot(index, y_train, linewidth=1.5, color=pal_red[0])
    ax1.plot(index, x_pred, ls='--', linewidth=1, color=pal_blue[1])

    ax1.vlines(index[-1], ymin=min(y_train), ymax=max(y_test), linewidth=0.5, color='white')
    ax1.text(forecast_index[3], (min(y_train) + max(y_train)) / 2, "80% - Train\n20% - Test", color='white', fontsize=12, ha='left', va='bottom')

    ax1.plot(forecast_index, y_test, linewidth=1.5, color=pal_red[3])
    ax1.plot(forecast_index, y_pred, ls='--', color=pal_blue[3])

    plt.title(title_model+'\n'+y_train.name, fontsize=15, color='gold', fontweight='bold')
    ax1.legend(['Actual Price','Model Train'], loc="upper left", fontsize=15)
    plt.ylabel('Forecast Train\nForecast Test', fontsize=20, color='Gold')
    ax1.tick_params(axis='x', labelrotation=30, labelsize=15, width=10, length=3,  direction="in", colors='White')
    ax1.tick_params(axis='y', labelrotation=30, labelsize=15, colors='White')
    ax1.grid(zorder=1, alpha=0.2, linestyle='--', linewidth=0.5, color='darkgrey')

    mplcp.make_lines_glow()

    ax1.spines['left'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['right'].set_color('gold')
    ax1.spines['right'].set_linewidth(0.7)
    ax1.spines['top'].set_color('gold')
    ax1.spines['top'].set_linewidth(0.7)
    plt.show()

    fig, ax2 = plt.subplots(figsize=(15,5), tight_layout=True)
    ax2.plot(forecast_index, y_test,  label='Actual', color=pal_red[3])
    ax2.plot(forecast_index, y_pred, ls='--', label='Forecast', color=pal_blue[3])

    plt.ylabel('Forecast Test', fontsize=20, color='Gold')
    plt.legend(['Actual','Forecast'], loc="upper left", fontsize=15)
    plt.tick_params(axis='x', labelrotation=30, labelsize=15, width=10, length=3,  direction="in", colors='White')
    plt.tick_params(axis='y', labelrotation=30, labelsize=15, colors='White')
    plt.grid(zorder=1, alpha=0.2, linestyle='--', linewidth=0.5, color='darkgrey')

    mplcp.make_lines_glow()

    ax2.spines['top'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_color('gold')
    ax2.spines['left'].set_linewidth(0.7)
    ax2.spines['right'].set_color('gold')
    ax2.spines['right'].set_linewidth(0.7)
    plt.show()


    Train_MSE = mean_squared_error(y_train, x_pred)
    Train_RMSE = math.sqrt(Train_MSE)
    Train_RMSE = round(Train_RMSE,5)

    Test_MSE = mean_squared_error(y_test, y_pred)
    Test_RMSE = math.sqrt(Test_MSE)
    Test_RMSE = round(Test_RMSE,5)

    Metric_data = pd.DataFrame(data={'Train' : [Train_RMSE],
                                     'Test' : [Test_RMSE]})

    fig, ax3 = plt.subplots(figsize=(15,5), tight_layout=True)
    bar1 = ax3.bar(Metric_data.columns[0], Metric_data['Train'], width=0.3, linewidth=3, alpha=0.8, bottom=0, edgecolor=pal_blue[3], color=pal_blue[4])
    bar2 = ax3.bar(Metric_data.columns[1], Metric_data['Test'], width=0.3, linewidth=3, alpha=0.8, bottom=0, edgecolor=pal_red[2], color=pal_red[3])

    plt.ylabel('Root Mean Square Error', fontsize=20, color='Gold') #Bottom title
    ax3.tick_params(axis='x', width=7, length=12, labelrotation=30, labelsize=15, bottom=True, direction="in", colors='White')
    ax3.tick_params(axis='y', labelsize=0) #White
    ax3.tick_params(axis='x', width=7, length=12, labelrotation=30, labelsize=15, bottom=True, direction="in", left=False, colors='White')
    ax3.grid(axis='y', zorder=1, alpha=0.2, linestyle='--', linewidth=0.5, color='darkgrey')

    ax3.text(x=Metric_data.Train.name, y=Metric_data.Train.sum()/2, s=Metric_data.Train[0], color='White', weight='extra bold', ha='center', fontsize=15)
    ax3.text(x=Metric_data.Test.name, y=Metric_data.Test.sum()/2, s=Metric_data.Test[0], color='White', weight='extra bold', ha='center', fontsize=15)

    mplcp.add_bar_gradient(bars=bar1)
    mplcp.add_bar_gradient(bars=bar2)

    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['left'].set_color('gold')
    ax3.spines['left'].set_linewidth(0.7)
    ax3.spines['bottom'].set_color('gold')
    ax3.spines['bottom'].set_linewidth(0.7)


# In[ ]:




