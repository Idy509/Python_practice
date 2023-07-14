#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as py


# In[2]:


top3 = pd.read_csv('epa_ca_tx_pa.csv') # read the csv file into a dataframe
top3


# In[3]:


top3.info() #use the dataframe method to know the number of rows,columns, the name of columns the memory use etc


# In[4]:


top3.describe() #summary statistic


# # Exploring my Data

# In[7]:


top3['state_name'].value_counts() #how many rows for each state 


# In[8]:


top3_sorted= top3.sort_values(by= 'aqi', ascending = False) # Sort by aqi largest to smallest
top3_sorted.head(10)


# # Examine California Data
# Regarding our top3_sorted dataframe, California is the state with the most aqi so we decide to go deeper into it

# In[9]:


#creating booleans mask
mask = top3_sorted['state_name'] == 'California'
cf_df = top3_sorted[mask]
cf_df.head(10)


# In[10]:


cf_df.shape #using shape attribute to see if the number of rows in shape match the number of rows in the value_counts in my previous code


# In[12]:


cf_df['county_name'].value_counts() #examine the number of times each county is represented in california data


# In[13]:


mask = cf_df['county_name'] == 'Los Angeles'
cf_df[mask]['aqi'].mean() #calculate the mean aqi for los angeles


# # Groupby
# groupby the original dataframe(top3) by state 

# In[15]:


top3.groupby('state_name').mean()[['aqi']] #mean of aqi by state


# Adding a second file

# In[16]:


other_states = pd.read_csv('epa_others.csv')
other_states.head(10)


# # Concat Data

# In[17]:


combined_df = pd.concat([top3,other_states], axis = 0)
len(combined_df) == len(top3) + len(other_states) # verify if the lengh of top3 + other_states is equal to combined_df


# # Task 7: Complex Boolean masking
# According to the EPA, AQI values of 51-100 are considered of "Moderate" concern. You've been tasked with examining some data for the state of Washington.
# 
# Use Boolean masking to return the rows that represent data from the state of Washington with AQI values of 51+.

# In[18]:


mask=(combined_df['state_name'] == 'Washington') & (combined_df['aqi'] > 50)
combined_df[mask]


# In[ ]:




