#Mini-case study - exercise 4.8

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns
from statsmodels.formula.api import ols
import numpy as np # Array and numerical processing

# Loading dataset
mtcars = pd.read_csv('data/mtcars.csv')
mtcars.head()


#%% Calculate the correlation between mpg and wt and test if it is significant.

# corr() is not a function:
# corr(mtcars['mpg'], mtcars['wt'])

# A correlation matrix
cor_mat = mtcars.corr()
cor_mat[['wt']].iloc[0]

# Targeted correlation between two Series in the DataFrame
mtcars['mpg'].corr(mtcars['wt'])

# Using NumPy
r = np.corrcoef(mtcars['mpg'], mtcars['wt'])
r

# import pingouin as pg 
# pg.corr(x=mtcars['mpg'], y=mtcars['wt'])

# import scipy.stats as stats
stats.pearsonr(mtcars['mpg'], mtcars['wt'])


#%% Visualize the relationship in an XY scatter plot 
# (bonus points for a regression line).

# previously imported seaborn (see above)
# sns.scatter(x=mtcars['mpg'], y=mtcars['wt'])

# import matplotlib.pyplot as plt # Low level plotting
y = mtcars.mpg
x = mtcars.wt
plt.scatter(x,y)
# plt.show()

sns.regplot(x="wt", y="mpg", data = mtcars, ci=None)

sns.lmplot(x="wt", y="mpg", data=mtcars, ci=None)


# from sklearn.linear_model import LinearRegression
# model = LinearRegression().fit(x, y)


#from statsmodels.formula.api import ols
model = ols("mpg ~ wt", data=mtcars)
results = model.fit()
results.summary()


#%%
""" Warnings:
[Standard Errors assume that the covariance matrix of the errors is correctly specified.
For plotting:
Continuous vs continuous (i.e. scatter plot), but also
Continuous vs categorical, or
Categorical vs continuous
Y-Axis
Dependent variable (i.e. dependent on the indpendent variable)
Response (i.e. the outcome)
f(x) (i.e. y as a function of x)
X-Axis
Independent variable (i.e. decided upon by the experimenter)
Predictor (a variable that predicts a specific resonse, i.e. y)"""

#%% Convert wt column from pounds to kg 
# (bouns points for adding it to the DataFrame).

# Avoid making unnecessary new objects that are separate from your DataFrame
#twocol = mtcars[['mpg','wt']]
#twocol['kilo'] = y/2.2046
#twocol

mtcars["wt"]
mtcars["wt"].apply(lambda x: x/2.2046)
mtcars['wt_kg'] = mtcars['wt']/2.2046226218

# Alternatvely:
# mtcars['wt_kg_2'] = mtcars['wt']*0.453592
