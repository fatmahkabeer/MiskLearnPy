# Diamonds Dataset Analysis:

import numpy as np # Array and numerical processing
import pandas as pd # For DataFrame and handling
import seaborn as sns # High level plotting

# Import only specific functions from a library
# ols is for ordinary least squares
from statsmodels.formula.api import ols


# load dataset
jems = pd.read_csv("Data/diamonds.csv")
jems


#%% What type of data is contained in each column

# Explore the DataFrame
jems.dtypes 
jems.columns # names
jems.describe()
jems.info()
jems.head()
jems.tail

# Random rows of my dataset
jems.sample(n = 10)

#jems['carat'].dtype



#%% Exercise 7.3 (Counting individual groups)

# How many diamonds with a clarity of category “IF” are present in the data-set?
len(jems[jems.clarity == 'IF'])

#(jems['clarity'] == 'IF').value_counts()[True]
#jems.clarity.value_counts()

#count = jems['clarity'].value_counts()
#countIf = count.get(key = 'IF')

# What fraction of the total do they represent?
#fracOfIf = countIf/sum(count)
len(jems[(jems.clarity == 'IF')]/len(jems))


#%% Exercise 7.4 (Summarizing proportions)
# What proportion of the whole is made up of each category of clarity?

# First get the unique values in the group variable
calarityCat = jems.clarity.unique()
# Then iterate over each group and calculate the mean of the weights
for value in calarityCat:
    prop = len(value)/len(jems)

prop

#%% Exercise 7.5 (Find specific diamonds prices) 
# What is the cheapest diamond price overall? 
min(jems.price)
jems['price'].min()

# What is the range of diamond prices?
# print('Range for prices (', jems['price'].min(), '-', jems['price'].max(), ')')

def getRange(l):
    low = min(l)
    hight = max(l)
    return low, hight

getRange(jems.price)
low, high = getRange(jems.price)

# What is the average diamond price in each category of cut and color?
jems.groupby('cut', 'color')['price'].mean()



#%% Exercise 7.6 (Basic plotting) 
# Make a scatter plot that shows the diamond price described by carat.
sns.catplot(x = 'carat', y = 'price', data = jems)


#%% Exercise 7.7 (Applying transformations)
#  Apply a log10 transformation to both the price and carat and store these as new columns in the DataFrame:
#  price_log10 and carat_log10
caratLog10 = np.log10(jems.carat)
priceLog10 = np.log10(jems.price)


#%% Exercise 7.8 (Basic plotting)
# Redraw the scatterplot using the transformed values
sns.catplot(x = 'caratLog10', y = 'priceLog10', data = jems)


#%% Exercise 7.9 (Viewing models)
# Define a linear model that describes the relatioship shown in the plot
model = ols("priceLog10 ~ caratLog10", jems)

sns.lmplot(x = 'priceLog10', y = 'caratLog10', data = jems,
           line_kws={'color':'r', 'alpha': 0.7, 'lw': 5})
 #plt.title("Linear Model")
 #plt.show()