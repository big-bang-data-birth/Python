#!/usr/bin/env python
# coding: utf-8

# In[6]:


from scipy.integrate import quad

import scipy.stats as stats

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
#pip install xlrd
import openpyxl
import os
import re	


# In[7]:


# get the current working directory
current_working_directory = os.getcwd()


# In[8]:


# print output to the console
print(current_working_directory)


# In[14]:


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/Airports_Delay.xls"
data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/airline_stats.csv"
data_file_dir_5 = "G:/My Drive/Learning/Data Science/R Language/loans_income.csv"
data_file_dir_6 = "G:/My Drive/Learning/Data Science/R Language/sp500_data.csv.gz"


# In[17]:


# Define variable to load the dataframe
#https://www.scaler.com/topics/pandas/pandas-read-excel/

#loans_income = pd.read_csv(LOANS_INCOME_CSV).squeeze('columns')

loans_income=pd.read_csv(data_file_dir_5).squeeze('columns')
sample_data = pd.DataFrame({
'income': loans_income.sample(1000),
'type': 'Data',
})


# In[19]:


sample_mean_05 = pd.DataFrame({
'income': [loans_income.sample(5).mean() for _ in range(1000)],
'type': 'Mean of 5',
})



# In[20]:


sample_mean_20 = pd.DataFrame({
'income': [loans_income.sample(20).mean() for _ in range(1000)],
'type': 'Mean of 20',
})


# In[21]:


results = pd.concat([sample_data, sample_mean_05, sample_mean_20])
g = sns.FacetGrid(results, col='type', col_wrap=1, height=2, aspect=2)
g.map(plt.hist, 'income', range=[0, 200000], bins=40)

