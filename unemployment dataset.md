# Inserting-Unemployment-Dataset-to-Mongodb-through-Python

import pymongo

connection=pymongo.MongoClient("mongodb://santhiya1204:<password>@ac-dqtoutk-shard-00-00.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-01.oeojj5f.mongodb.net:27017,ac-dqtoutk-shard-00-02.oeojj5f.mongodb.net:27017/?ssl=true&replicaSet=atlas-6lfbkt-shard-0&authSource=admin&retryWrites=true&w=majority")

umemp=connection["work"]


import vega_datasets
dir(vega_datasets.data)

data1 = vega_datasets.data.unemployment()
data1_dict=data1.to_dict("records")

unemp_unemployment=sandy["unemplyment"]

unemp_unemployment.insert_many(data1_dict)
