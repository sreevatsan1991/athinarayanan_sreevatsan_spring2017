
# coding: utf-8

# In[1]:

import pandas as pd
df = pd.read_csv('Data\employee_compensation.csv')


# In[9]:

df1= df[df['Year Type']=='Calendar'].reset_index(level=0,drop =True)


# In[13]:

df2=df1.groupby(['Employee Identifier','Job Family']).mean().reset_index()


# In[16]:

df2['salary_overtime_ratio'] =(df2['Overtime']/df2['Salaries'])*100


# In[18]:

df3 = df2[df2['salary_overtime_ratio']>5]


# In[21]:

df4 =df3.groupby('Job Family')['Total Benefits','Total Compensation'].mean()


# In[23]:

df4['Percent_Total_Benefit']= (df4['Total Benefits']/df4['Total Compensation'])*100


# In[24]:

print(df4.head())


# In[ ]:

df4.to_csv('Output\Question2_part2.csv')

