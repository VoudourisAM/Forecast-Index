#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pandas_ta as pta
import numpy as np


# In[6]:


def Percentage_Return(column_name, dataframe):      
    try:
        dataframe['Percentage_' + column_name] = dataframe[column_name].pct_change() * 100
        return dataframe 
    except:
        print('No option!\nError')


# In[7]:


def Exponential_Moving_Average(column_name, ema_number, dataframe):
    try:
        if 5 <= ema_number <= 20:
            dataframe.loc[:, column_name + '_SEMA_' + str(ema_number)] = dataframe[column_name].rolling(window=ema_number).mean()
        elif 21 <= ema_number <= 50:
            dataframe.loc[:, column_name + '_MEMA_' + str(ema_number)] = dataframe[column_name].rolling(window=ema_number).mean()
        elif 100 <= ema_number <= 200:
            dataframe.loc[:, column_name + '_LEMA_' + str(ema_number)] = dataframe[column_name].rolling(window=ema_number).mean()
        return dataframe
    except:
        print('No option!\nError')


# In[ ]:




