#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


df=pd.read_csv("C:\\Users\\arunk\\Downloads\\fifa_data.csv")


# In[17]:


df


# In[19]:


#1.Which country has the most number of players
df['Nationality'].value_counts()


# ### ENGLAND has the most number of players.

# In[41]:


#2.Plot a bar chart of 5 top countries with the most number of players.
TF=df['Nationality'].value_counts().head(5)
plt.bar(TF.index,TF.values)
plt.title('Top 5 Countries with most no of players')
plt.xlabel('Country')
plt.ylabel('No of players')
plt.show()


# ## Countries like england, germany,spain,argentina,france have most no of players.They are the top 5 countries in the world when it comes to football

# In[45]:


#3.Which player has the highest salary?
HS=df.loc[df['Wage'].idxmax()]['Name']
HS


# ## F Marchetti is the player having highest salary

# In[62]:


#4.Plot a histogram to get the salary range of the players.
plt.hist(df['Wage'],color='r') 
plt.title('salary range of players')
plt.xlabel('player')
plt.ylabel('salary')
plt.show()


# ## There is a huge salary difference between avarage players and top players 

# In[72]:


#5.Who is the tallest player in the fifa?
TP=df.sort_values(by=['Height'],ascending=False)
TP[['Name','Height']].head(2)


# ## There are two players with height 6'9(tallest)

# In[70]:


#6.Which club has the most number of players? 
df['Club'].value_counts()


# ## There are 5 clubs with most no of players and they all have 33 players

# In[74]:


#7.Which foot is most preferred by the players?Draw a bar chart for preferred foot
PF=df['Preferred Foot'].value_counts()
PF


# ## Most of the players are right footers

# In[78]:


plt.bar(PF.index,PF.values,color='y')
plt.title('Preferred foot of the players')
plt.xlabel('Foot preference')
plt.ylabel('No of players')
plt.show()


# In[ ]:




