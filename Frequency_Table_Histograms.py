###########################################
#Reference: https://math.stackexchange.com/questions/1665823/how-to-manually-create-a-z-table
###########################################

from scipy.integrate import quad

import scipy.stats as stats

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
#pip install xlrd
import openpyxl
import os
import re			# For String Comparison Operations
  

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/data_table_1_2.xlsx"
#data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/Population_By_US_States.xlsx"

# Define variable to load the dataframe
state = pd.read_excel(data_file_dir_1,index_col=0)

state['Population'].mean()
States_Population_Mean=stats.trim_mean(state['Population'], 0.1)
States_Population_Median=state['Population'].median()

# plt.hist(state)	# Error: Failed to convert value(s) to axis units: array(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE'], dtype=object)

binned_Population = pd.cut(state['Population'], 10)
binned_Population.value_counts()

#Plotting Histogram
ax = (state['Population'] / 1_000_000).plot.hist(figsize=(4, 4))
ax.set_xlabel('Population (millions)')


'''
dataframe1 = openpyxl.load_workbook(data_file_dir_1)			# Ref: https://www.geeksforgeeks.org/reading-excel-file-using-python/
# Define variable to read sheet
dataframe_variable1 = dataframe1.active

# Iterate the loop to read the cell values
loop_Break=False
for row in range(0, dataframe_variable1.max_row):
    if(loop_Break):
        break
    else:
        for col in dataframe_variable1.iter_cols(1, dataframe_variable1.max_column):
          print(col[row].value)
          if(col[row].value==None):
            print("Exiting For Loops")
            loop_Break=True
            break
'''
        

