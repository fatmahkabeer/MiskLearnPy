
# Chapter 6: Data Visualization

import numpy as np # Array and numerical processing
import pandas as pd # For DataFrame and handling
import seaborn as sns # High level plotting
import matplotlib.pyplot as plt


mtcars = pd.read_csv('data/mtcars.csv')
print(mtcars.info())

# A basic scatter plot follows the form:
plt.scatter(mtcars["wt"], mtcars["mpg"], alpha=0.65)
plt.title('A basic scatter plot')
plt.xlabel('weight')
plt.ylabel('miles per gallon')





#%%We can also assign the output of plt.subplots to:
#fig, a container that holds everything you see on the past, and
#ax, the part of the page that holds the data, i.e. the canvas.
# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots(1, 3, sharex=True, sharey=True)
print(ax.shape)
# Make plot

for key, value in enumerate(mtcars["cyl"].unique()):
    ax[key].scatter(mtcars["wt"][mtcars["cyl"] == value],
    mtcars["mpg"][mtcars["cyl"] == value], alpha=0.65)

# Call the show function
plt.show()



# %% # Bar chart demo with pairs of bars grouped for easy comparison.

n_groups = 5

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=std_men,
                 error_kw=error_config,
                 label='Men')

rects2 = plt.bar(index + bar_width, means_women, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=std_women,
                 error_kw=error_config,
                 label='Women')

plt.xlabel('Group')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D', 'E'))




# %% Scatter plots
sns.scatterplot(x="wt", y="mpg", data = mtcars)

# Alternatively, using pandas Series:
# sns.scatterplot(mtcars["wt"], mtcars["mpg"])

#Add color
sns.scatterplot(x="wt", y="mpg", hue="cyl", data = mtcars)



# %%
