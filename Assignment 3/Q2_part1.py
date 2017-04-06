
# coding: utf-8

# In[2]:

import pandas as pd


# In[3]:

df = pd.read_csv("Data/employee_compensation.csv")


# In[9]:

df1 = df.groupby(['Organization Group','Department'], as_index=False)['Total Compensation'].mean()


# In[25]:

df2=df1.sort_values(['Organization Group','Total Compensation'],ascending=[True,False])


# In[26]:

df3= df2.reset_index(level=0,drop=True)


# In[ ]:

print(df3.head(20))


# In[27]:

df3.to_csv('Output\Question2_part1.csv')


# In[ ]:



