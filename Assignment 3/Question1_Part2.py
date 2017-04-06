
# coding: utf-8

# In[ ]:

#Question 1 Part 2


# In[13]:

#Importing libraries and reading 
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
df=pd.read_csv("Data/vehicle_collisions.csv",sep=",")
#Filtering columns
df1=DataFrame(df, columns=['BOROUGH', 'VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'])


# In[14]:

#Dropping columns in borough with NA value and assigning count value to a new column
df1=df1.dropna(subset=['BOROUGH'])
df1['Count']=df1.apply(lambda x:x.count()-1,axis=1)


# In[15]:

#Aggregating and counting values
df1['ONE VEHICLE INVOLVED']= np.where(df1['Count']== 1, 1,0)
df1['TWO VEHICLE INVOLVED']= np.where(df1['Count']== 2, 1,0)
df1['THREE VEHICLE INVOLVED']= np.where(df1['Count']== 3, 1,0)
df1['MORE VEHICLES INVOLVED']= np.where(df1['Count']== 4, 1,0)
df1=df1.groupby('BOROUGH').sum()


# In[ ]:




# In[16]:

#Getting the required columns
df2=df1[['ONE VEHICLE INVOLVED','TWO VEHICLE INVOLVED','THREE VEHICLE INVOLVED','MORE VEHICLES INVOLVED']]


# In[19]:

df2.reset_index(level=0, inplace=True)


# In[ ]:

#write to csv
df2.to_csv('Output/Question1_Part2.csv',index=F)


# In[10]:




# In[ ]:




# In[ ]:



