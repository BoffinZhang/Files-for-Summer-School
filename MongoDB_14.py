import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]

myresult = mycol.find().limit(2)
for x in myresult:
    print(x)
