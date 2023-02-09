#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pymongo


# In[ ]:


connection=pymongo.MongoClient("mongodb://santhiya1204:santhiya1204@ac-dqtoutk-shard-00-00.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-01.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-02.oeojj5f.mongodb.net:27017/?ssl=true&replicaSet=atlas-6lfbkt-shard-0&authSource=admin&retryWrites=true&w=majority")


# In[ ]:


emp=connection["work"]


# In[ ]:


sampleSupplies = connection["sample_supplies"]


# In[ ]:


sample_supp=sampleSupplies["sales"]


# In[ ]:


B=[]
for i in sample_supp.find({"$and":[{"$and":[{"customer.age":{"$gte":50}},{"customer.age":{"$lte":70}}]},{"customer.gender":"F"},{"purchaseMethod":{"$in":["Online","Phone"]}},{"storeLocation":"Seattle"}]},{"_id":0,"customer.age":1,"customer.gender":1,"purchaseMethod":1,"storeLocation":1}):
      B.append(i)


# In[ ]:


import pandas as pd


# In[ ]:


df1=pd.DataFrame(B)


# In[ ]:


df1.to_csv("samplesupplies.csv")

