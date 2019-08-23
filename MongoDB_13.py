import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]

# 13.1
'''
myquery = {"address":"Valley 345"}
newvalues = {"$set":{"address":"Canyon 123"}}
mycol.update_one(myquery,newvalues)
for x in mycol.find():
    print(x)
'''

myquery = {"address":{"$regex":"^J"}}
newvalues = {"$set":{"name":"Minnie"}}
x = mycol.update_many(myquery,newvalues)
print(x.modified_count,"documents updated.")
for x in mycol.find():
    print(x)
