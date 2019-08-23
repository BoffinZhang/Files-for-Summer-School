# Add zip code
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]

myquery = {"borough":{"$regex":"Bronx"}}

for x in mycol.find(myquery):
    print(x)
