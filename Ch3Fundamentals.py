# Chapter 3: Python Fundamentals


import math #literally from math
import numpy as np 
import pandas as pd 
import seaborn as sns
from scipy import stats

# Lists - Data Container, pt 1
# A builtin type
# 1D
# Defined with []
#heterogenous, i.e. many different data types

heights = [167, 188, 178, 194, 171, 169]

sum(heights)
len(heights)
np.mean(heights)

#%% Exercise 3.3:
lower95 = np.mean(heights) - 1.96 * np.std(heights) /(len(heights)**0.5)
upper95 = np.mean(heights) + 1.96 * np.std(heights) /(len(heights)**0.5)

# np.sqrt(100)
# 100**0.5
# x ** 2 = 100, solve for x
# x = 100**0.5


#%% Exercise 3.4:

cities = ['Munich', 'Paris', 'Amsterdam', 'Madrid', 'Istanbul']
dist = [584, 1054, 653, 2301, 2191]

len(dist)
max(dist)
min(dist)
np.mean(dist)


#%% Exercise 3.5:
# np.histogram(dist)
sns.stripplot(dist)
sns.stripplot(cities, dist)
# sns.distplot(dist)

# First import seaborn to get nice plotting functions
# use the alias sns
# sns.histplot(dist)




#%% A multi line comment: use """......"""
# Use them to also add "docstrings" to a function

def addNumbers(x, y):
    """Add two numbers together"""
    z = x + y
    return z

# Call the function
addNumbers(5,8)

# doc strings can be called as a method:
addNumbers.__doc__

#%% Exercise 3.6:
# Write a function to retuen lower95 for any list
def confInt(x):
    z = np.mean(x) - 1.96 * np.std(x)/np.sqrt(len(x))
    return z


confInt(heights)

# Returning two values - output is a tuple
# like a list, but use () instead of []
# tuples are immutablle - they can't be modified

def mathFun(x, y):
    """Add and subtract two numbers together"""
    result = (x + y, x - y)
    return result
    

myOutput = mathFun(3, 4)
type(myOutput)



# Exercise 3.7 
#Return a tuple of two values (lower and upper limit)
def confInt(x):
    lower95 = np.mean(x) - 1.96 * np.std(x) /(len(x)**0.5)
    upper95 = np.mean(x) + 1.96 * np.std(x) /(len(x)**0.5)

    return(lower95, upper95)


# inner functions 
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

three_shouts('A', 'B', 'C')
# inner('hello') # no access to inner()
    

#%% Exercise 3.8 Inner functions
def confInt(x):
    """calculate the conf int"""

    def error(x):
        return 1.96 * np.std(x)/np.sqrt(len(x))

    lower = np.mean(x) - error(x)
    upper = np.mean(x) + error(x)

    return (lower, upper)


#confInt()



#%% Function generators
# Functions that make new functions
def raiseValue(n):
    """return a function"""

    def inner(x):
        """raise x to the power of n"""
        raised = x ** n 
        return raised

    return inner

raise_2 = raiseValue(2)
raise_2(3)



# For conf ints, using the N dist we have 1.96
# For t-dist, this is dependent on n(sample size)
# e.g. n=10, use 2.26


#%% Exercise 3.9: Function generators 
def setCorrection(c):
    def confInt(x):
        """calculate the conf int"""

        def error(x):
            return c * np.std(x)/np.sqrt(len(x))

        lower = np.mean(x) - error(x)
        upper = np.mean(x) + error(x)
        return (lower, upper)

    return confInt

CI_Norm = setCorrection(1.96)
CI_Norm(heights)

CI_n10 = setCorrection(2.26)
CI_n10(heights)


#%% Setting default values
def confInt(x, correct = 1.96):
    """calculate the conf int"""

    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))
    return (lower, upper)

confInt(heights, 1.96)
confInt(heights)
confInt(heights, 2.26)



#%%
# Determine the correction factor dependent on 
# Sample size on a t-distbutions
# i.e. df (degrees of freedom) = n-1
# First, get the t distribution
# from scipy.stats import t

def confInt(x):
    """calculate the conf int"""

    correct = stats.t.ppf(0.975,  len(x)-1 )
    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))
    return (lower, upper)

confInt(heights)




#%% 3.7.8 lambda functions
def raise_to_power(x, y):
    """exponents"""
    return x ** y

raise_to_power(2, 3)

# anonymous, unnamed, lambda
lambda x, y: x ** y

# e.g. we saw it already in the context of a DataFrame
# the \ breaks up a long command onto the next line
#chick.groupby(['feed'])['weight']. \
#   transform(lambda x: stats.zscore(x, ddof = 1))

# or use the map()
# heights ** 3 # lists are not iterable
cubed = map(lambda x: x ** 3, heights)
# This results in a map object
# Which we can convert to a list 
list(cubed)

# cubed_2 = map(lambda x, y: x ** y, {heights, 3})
# This results in a map object
# Which we can convert to a list 
# list(cubed_2)

