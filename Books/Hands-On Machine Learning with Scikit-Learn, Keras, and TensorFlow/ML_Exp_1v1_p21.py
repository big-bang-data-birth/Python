'''
Book Title: Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow
by Aurélien Géron

Complete Projects: https://github.com/ageron/handson-ml3

Example 1-1 (page #21): Training and running a linear model using Scikit-Learn

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
import sklearn.neighbors

import os

#####################################################################
########################### Functions ###############################
#####################################################################
def prepare_country_stats(oecd_bli, gdp_per_capita):
  #print(oecd_bli['OBS_VALUE'])

  oecd_bli = oecd_bli[oecd_bli['INEQUALITY']=='TOT']
  #print(oecd_bli['OBS_VALUE'])
  
  # reindexing the oecd_bli data frame.
  oecd_bli = oecd_bli.pivot(index='Country',columns='INDICATOR',values='OBS_VALUE')
  #print(oecd_bli)   

  #print(gdp_per_capita.columns)
  gdp_per_capita.rename(columns={'2015':'GDP per capita'},inplace=True)   # inplace=True => No return value
  #print("\n\n",gdp_per_capita.columns)

  #print("\nDisplaying only column names\n")
  #print(gdp_per_capita.columns)
  #print("\n ===========================\n")
  #print(gdp_per_capita.head())

  #print(gdp_per_capita['Country Name'])
  gdp_per_capita.set_index('Country Name',inplace=True)    # inplace=True => No return value
  #print(gdp_per_capita.head())

  
  full_country_stats = pd.merge(left=oecd_bli,right=gdp_per_capita,left_index=True,right_index=True)
  #print(full_country_stats.head())

  full_country_stats.sort_values(by='GDP per capita',inplace=True)
  remove_indices = [0,1,6,8,33,34,35]
  keep_indices = list(set(range(36))-set(remove_indices))
  #print(full_country_stats.head())

  #print(full_country_stats['GDP per capita'])
  
  #print(full_country_stats.head())
  #return full_country_stats[['GDP per capita', 'Life Satisfaction']].iloc[keep_indices]
  return full_country_stats[['GDP per capita', 'SW_LIFS']].iloc[keep_indices]

#####################################################################


# Few lines to connect with Google Drive
# from google.colab import drive

casted_key=""

file1_path="./Data/oecd_bli_2015.csv"
file2_path="./Data/gdp_per_capita.csv"
#file_test_path="./Data/sample.csv"

# Code to find the current working directory in google drive.
#drive.mount('/content/drive')
#current_working_directory = os.getcwd()
#print(current_working_directory)

pd.set_option('display.max_rows', None)    #To display all columns
pd.set_option('display.max_columns', None)    #To display all columns

# Load the data
oecd_bli = pd.read_csv(file1_path, thousands=',')
#oecd_bli.describe()    # Display data summary
#print(oecd_bli.head())         # Display data

#gdp_per_capita = pd.read_csv(file2_path,thousands=',',delimiter='\t', encoding='latin1', na_values="n/a")
gdp_per_capita = pd.read_csv(file2_path)
#test = pd.read_csv(file_test_path)
#print(gdp_per_capita.head())
#print(gdp_per_capita['Country Name'])

#gdp_per_capita.describe()  # Display data summary
#print(gdp_per_capita.head())         # Display data

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)

X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["SW_LIFS"]]

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita", y='SW_LIFS')
plt.show()

# Select a linear model
#model = sklearn.linear_model.LinearRegression()
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[22587]] # Cyprus's GDP per capita
print(model.predict(X_new)) # outputs [[ 5.96242338]]

