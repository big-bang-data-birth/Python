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


# In[5]:


kc_tax = pd.read_csv(data_file_dir_4a, compression='gzip', header=0, sep=',', quotechar='"')


# In[6]:


kc_tax0 = kc_tax.loc[(kc_tax.TaxAssessedValue < 750000) &
(kc_tax.SqFtTotLiving > 100) &
(kc_tax.SqFtTotLiving < 3500), :]


# In[7]:


kc_tax0.shape


# In[8]:


ax = kc_tax0.plot.hexbin(x='SqFtTotLiving', y='TaxAssessedValue',
gridsize=30, sharex=False, figsize=(5, 4))
ax.set_xlabel('Finished Square Feet')
ax.set_ylabel('Tax-Assessed Value')


# In[24]:


# Import seaborn
import seaborn as sns
#tips = sns.load_dataset("tips")
#sns.kdeplot(data=tips, x="total_bill")

fig, ax = plt.subplots(figsize=(4, 4))
sns.kdeplot(data=kc_tax0.sample(10000), x='SqFtTotLiving', y='TaxAssessedValue', ax=ax)
ax.set_xlabel('Finished Square Feet')
ax.set_ylabel('Tax Assessed Value')

