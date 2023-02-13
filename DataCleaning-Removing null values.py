#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv("SAMPLE.csv")


# In[4]:


df


# In[5]:


df.dropna(how="any",subset=["cmark" and (("hsc" and "SSLC") or "arrears")])


# In[ ]:




