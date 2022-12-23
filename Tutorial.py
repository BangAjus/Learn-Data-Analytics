# Apply this on Google Colab
from pandas import *
df = read_csv('Students Performance.csv')

# Level 1 data analytics

# About dataframe :

# 1. describe dataframe
# syntax : df.describe()
df.describe() #implementation

# 2. shape of dataframe
# syntax : df.shape()
df.shape() #implementation

# Statistics :
# you can only apply 'statistics' function to value of numbers in dataframe

# 1. max value of columns
# syntax : df['column_name'].max()
df['nilai'].max() #implementation

# 2. min value of columns
# syntax : df['column_name'].min()
df['nilai'].min() #implementation

# 3. mean value of columns
# syntax : df['column_name'].mean()
df['nilai'].mean() #implementation

# 4. sum value of columns
# syntax : df['column_name'].sum()
df['nilai'].sum() #implementation
 
# Data Findings :
# Use this functions to find the data you want

# 1. Find string(categoric) data
# syntax : df[df['column_name'] == 'data'] 
df[df['gender'] == 'male'] #implementation

# 2. Find numeric data
# syntax : df[df['column_name'] == 0]  
df[df['nilai'] == 97] #implementation
