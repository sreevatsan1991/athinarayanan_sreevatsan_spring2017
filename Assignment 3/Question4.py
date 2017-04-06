
# coding: utf-8

# In[ ]:

#Question 4 - Movies data


# In[61]:

#Importing libraries and reading csv
import pandas as pd
import numpy as np
import re
df=pd.read_csv('Data/movies_awards.csv',sep=',')[['Title','Awards']]


# In[62]:



#Getting the number of awards and nominations using regex patterns


df['Wins'] = df['Awards'].str.extract('(\d+) w', expand=True).fillna(0)
df['Nominations']  = df['Awards'].str.extract('(\d+) n', expand=True).fillna(0)
df['Bafta_Nominations']  = df['Awards'].str.extract('Nominated for (\d+) BAFT', expand=True).fillna(0)
df['Oscar_Nominations']  = df['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True).fillna(0)
df['Prime_Nominations'] = df['Awards'].str.extract('Nominated for (\d+) Prime', expand=True).fillna(0)
df['Golden_Globe_Nominations'] = df['Awards'].str.extract('Nominated for (\d+) Golden', expand=True).fillna(0)
df['Bafta_Wins']  = df['Awards'].str.extract('Won (\d+) BAFTA', expand=True).fillna(0)
df['Oscar_Wins']  = df['Awards'].str.extract('Won (\d+) Oscar[s]?', expand=True).fillna(0)
df['Prime_Wins'] = df['Awards'].str.extract('Won (\d+) Prime', expand=True).fillna(0)
df['Golden_Globe_Wins'] = df['Awards'].str.extract('Won (\d+) Golden', expand=True).fillna(0)


df[['Wins','Nominations']]=df[['Wins','Nominations']].apply(pd.to_numeric,errors='ignore')
df[['Bafta_Nominations']]=df[['Bafta_Nominations']].apply(pd.to_numeric,errors='ignore')
df[['Oscar_Nominations']]=df[['Oscar_Nominations']].apply(pd.to_numeric,errors='ignore')
df[['Prime_Nominations']]=df[['Prime_Nominations']].apply(pd.to_numeric,errors='ignore')
df[['Golden_Globe_Nominations']]=df[['Golden_Globe_Nominations']].apply(pd.to_numeric,errors='ignore')
df[['Bafta_Wins']]=df[['Bafta_Wins']].apply(pd.to_numeric,errors='ignore')
df[['Oscar_Wins']]=df[['Oscar_Wins']].apply(pd.to_numeric,errors='ignore')
df[['Prime_Wins']]=df[['Prime_Wins']].apply(pd.to_numeric,errors='ignore')
df[['Golden_Globe_Wins']]=df[['Golden_Globe_Wins']].apply(pd.to_numeric,errors='ignore')

#Adding nominations and wins of each award to actul total wins and nominations

df['Wins']=df['Wins'] + df['Bafta_Wins']+df['Oscar_Wins']+    df['Prime_Wins']+df['Golden_Globe_Wins']


df['Nominations']=df['Nominations']+df['Bafta_Nominations']+    df['Oscar_Nominations']+df['Prime_Nominations']+df['Golden_Globe_Nominations']

df.to_csv('Awards.csv', sep=',', encoding='utf-8')


# In[64]:

print(df.head(25))


# In[47]:

df2 = df[['Awards']]


# In[49]:

df3 = df2[df2['Awards'].isnull()==False]


# In[50]:

df3


# In[53]:

df3['Wins']=df3['Awards'].apply(lambda x: (re.findall(r"(\d+) win",x)))
df3['Wins']=df3['Wins'].apply(lambda x:[0] if len(x)==0 else x)


# In[60]:

df3['Wins']=df3['Wins'].apply([lambda x: x.replace('[]',''))


# In[ ]:

df3['wins']=df3['Awards'].apply(lambda x: list(map(int,x))[0])


# In[43]:

df2['Awards'].str.extract('([wins])', expand=True)


# In[35]:

df2['Awards'].str.extract(['(win)(/d)'])

