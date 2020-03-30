#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]


# In[3]:


GradeList = zip(names,grades)


# In[4]:


df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])


# In[5]:


df


# In[6]:


df.loc[(df['Grades'] < 0, 'Grades')] = 0


# In[7]:


df


# In[ ]:




