
# coding: utf-8

# In[2]:

import pandas as pd


# In[3]:

df = pd.read_csv("Data/cricket_matches.csv")


# In[4]:




# In[5]:

df1 = df[df['home']==df['winner']]


# In[6]:




# In[11]:

df1['score'] = df1[['innings1_runs','innings2_runs']].max(axis=1)


# In[12]:




# In[15]:

df_final=df1.groupby('winner')['score'].mean()


# In[26]:

df_final1 = df_final.to_frame().reset_index()
df_final1['score']= round(df_final1['score'],2)


# In[25]:

df_final1.to_csv('Output/Q3.csv',index= False)

