#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.model_selection import train_test_split


# In[3]:


def split_data(dataframe):
    X = dataframe.iloc[:, 1:]
    y = dataframe.iloc[:, 0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    return X_train, X_test, y_train, y_test


# In[ ]:




