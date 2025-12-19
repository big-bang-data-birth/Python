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


data_file_dir_1 = "G:/My Drive/Learning/Data Science/R Language/Murder_Rate_By_US_States.xls"
#data_file_dir_2 = "G:/My Drive/Learning/Data Science/R Language/Population_By_US_States.xlsx"

# Define variable to load the dataframe
state = pd.read_excel(data_file_dir_1,index_col=0)


#Plotting Density Plot
ax = state['Murder Rate'].plot.hist(density=True, xlim=[0,12], bins=range(1,12))
state['Murder Rate'].plot.density(ax=ax)
ax.set_xlabel('Murder Rate (per 100,000)')

        

