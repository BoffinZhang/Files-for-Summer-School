import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]
mydict = {"name":"John","address":"Jordanstown"}

x = mycol.insert_one(mydict)

print(x.inserted_id)


mylist = [
    {"_id":1,"name":"Peter","address":"Apple st 652"},
    {"_id":2,"name":"Sandy","address":"Mountain 21"},
    {"_id":3,"name":"Betty","address":"Valley 345"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)
