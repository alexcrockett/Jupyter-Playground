#!/usr/bin/env python
# coding: utf-8

# # Notes (IQR)
# 
# All we are going to do in this file is compute the inter-quartile-range and create a variable that references out data without these outliers. We're also going to create a third variable that excludes companies along with the IQR.
# 
# For each, we will also compute a measure of skew to see how the data are shaped.
# 
# As a note, the IQR is:
# $\text{IQR} = Q3 - Q1$
# 
# Outliers are considered:
# $Q1 - \text{IQR} \cdot 1.5$ and $Q3 + \text{IQR} \cdot 1.5$ 

# In[2]:


# Importing libraries and variables

import pandas as pd
yfin_csv = pd.read_csv(r'https://raw.githubusercontent.com/alexcrockett/Jupyter-Playground/personal/yfin_dataset/02-data/stock_details_5_years.csv')
from yfin_group_range_py import company_averages, first_quartile, fourth_quartile, companies_in_first_quartile, companies_in_fourth_quartile


# In[3]:


# Defining the IQR

## Define the 3rd Quartile and median
median = company_averages.quantile(0.5)  # The median (50th percentile)
third_quartile = fourth_quartile  # The third quartile (75th percentile)

## Define companies in the third quartile
companies_in_third_quartile = company_averages[(company_averages > median) & (company_averages <= third_quartile)]

# Define the IQR
IQR = third_quartile - first_quartile

print("IQR= ", float(str(IQR)))


# In[4]:


# Finding outliers
outlier_scope = 1.5 * IQR 

## Calculate the lower bound for outliers
outlier_lower_bound = first_quartile - outlier_scope

## Identify outliers below the lower bound
outliers_lower = company_averages[company_averages < outlier_lower_bound]

# -----

## Calculate the upper bound for outliers
outlier_upper_bound = third_quartile + outlier_scope

## Identify outliers below the lower bound
outliers_upper = company_averages[company_averages > outlier_upper_bound]


# In[5]:


# Review the results
print("Median: ", median)
print("--------------------")

print("IQR: ", float(str(IQR)))
print("--------------------")

print("Outliers Scope: ", outlier_scope)
print("--------------------")

print(" ") # Add a little space for reading

print("--------------------")
print("Outliers in the lower bound:")
print(outliers_lower)
print("-------------------")

print("Outliers in the upper bound:")
print(outliers_upper)
print("-------------------")


# In[6]:


# Create a new dataframe without the outliers

## Map companies to outliers
outlier_companies = outliers_upper.index

## Remove the comapnies
yfin_restricted_set = yfin_csv[~yfin_csv['Company'].isin(outlier_companies)]


# # Notes
# `outliers_upper.index` gives you the names of the companies that are outliers.
# 
# `yfin_csv['Company'].isin(outlier_companies)` creates a boolean mask where each row is `True` if the company is in the list of outliers and `False` otherwise.
# 
# The `~` operator negates the boolean mask, so you select all rows where the company is not an outlier.
# 
# `yfin_csv[...]` with this mask removes the rows corresponding to outlier companies.

# In[7]:


# Revaluate the mean and median scores

## Means
mean_open_restricted = yfin_restricted_set['Open'].mean() # mean Open
mean_high_restricted = yfin_restricted_set['High'].mean() # mean High
mean_low_restricted = yfin_restricted_set['Low'].mean() # mean Low
mean_close_restricted = yfin_restricted_set['Close'].mean() # mean Close

## Medians
median_open_restricted = yfin_restricted_set['Open'].mean() # median Open
median_high_restricted = yfin_restricted_set['High'].mean() # median High
median_low_restricted = yfin_restricted_set['Low'].mean() # median Low
median_close_restricted = yfin_restricted_set['Close'].mean() # median Close

## Define a set of values to print
central_tendency_restricted = {
    "mean open": mean_open_restricted,
    "mean high": mean_high_restricted,
    "mean low": mean_low_restricted,
    "mean close": mean_close_restricted,
    "median open": median_open_restricted,
    "median high": median_high_restricted,
    "median low": median_low_restricted,
    "median close": median_close_restricted
}

# Print the results
for key, value in central_tendency_restricted.items():
    print(f"{key}: {value:.2f}")


# # Notes
# 
# We can see that the gap between mean and median scores has radiacally reduced by removing ~35 companies from the set of 500. 
# 
# This gives us the data-sets
# - yfin_csv
# - yfin_restricted_set
# 
# We want one more set, a set without the outliers and without scores that have extreme ranges. We will also want to rename our datasets so they're easier to type. We will call them 
# - set_1
# - set_2
# - set_3

# In[14]:


# Finding range outliers

# Calculate the range (High - Low) for each row
yfin_csv['Range'] = yfin_csv['High'] - yfin_csv['Low']

# Calculate median and quartiles of the range
range_median = yfin_csv['Range'].median()
range_quartile_1 = yfin_csv['Range'].quantile(0.25)
range_quartile_3 = yfin_csv['Range'].quantile(0.75)

# Calculate the Interquartile Range (IQR)
range_IQR = range_quartile_3 - range_quartile_1

# Calculate the bounds for outliers
range_outlier_lower_bound = range_quartile_1 - 1.5 * range_IQR
range_outlier_upper_bound = range_quartile_3 + 1.5 * range_IQR

# Identify outliers
range_outliers_lower = yfin_csv[yfin_csv['Range'] < range_outlier_lower_bound]
range_outliers_upper = yfin_csv[yfin_csv['Range'] > range_outlier_upper_bound]

# Get the company names that are outliers
outlier_companies_lower = range_outliers_lower['Company']
outlier_companies_upper = range_outliers_upper['Company']

# Combine the lists of outlier companies
outlier_companies = pd.concat([outlier_companies_lower, outlier_companies_upper]).unique()

outlier_companies_count = outlier_companies.shape

# Remove these companies from the original DataFrame
yfin_restricted_range = yfin_csv[~yfin_csv['Company'].isin(outlier_companies)]


# In[15]:


# Print the results
print("-------------------")
print(" ")
print("Median Range")
print(range_median)
print("-------------------")
print("Range IQR")
print(range_IQR)
print("-------------------")
print(" ")
print("-------------------")
print("Lower bound outliers")
print(outlier_companies_lower)
print("-------------------")
print("Upper bound outliers")
print(outlier_companies_upper)
print("-------------------")
print(" ")
print("-------------------")
print("outlier companies")
print(outlier_companies)

print("count: ", outlier_companies_count)


# There are 306 companies in this list, which suggests a serious problem with the method. The result seems to indicate that based on the calculations, most of the dataset falls outside the IQR, which indicates either, the method os is not useful in this context.
# 
# One interpretation is that segmenting the company stock market prices and using this method for financial data like this will lead to a large number of false postives due to the thickness of the tails inherent in this kind of data. It is also possible that given that the data stretches from 2018 to 2023, both the Pandemic and the 2020 election will have played a role. These are testable hypotheses and graphical analysis of the data will help determine if more specificity in the procedure, or extending the bounds for outliers will be useful.

# In[ ]:


# Renaming datasets

set_1 = yfin_csv # original data set
set_2 = yfin_restricted_set # data without outliers


# In[ ]:




