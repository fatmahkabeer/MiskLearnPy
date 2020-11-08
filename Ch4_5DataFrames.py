
# pandas DataFrames - Data containers, pt 4

import numpy as np 
import pandas as pd 
import seaborn as sns

#DataFrames with Pandas - Data containers, pt 4
# pd.DataFrame({}) produces a DataFrame from a dictionary
# pd.DataFrame(dict(list(zip([],[])))) 
# produces a DataFrame from a list of names and list of lists


# Get a DataFrame when impoting a file

# Or from a dict:
foo1 = [True, False, False, True, True, False]
foo2 = ["Liver", "Brain", "Testes", "Muscle", "Intestine", "Heart"]
foo3 = [13, 88, 1233, 55, 233, 18]


# We have already imported pandas as pd
# use a dictionary to get a data frame
# Collect list into a dataframe
foo_df = pd.DataFrame({'healthy': foo1, 'tissue': foo2, 'quantity': foo3})
foo_df
type(foo_df)


#%% Exercise 4.1
cities = ['Munich', 'Paris', 'Amsterdam', 'Madrid', 'Istanbul']
dist = [584, 1054, 653, 2301, 2191]

distDictDF = pd.DataFrame({"City": cities, 
                           "Distance": dist})

distDictDF



# Or from a list of keys and values:
list_names = ['healthy', 'tissue', 'quantity']
# A list of lists
list_cols = [foo1, foo2, foo3]
# zip put the key/value pairs together
pd.DataFrame(dict(zip(list_names, list_cols)))


#%% from the lesson
zip_list = list(zip(list_names, list_cols))
zip_list

zip_dict = dict(zip_list)
zip_dict # True dictionary

zip_df = pd.DataFrame(zip_dict)
zip_df

# Access information by:
# Name (here)
# Position (later, indexing)

# columns
foo_df.columns
# rows
foo_df.index


# Working with DataFRames
foo_df['healthy'] # Series
type(foo_df['healthy'])

foo_df[['healthy']] # DataFrame
type(foo_df[['healthy']])

foo_df.healthy # a Series

foo_df[['quantity', 'healthy']] # DataFrame

# each column is a Series
# DataFrames are build upon np.arrays
# i.e. Series can only be ONE type!

foo_df.info()

quantity_list = foo3.copy()
# quantity_list.mean() # no!
np.mean(quantity_list) # yes :)
# quantity_list/100 # no!

quantity_array = np.array(foo3)
quantity_array.mean()
quantity_array/100
quantity_array.astype("str")
# quantity_array.name # no!

quantity_Series = foo_df['quantity']
quantity_Series.mean()
quantity_Series/100
quantity_Series.astype("str")
quantity_Series.name

test_Series = pd.Series(quantity_array)
test_Series.name = "hello"
test_Series


#%% # Add a new column and populate it with the value 
# (which is recycled, i.e. "broadcast" over the length of the Series)
foo_df['new'] = 0
foo_df

# But this doesn't work
foo_df.new2 = 4
foo_df



#%% Indexing
foo_df
foo_df['tissue']

foo_df[['tissue']]

foo_df.tissue

# First row, as a Series
foo_df.iloc[0]

# First row, as a DataFrame
foo_df.iloc[[0]]

foo_df.iloc[[0, 1]]

# Using two dimensions:
# To get all columns, use : after the comma
foo_df.iloc[0,:] # : == everything

# Valid
# foo_df.iloc[0,]

# Indexing begins at 0 and is exclusive
# The first two columns, all rows
foo_df.iloc[:,:2] # 0, 1, and exclude 2

# One column as a Series
foo_df.iloc[:,1]


# One column as a Series
foo_df.iloc[:,1]

# counting from the opposite direction
# -1 is the last row
foo_df.iloc[-1,]
# forward: 0  1  2  3  4  5
# Reverse -6 -5 -4 -3 -2 -1

foo_df.reverse()


#%% Exercise 5.1 
#Using foo_df, retreive:
#The 2nd to 3rd rows

# foo_df.iloc[2:3, :] # only the 3rd row
# foo_df.iloc[[2,3],:] # the 3rd & the 4th row using a list
# foo_df.iloc[2:4] # the 3rd & the 4th row using : notation
# foo_df.iloc[0:2,] # 1st & 2nd rows
# foo_df[-1:2,:] # Computer says "no"
# foo_df.iloc[3:,:] # 4th to the end 

# yes :)
foo_df.iloc[[1, 2]] # 2nd & 3rd rows using a list
# foo_df.iloc[1:3,:] # 2nd & 3rd rows using : notation


# The last 2 rows
foo_df[-2:]

# The last two no matter how long
foo_df.iloc[-2:]
# foo_df.iloc[[-1,-2],:] # specify the order with a list

# Hard coding positions
# foo_df.iloc[ [4, 5],:]
# foo_df.iloc[4:,:]

# A random row in foo_df
# import random
# foo_df.iloc[[random.randrange(0, len(foo_df))]]
foo_df.sample()

# From the 4th to the last row (But without hard-coding,
#  i.e. regardless of how many rows my data frame contains)
# foo_df[3:]
foo_df.iloc[3:,:]



#%% Exercise 5.2
# Using .iloc() with:

# Integers? yes :)
foo_df.iloc[4,]

# Floats? Computer says no
# foo_df[0.1:]

# Strings (Characters)? Computer says "no"
# foo_df.iloc[:,'tissue']
# foo_df.iloc['Brain'] # need to look inside the tissue column
# foo_df.iloc['A'] # No is no 'A' anyways
# foo_df[heart:]   # No object defined

# A heterogenous list? Computer says "no"
# foo_df.iloc[:,[1, 'quantity']]

# A heterogenous list? Computer says "no"
# foo_df.iloc[:,[1, 'quantity']]


#%% Exercise 5.3
# Use indexing to obtain all the odd rows
foo_df.iloc[1::2] # 2nd, 4th, 6th
foo_df.iloc[lambda x: x.index % 2 == 1]
foo_df[foo_df.index % 2 != 0]

# Use indexing to obtain all the even rows
foo_df.iloc[::2] # 1st, 3rd, 5th
foo_df.iloc[lambda x: x.index % 2 == 0]


#%% Logical Expressions
# Relational and logical operators

foo_df[foo_df.quantity >= 233]
foo_df[(foo_df.tissue == "Heart") | (foo_df.quantity >= 233)]


#%% Exercise 5.4
# Only “healthy” samples.
foo_df[foo_df.healthy]

# Only “unhealthy” samples.
foo_df[-foo_df.healthy]
foo_df[~foo_df.healthy]

#%% Exercise 5.5
# Only low quantity samples, those below 100.
foo_df[foo_df.quantity < 100]

#Midrange: Quantity between 100 and 1000
foo_df[(foo_df.quantity > 100) & (foo_df.quantity < 1000)] 


#Tails of the distribution: Quantity below 100 and beyond 1000
foo_df[(foo_df.quantity < 100) & (foo_df.quantity > 1000)] 


#%%Exercise 5.6
#Only “Heart” samples.
foo_df[foo_df.tissue == 'Heart']

#Heart” and “liver” samples
foo_df[(foo_df.tissue == 'Heart') | (foo_df.tissue == 'Liver')]


#Everything except “intestines"#
foo_df[foo_df.tissue != 'Intestine']
