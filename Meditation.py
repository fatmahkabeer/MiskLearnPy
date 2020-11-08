
#%% Import needed library
import numpy as np # Array and numerical processing
import pandas as pd # For DataFrame and handling
import math # Functions beyond the basic maths
from scipy import stats

# Import only specific modules from a library
# we'll use this for the t-test function
from scipy.stats import ttest_ind


#Example on getting tidy data
# To really be tidy:
# 1 obs per row
# 1 variable per column
# Here: 3 variables in the "variable" column: treatment, gene, time
# We need to split them up into three distinct columns!
# medi.unstack()

# this just gets treatments:
# medi_melt['treatment'] = medi_melt['variable'].str.split('_').str.get(0)

#%% Make a DataFrame
medi = pd.read_table("data/Expression.txt")
# medi
medi.columns


# %%
# Add an index column, but it's not necessary
# medi_index = medi.reset_index()
# medi_index


#%%
# If we had the index column:
# medi_melt = pd.melt(medi_index, id_vars='index')

# If we don't have an index column, or ID variables: 
# This is "long" data, but *not* tidy! 
medi_melt = pd.melt(medi)


#%%Exercise 8.3 
# split up the three variables, call the .str attribute to get strings
# (Tidy data) Convert the data set to a tidy format.
# Use melt to get tidy data
# the id variables stay the same before and after melting
# the measure variables will become a key:value pair

medi_melt = pd.melt(medi)
medi_melt

medi_melt['treatment'], medi_melt['gene'], medi_melt['time'] = medi_melt['variable'].str.split('_').str

#%% Exercise 8.4 (Calculate Statistics) 
# Calculate each of the following statistics for each of the unique 24 combinations of gene,
# treatment and time:

#average the mean of the value
valMean = np.mean(medi_melt.value)

medi_melt.groupby('gene')['value'].mean()

#n the number of observations in each group
medi_melt.groupby('gene').count()


#SEM The standard error of the mean
valStd = np.std(medi_melt.value)

medi_melt.groupby('gene')['value'].std()
# CIerror The 95% CI error defined by the t distribution


# (degrees of freedom) = n-1
# First, get the t distribution
# from scipy.stats import t

def confInt(x):
    """calculate the conf int"""

    correct = stats.t.ppf(0.975,  len(x)-1 )

    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))

    return (lower, upper)

#confInt()

#lower95 The upper 95% CI limit
#upper95 The upper 95% CI limit
def CI(x, correct = 1.96):
    """calculate the conf int"""

    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))

    return(lower, upper)

#%%Exercise 8.5 (Export data) Now that you’ve processed your data,
# refer to the following table and save a file on your computer that contains the summary statistics.
summaryStat = medi_melt.describe()
summaryStat.to_csv('MediSummaryStatistics.csv')



# %%
# Drop the variable column
medi_melt.drop('variable', axis=1)

