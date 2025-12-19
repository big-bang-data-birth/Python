#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


# get the current working directory
current_working_directory = os.getcwd()


# In[4]:


# print output to the console
print(current_working_directory)


# In[10]:


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/Murder_Rate_By_US_States.xls"
#data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/Population_By_US_States.xlsx"



# In[11]:


# Define variable to load the dataframe
state = pd.read_excel(data_file_dir_1,index_col=0)




# In[12]:


#Plotting Density Plot
ax = state['Murder Rate'].plot.hist(density=True, xlim=[0,12], bins=range(1,12))
state['Murder Rate'].plot.density(ax=ax)
ax.set_xlabel('Murder Rate (per 100,000)')


# In[ ]:





# In[ ]:




