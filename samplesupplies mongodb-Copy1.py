import pymongo

connection=pymongo.MongoClient("mongodb://santhiya1204:santhiya1204@ac-dqtoutk-shard-00-00.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-01.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-02.oeojj5f.mongodb.net:27017/?ssl=true&replicaSet=atlas-6lfbkt-shard-0&authSource=admin&retryWrites=true&w=majority")

emp=connection["work"]

sampleSupplies = connection["sample_supplies"]

sample_supp=sampleSupplies["sales"]

B=[]
for i in sample_supp.find({"$and":[{"$and":[{"customer.age":{"$gte":50}},{"customer.age":{"$lte":70}}]},{"customer.gender":"F"},{"purchaseMethod":{"$in":["Online","Phone"]}},{"storeLocation":"Seattle"}]},{"_id":0,"customer.age":1,"customer.gender":1,"purchaseMethod":1,"storeLocation":1}):
      B.append(i)


import pandas as pd

df1=pd.DataFrame(B)

df1.to_csv("samplesupplies.csv")

