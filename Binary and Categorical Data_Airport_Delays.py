#!/usr/bin/env python
# coding: utf-8

# In[10]:


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


# In[11]:


# get the current working directory
current_working_directory = os.getcwd()


# In[12]:


# print output to the console
print(current_working_directory)


# In[13]:


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/Airports_Delay.xls"
#data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/Population_By_US_States.xlsx"



# In[139]:


# Define variable to load the dataframe
Data_Frame = pd.read_excel(data_file_dir_1,index_col=0, usecols=[1,2])      #https://www.scaler.com/topics/pandas/pandas-read-excel/
Airports=pd.read_excel(data_file_dir_1,index_col=0, usecols=[0])
#print(Data_Frame)
#print(Airports)
Airport_Name=Airports.iloc[0,:].name
#print(Airport_Name)


#print(Data_Frame.cell(row = 1, column = 1).value)

'''
Delays=Data_Frame.to_numpy()
type(Delays)
print(Delays)
'''


# In[140]:


#Plotting Density Plot
ax = Data_Frame.plot.bar(figsize=(4, 4), legend=False)
ax.set_title(Airport_Name+' Airport - Delay Reasons')


# In[ ]:





# In[ ]:




