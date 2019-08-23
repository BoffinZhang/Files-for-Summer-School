# Add zip code
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]

myquery = {"grades":{"$elemMatch":{"score":{"$gt":90}}}}

mylist = mycol.find(myquery).limit(10)

for x in mylist:
    print(x)
