import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]

# sort by address
mydoc = mycol.find().sort("address",-1)
for x in mydoc:
    print(x)
