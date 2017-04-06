
# coding: utf-8

# In[2]:

import pandas as pd
import os



# In[51]:

df = pd.read_csv("Data/vehicle_collisions.csv")


# In[4]:

df1 = df[['DATE','BOROUGH']]


# In[5]:



# In[6]:

df1['DATE']=pd.to_datetime(df1['DATE'])


# In[13]:

import calendar
df1['MONTH']=df1['DATE'].dt.month.apply(lambda x: calendar.month_abbr[x])


# In[20]:

df1['YEAR']=df1['DATE'].dt.year




# In[24]:

df1=df1[df1['YEAR']==2016]


# In[46]:

df_total=df1.groupby('MONTH',sort=False).count().reset_index()
df_total1=df_total[['MONTH',"DATE"]]


# In[49]:

df_total1=df_total1.rename(columns={'DATE':'TOTAL_COUNT'})


# In[50]:




# In[19]:

#df1 = df.loc[df['BOROUGH'] == 'MANHATTAN']


# In[52]:

deeff = df1.loc[df1['BOROUGH'] == 'MANHATTAN']


# In[53]:




# In[55]:

deeff_total=deeff.groupby('MONTH',sort=False).count().reset_index()
deeff_total1=deeff_total[['MONTH',"DATE"]]


# In[57]:




# In[60]:

deeff_total1=deeff_total1.rename(columns={'TOTAL_COUNT':'MANHATTAN_COUNT'})




# In[62]:

final_df = df_total1.merge(deeff_total1)


# In[64]:

final_df['PERCENTAGE']=(final_df['MANHATTAN_COUNT']/final_df['TOTAL_COUNT'])*100


# In[65]:

print(final_df.head())


# In[67]:

final_df.to_csv('Output/Question1_Part1.csv',index=False)


# In[ ]:



