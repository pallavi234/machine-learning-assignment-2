#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
a = np.random.randint(1,20,(15)) #random and randint function to create vector with random numbers
print(a)


# In[29]:


b= a.reshape(3,5) #reshaping vector into 3 by 5 array
print(b)


# In[30]:


c =np.where(b == [[i]for i in np.amax(b,axis=1)],0,b) #replaced max values of each row with 0
print(c)


# In[7]:


import pandas as pd
data=pd.read_csv("data.csv") #reading csv file using pandas


# In[8]:


data.describe() #basic desciption of the data


# In[9]:


data.isnull() #checking for null values in data


# In[10]:


data.fillna(data.mean(),inplace=True) #filling the null values with mean value
data.head(20)


# In[11]:


data.agg({'Duration' : ['min', 'max','count','mean'], 'Pulse' : ['min', 'max','count','mean']})


# In[12]:


data.loc[(data['Calories'] >=500) & (data['Calories'] <=1000)] #filtering dataframe with calories between 500 and 1000


# In[13]:


data.loc[(data['Calories'] >500) & (data['Pulse'] <100)] #filtering dataframe with calories >500 and pulse < 100


# In[14]:


df_modified = data.drop('Maxpulse',axis=1) #creating new dataframe without Maxpulse
df_modified


# In[15]:


del data["Maxpulse"] #deleted the Maxpulse
data


# In[16]:


data = data.astype({'Calories':'int'}) #changed the datatype of calories
print(data.dtypes)


# In[19]:


ax1 = data.plot.scatter(x='Duration', y='Calories') #created a scatter plot for the two columns (Duration and Calories).
ax1


# In[20]:


import matplotlib.pyplot as plt
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0,0,0)  
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()


# In[27]:





# In[ ]:




