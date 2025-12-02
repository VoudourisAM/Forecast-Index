#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import mplcyberpunk as mplcp

import seaborn as sns


# In[2]:


def Plot_Of_Missing_Data(dataframe):

    plt.style.use("cyberpunk") #Background color
    pal_green = sns.color_palette("Dark2", 7)
    colours = ['#34495E', pal_green[0]] 

    fig, (x1) = plt.subplots(figsize=(20,8), tight_layout=True)
    sns.heatmap(dataframe.isnull(), cmap=colours, cbar=False, yticklabels=False, ax=x1)

    plt.tick_params(axis='y', labelrotation=7, labelsize=7, colors='White') #Rotation label x and y
    plt.tick_params(axis='x', labelsize=12, colors='White') #Rotation label x and y
    plt.xlabel('Missing Data of Columns', fontsize=20, color='Gold') #Bottom title
    plt.ylabel('', fontsize=0) #Bottom title

    plt.show()


# In[ ]:




