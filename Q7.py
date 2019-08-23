# Add zip code
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]

myquery = {"borough":{"$regex":"Bronx"}}

mylist = mycol.find(myquery,{"_id":0,"restaurant_id":1,"name":1,"borough":1,"address":1}).limit(10)

for i in range(5,10):
    print(mylist[i])
