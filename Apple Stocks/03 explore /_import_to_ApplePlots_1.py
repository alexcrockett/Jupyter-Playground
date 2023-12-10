#%%
import numpy as np
import pandas as pd
apples = pd.read_csv('../02 data/AppleStockPrices.csv')

#%%
print(apples)
#%%
'''
Convert to a numpy array
Print the array
'''
#%%
apples_array = apples.to_numpy()
aay = apples_array
#%%
print(aay)
#%%
'''
Means
Total sums
Maximums
Minimums
Counts
Medians
Standard deviation of salaries
Variance of of salaries
'''
#%%
# Calculating means and storing variables for later
mean_Open = apples['Open'].mean() # Mean Open
mean_High = apples['High'].mean() # Mean High
mean_Low = apples['Low'].mean() # Mean Low
mean_Close = apples['Close'].mean() # Mean Close
mean_Volume = apples['Volume'].mean()


# Calculating the mean values and storing them in a dictionary
mean_values = {
    "Mean Open": apples['Open'].mean(), # Mean Open
    "Mean High": apples['High'].mean(), # Mean High
    "Mean Low": apples['Low'].mean(), # Mean Low
    "Mean Close": apples['Close'].mean(), # Mean Close
    "Mean Volume": apples['Volume'].mean() # Mean Volume
}

# Iterating over the dictionary and printing each item
for key, value in mean_values.items():
    print(f"{key}: {value:.2f}")
#%%
# Create an array of values that can be manipulated later

mean_array = x_1 = np.array([mean_Open, mean_High, mean_Low, mean_Close, mean_Volume])

print(x_1)

#%%
# Here we want to convert our array into a column vector
x_1 = mean_array.reshape((-1, 1))
