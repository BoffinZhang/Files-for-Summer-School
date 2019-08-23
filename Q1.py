import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]

mylist = mycol.find()
for x in mylist:
    print(x)



