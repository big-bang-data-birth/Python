#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


# get the current working directory
current_working_directory = os.getcwd()


# In[3]:


# print output to the console
print(current_working_directory)


# In[4]:


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/Airports_Delay.xls"
#data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/Population_By_US_States.xlsx"
data_file_dir_3a = "G:/My Drive/Learning/Data Science/R Language/sp500_data.csv.gz"
data_file_dir_3b = "G:/My Drive/Learning/Data Science/R Language/sp500_sectors.csv"
data_file_dir_4a = "G:/My Drive/Learning/Data Science/R Language/kc_tax.csv.gz"
data_file_dir_5a = "G:/My Drive/Learning/Data Science/R Language/lc_loans.csv"


# In[15]:


lc_loans = pd.read_csv(data_file_dir_5a, header=0, sep=',', quotechar='"')

crosstab = lc_loans.pivot_table(index='grade', columns='status',aggfunc=lambda x: len(x), margins=True)



# In[40]:


df = crosstab.copy().loc['A':'G',:]


# In[41]:


df


# In[42]:


df1=df.loc[:,'Charged Off':'Late'].div(df['All'], axis=0)

df1


# In[38]:


df['All']=df['All']/sum(df['All'])


# In[39]:


perc_crosstab = df
print(perc_crosstab)

