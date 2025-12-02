#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def Drop_Null_Rows(dataframe):
    return dataframe.dropna()


# In[3]:


def Drop_Holidays_Values(dataframe):
    new_dataframe = dataframe.copy()

    try:
        new_dataframe['Days_Of_Weeks'] = new_dataframe.index
        sr = new_dataframe['Days_Of_Weeks']
        sr = pd.to_datetime(sr) 
        result = sr.dt.day_name(locale = 'English') 
        new_dataframe['Days_Of_Weeks'] = result

        drop_holidays_index = []

        for _ in range(len(new_dataframe)):
            #print(_, ' --- ', dataframe.index[_], ' : ', dataframe.iloc[_,-1])
            if new_dataframe.iloc[_,-1] == 'Saturday' or new_dataframe.iloc[_,-1] == 'Sunday':
                #print(_, ' --- ', dataframe.index[_], ' : ', dataframe.iloc[_,-1])
                drop_holidays_index += [new_dataframe.index[_]]

        new_dataframe.drop(index=drop_holidays_index, axis=0, inplace=True)
        new_dataframe.drop(columns=['Days_Of_Weeks'], axis=1, inplace=True)
        return new_dataframe

    except:
        print('No option!\nError')


# In[4]:


def Drop_Missing_Data(dataframe):
    new_dataframe = dataframe.copy()
    for i in new_dataframe.columns:
        if (0.20 * len(new_dataframe)) <= (new_dataframe[i].isnull().sum()):
            new_dataframe.drop(columns=_, axis=1, inplace=True)
    return new_dataframe


# In[5]:


def Forward_Fill_Data(dataframe):
    new_dataframe = dataframe.copy()

    for _ in new_dataframe.columns:
        if new_dataframe.isnull().sum()[_] > 0:
            new_dataframe.ffill(axis ='rows', inplace=True)
    return new_dataframe


# In[6]:


def Drop_Null_Rows(dataframe):
    return dataframe.dropna()


# In[7]:


def Select_Target_Finance(dataframe, column_name, clear):
    try:
        print('Target: ',column_name)
        new_dataframe = dataframe.copy()
        new_dataframe['Date'] = new_dataframe.index
        new_dataframe['Date'] = new_dataframe['Date'].shift(-1)
        new_dataframe.index = new_dataframe['Date']
        new_dataframe.drop(['Date'], axis=1, inplace=True)
        new_dataframe.insert(0, 'Target_'+column_name, new_dataframe[column_name].shift(-1))
        if clear == 1:
            new_dataframe.dropna(axis=0, inplace=True)
        return new_dataframe
    except:
        print('No option!\nError')


# In[ ]:




