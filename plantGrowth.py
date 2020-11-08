
import matplotlib.pyplot as plt # Low level plotting
import numpy as np # Array and numerical processing
from scipy import stats

# Import only specific modules from a library
# we'll use this for the t-test function
from scipy.stats import ttest_ind

from statsmodels.stats.multicomp import pairwise_tukeyhsd

import math # Functions beyond the basic maths

import pandas as pd # For DataFrame and handling
import seaborn as sns # High level plotting
import statsmodels.api as sm # Modling, e.g. ANOV

# Import only specific functions from a library
# ols is for ordinary least squares
from statsmodels.formula.api import ols



# Load dataset
plant_growth = pd.read_csv('data/plant_growth.csv')



#%% Examine the data
plant_growth.info()
plant_growth.shape
plant_growth.columns


# Summaries
plant_growth.describe()


# explore first dataset rowa
plant_growth.head()


#%%
# Descriptive statistics
# count group members
plant_growth['group'].value_counts()

# explore first daraset rows
plant_growth.head()

# Get the average
np.mean(plant_growth['weight'])

# Summary statistics
plant_growth.groupby(['group']).describe()

# also
df1 = plant_growth.groupby(['group']).mean()
df2 = plant_growth.groupby(['group']).std()
final_df = pd.concat([df1, df2], axis = 1)


# Produces Pandas Series
plant_growth.groupby('group')['weight'].mean()
# Produces Pandas DataFrame
plant_growth.groupby('group')[['weight']].mean()


# I like it :)
# EAsy and flexible
plant_growth.groupby(['group']).agg({'weight':['mean','std']})



#%%
# Plotting (Data Visualization)

# boxplot:
sns.boxplot(x='group', y='weight', data=plant_growth)
# Just the points:
sns.catplot(x = "group", y = "weight", data = plant_growth)
# Just the mean with their standard deviations:
sns.pointplot(x = "group", y = "weight", data = plant_growth, join = False)
# alternatively:
# sns.catplot(x="group", y = "weight", data = plant_growth, kind = "point")



#%% Inferential Statistics:

# specify the model
#fit a linear model
# specify model
model = ols("weight ~ group", data = plant_growth)
# fit model
results = model.fit()

# explore model results
results.sammary()

# extract coefficients
results.params.Intercept

# t-test
results.params["group[T.trt1]"]
results.params["group[T.trt2]"]


# ANOVA
# compute anova
aov_table = sm.stats.anova_lm(results, type=2)

# explore anova results
aov_table

#%% Attributes

# __ are reserved names from python
# but you can use them like all other attributes!
# pronunce them as "dunder"
# don't define you own variables, etc, using __xx__

# Attributes on a data frame
plant_growth.shape
plant_growth.columns

# A method
plant_growth.info()

# Methods are class functions, i.e. functions specific to a type of object
# Attributes are class parameters, i.e. values specific to a type of object

getattr(plant_growth, 'columns')
plant_growth.columns
dir(plant_growth)
setattr(plant_growth, 'Rick', 'Scavetta')
plant_growth.Rick

getattr(plant_growth, 'shape')
plant_growth.shape
# %%
