'''
# Reference: https://www.geeksforgeeks.org/reading-excel-file-using-python/
'''
import pandas as pd
import numpy as np
import openpyxl
import wquantiles
import statistics

from scipy import stats 	# for numerous stats functions

'''
#Method #1
'''
x=[1,2,3]
data_mean=np.mean(x)

# read by default 1st sheet of an excel file
data_file_dir="G:/My Drive/Learning/Data Science/R Language/data_table_1_2.xlsx"
data_frame = pd.read_excel(data_file_dir, sheet_name='Sheet1')

print(data_frame)

data_population_mean=data_frame["Population"].mean()
data_population_trim_mean=stats.trim_mean(data_frame["Population"], 0.2)
data_population_median=data_frame["Population"].median()
data_weights=[1,1,1,1,1,1,1,1]
data_population_weighted_mean=stats.hmean(data_frame["Population"], weights=data_weights)

'''
#Method #2
# Iterate the loop to read the cell values
#for row in range(0, dataframe1.max_row):
for row in range(0, 10):
#    for col in dataframe1.iter_cols(1, dataframe1.max_column):
    for col in dataframe1.iter_cols(1, 4):
        print(col[row].value)
'''

# Method #3
# Weighted Mean using Numpy package
np_data_population_weighted_mean=np.average(data_frame["Population"], weights=data_weights)
np_data_population_median=wquantiles.median(data_frame["Population"], weights=data_weights)

#Finding SD, MAD(ian) and IQR
df1=pd.DataFrame(data_frame["Population"])
Population_mean=statistics.mean(df1["Population"])
Population_SD=statistics.stdev(df1["Population"])
Population_median=statistics.median(df1["Population"])
Population_variance=statistics.variance(df1["Population"])
Population_Q1=np.percentile(data_frame["Population"],25)
Population_Q3=np.percentile(data_frame["Population"],75)
Population_IQR=Population_Q3-Population_Q1

#Finding SD, MAD(ian) and IQR for Murder Rate
df3=pd.DataFrame(data_frame["Murder Rate"])
Murder_Rate_SD=statistics.stdev(df3["Murder Rate"])
Murder_Rate_median=statistics.median(df3["Murder Rate"])
Murder_Rate_variance=statistics.variance(df3["Murder Rate"])

