#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = 'https://www.bbc.com/news/science-environment-63950962'
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")


# In[3]:


A = []
for el in soup.findAll('p'):
        A.append(el.get_text().strip().lower())


# In[4]:


import pandas as pd


# In[5]:


df = pd.DataFrame(columns = ['Text'])

for i in range(len(A)):
    df.loc[i] = [A[i]]
    
df


# In[6]:


df.to_csv('Text1',index = False)


# In[ ]:




