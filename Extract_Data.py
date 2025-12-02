#!/usr/bin/env python
# coding: utf-8

# ---
# ### Libraries
# ---

# In[1]:


import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


# ---
# ###  Extracting Index Data Using yfinance
# ---

# In[1]:


def Extract_Index_Data():
    tickers = {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Euro Stoxx 50": "^STOXX50E"
    }

    end_date = datetime.now() + timedelta(days=1)
    start_date = end_date - timedelta(days=366)

    dataframe = pd.DataFrame()

    for name, ticker in tickers.items():
        print(f"Downloading {name} ...")
        df = yf.download(ticker, start=start_date, end=end_date)

        df.columns = df.columns.get_level_values(0)
        df.columns.name = None
        df.index = df.index.strftime('%Y-%m-%d')

        df.columns = [f"{name}_{col}" for col in df.columns]

        if df.empty:
            print(f"⚠️ No data for {name}")
            continue
        else:
            dataframe = dataframe.join(df, how="outer")
    return dataframe


# In[ ]:




