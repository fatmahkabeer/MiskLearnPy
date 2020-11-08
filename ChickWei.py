
import matplotlib.pyplot as plt # Low level plotting
import numpy as np # Array and numerical processing
import scipy.stats as stats

# Import only specific modules from a library
# we'll use this for the t-test function

from statsmodels.formula.api import ols

import math # Functions beyond the basic maths

import pandas as pd # For DataFrame and handling
import seaborn as sns # High level plotting
import statsmodels.api as sm # Modling, e.g. ANOV

# Import only specific functions from a library
# ols is for ordinary least squares
from statsmodels.formula.api import ols



chickWei = pd.read_table("data/Chick Weights.txt")


# Calculate the mean and standard deviation for each group
chickWei.groupby(['feed']).agg({'weight':['mean','std']})


# Calculate the number of chicks in each group.
chickWei['feed'].value_counts()

# Calculate a within-group z-score.
stats.zscore(chickWei['weight'])



feedGroup = chickWei.feed.unique()
for value in feedGroup:
    result = stats.zscore(chickWei.weight[chickWei.feed == value])
print(result)


#scipy.stats.zscore(a, axis=0, ddof=0, nan_policy=’propagate’)
#a: an array like object containing data
#axis: the axis along which to calculate the z-scores. Default is 0.
#ddof: degrees of freedom correction in the calculation of the standard 
#...deviation.Default is 0.
#nan_policy: how to handle when input contains nan.
# ...Default is propagate, which returns nan.
# ...‘raise’ throws an error and ‘omit’ performs calculations ignoring nan values.



#Produce a strip chart showing each chick as an individual data point
sns.stripplot(x = 'feed', y = 'weight', data = chickWei)

#Calculate a 1-way ANOVA.
model = ols("weight ~ feed", data = chickWei)
# fit model
results = model.fit()
aov_table = sm.stats.anova_lm(results, type=2)

# explore anova results
aov_table


#Calculate Tukey’s post-hoc test (i.e. p-values for all pair-wise t-tests)
def confInt(x):
    """calculate the conf int"""

    correct = stats.t.ppf(0.975,  len(x)-1 )
    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))
    return (lower, upper)

confInt(chickWei.weight)


