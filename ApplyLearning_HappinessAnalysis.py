
import numpy as np # Array and numerical processing
import pandas as pd # For DataFrame and handling
import seaborn as sns # High level plotting

#In this document, I analyze a dataset that I have collected from Kaggle.
#This dataset illustrates the happiness in the world.
#I mainly focus on my analysis of the year 2019 as well as my country, Saudi Arabia.


#%% Reading Data

happiness_2015 = pd.read_csv("archive/2015.csv")
happiness_2016 = pd.read_csv("archive/2016.csv")
happiness_2017 = pd.read_csv("archive/2017.csv")
happiness_2018 = pd.read_csv("archive/2018.csv")
happiness_2019 = pd.read_csv("archive/2019.csv")

# %%comparisons criterias in 2019:
list(happiness_2019.columns)
   

#%% How many Countries in the evaluating list?
len(happiness_2019)


# %% the top 10 of the happiest countries in 2019?
happiness_2019.head(10)

# %% The top 10 of the saddest countries in 2019:
happiness_2019.tail(10)

# %% lot to explain the relationship between freedom to make life choices with the level of happiness

sns.stripplot(x = happiness_2019['Overall rank'],
              y = happiness_2019['Country or region'],
              #col = happiness_2019['Freedom to make life choices']
             )

# %%average of the Healthy Life Expectancy for the saddest country in 2019:


#happiness_2019['Healthy life expectancy']
#happiness_2019['Overall rank']
for i in happiness_2019['Overall rank'] > 146 :
    avgP = np.mean(happiness_2019['Healthy life expectancy'])

print(avgP)

#%%The average of the Healthy life expectancy for the happiest country in 2019:**
for i in happiness_2019['Overall rank'] < 10 :
    avgH = np.mean(happiness_2019['Healthy life expectancy'])

print(avgH)



# %% Saudi Arabia data:


sa2015 = happiness_2015.loc[happiness_2015['Country'] == "Saudi Arabia"]
sa2016 = happiness_2016.loc[happiness_2016['Country'] == "Saudi Arabia"]
sa2017 = happiness_2017.loc[happiness_2017['Country'] == "Saudi Arabia"]
sa2018 = happiness_2018.loc[happiness_2018["Country or region"] == "Saudi Arabia"]
sa2019 = happiness_2019.loc[happiness_2019["Country or region"] == "Saudi Arabia"]

# %%Saudi Arabia Rank in 2019
sa2019['Overall rank']

# %%
# selecting rows based on condition 
happiness_2019[(happiness_2019['Country or region'] == "Saudi Arabia") |
(happiness_2019['Overall rank'] == 1)]


# %% Happiness Rate over last 5 years


years = ["2015", "2016", "2017", "2018", "2019"]
happinessRate = [sa2015['Happiness Rank'],
                   sa2016['Happiness Rank'],
                   sa2017['Happiness.Rank'],
                   sa2018['Overall rank'],
                   sa2019['Overall rank']]

sns.stripplot(x = years, y = happinessRate)

#%% Relation between Social Support and Ovarall.rank in 2018 and 2019:**

sociVsRank18_19 = { 'sociVsRank18' : [sa2018['Social support'], sa2018['Overall rank']],
                    'sociVsRank19' : [sa2019['Social support'], sa2019['Overall rank']]}


df = pd.DataFrame(sociVsRank18_19, columns = ['sociVsRank18','sociVsRank19'])
df


# %% Saudis' happiness details over the last two years:
#pd.merge(sa2018, sa2019, on='Country or region', how='inner')

sa2018.append(sa2019) 