# map without lambda
list(map(np.mean, [[1,2,3], [4,5,6]]))

# e.g. filter()
list(filter(lambda x: x > 175, heights))


#%% Exercise 3.14 Returning meaningful messages:
# i.e. a function that returns:
# There is a 95% chance that the true population 
# parameter is covered by the region XX, YY

def confInt(x):
    """calculate the conf int"""

    correct = stats.t.ppf(0.975,  len(x)-1)

    lower = np.mean(x) - correct * np.std(x)/np.sqrt(len(x))
    upper = np.mean(x) + correct * np.std(x)/np.sqrt(len(x))

    print(f"There is a 95% chance that the true population parameter is covered by the region [{round(lower, 2)}, {round(upper, 2)}].")

confInt(heights)


#%% See section 3.8
# use f-string formatting
name = 'Rick'
print(f"Hi my name is {name}")
print(f"{100 * 566} is a big number,\nbut {100 / 566} is not")
print(f"{np.mean([1,2,3])} is the mean of 1,2,3")


#%% Methods:
# access using the . notation

# Methods for numerical list objects
# Available methods for this object:
dir(dist)


# like, but not the same as...
np.mean(heights) # a function in the np module
len(heights) # a function

# len is not a method
# heights.len()
# 'list' object (heights) has no attribute 'len'

# Function takes an object as an argument
# Objects call methods
# Methods are just functions specific to a given class of object



## Exercise 3.15
# try these methods that we haven't explored yet:
# copy()
heights
heights_2 = heights.copy()
heights_2
heights_2.append(455)
heights_2
heights

# clear()
heights_2.clear()
heights_2

# A list of lists
heights.append([45, 74, 23])
heights

# Reset list
heights = [167, 188, 178, 194, 171, 169]
heights

# reverse()
heights.reverse()
heights

# count()
heights.count(194)

# These are methods we already saw,
# but the are NOT methods for lists!
# heights.value_counts()
# heights.mean() # called as a builtin method



#%% index()
heights
heights.index(194)

# Revisit for iterables
range(3)
list(range(3)) # 0,1,2

heights.extend(range(3))
heights
heights.extend([4,6,8])
heights

# insert()
heights.insert(8, 653)
heights

help(round)


#%% Dictionaries
# [] produce lists
# () produce tuples (immutable)
# {} produce dictionaries key:value
# dict(zip([],[])) zip two lists to make a dictionary




#%% Attributes
#l.__len__

#len(l)

#addNumbs.__doc__
#setattr(addNumbs, '__doc__', "hello")
#addNumbs.__doc__


# __ are reserved names from python
# but you can use them like all other attributes!
# pronunce them as "dunder"
# don't define you own variables, etc, using __xx__

# Attributes on a data frame
#plant_growth.shape
#plant_growth.columns

# A method
#plant_growth.info()

# Methods are class functions, i.e. functions specific to a type of object
# Attributes are class parameters, i.e. values specific to a type of object

#getattr(plant_growth, 'columns')
#plant_growth.columns
#dir(plant_growth)
#setattr(plant_growth, 'Rick', 'Scavetta')
#plant_growth.Rick

#getattr(plant_growth, 'shape')
#plant_growth.shape



#%% Dictionaries - Data containers, pt 2
# aka dict

# key/value pairs
# list, use []
# tuples, use ()
# dict, use {}
d = {'int_value': 3,
     'bool_value': False,
     'str_value': 'hello'}

d

# Access values using their key
d['bool_value']

# values can be more than length one
# i.e. they can contain a list
organizations = {'name': ['Volkswagen', 'Daimler', 'Allianz', 'Charite'],
                 'structure': ['company', 'company', 'company', 'research']}
organizations['name']

# Make a dictionary (key/value pair) from lists:
heights = [167, 188, 178, 194, 171, 169]
persons = ["Mary", "John", "Kevin", "Elena", "Doug", "Galin"]

# key is persons, 
# value is corresponding value in heights
heights_persons = dict(zip(persons, heights))
heights_persons


heights_persons.values()
heights_persons.keys()

# in a list use index position:
heights[3]
heights.index(194)
heights_persons['Mary']


#%% NumPy Array - Data containers, pt 3
# np.array([]) produces an ndarray
# n-dimensional (1, 2, ...)
# what we think as a matrix
# They can only have ONE type

xx = [3, 8, 9, 23]
type(xx)

yy = np.array([3, 8, 9, 23])
type(yy)

# A list [] of lists [], [], range()
zz_list = [[5, 7, 8, 9, 3],
           [0, 3, 6, 8, 2],
           range(5)]
zz_list # 1-dimension

zz_array = np.array([[5, 7, 8, 9, 3],
                     [0, 3, 6, 8, 2],
                     range(5)])
zz_array # 2-dimensional

# What is range(5)?
list(range(5))
list(range(3, 5))

# for reference:
import keyword
keyword.kwlist

