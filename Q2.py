import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]


for x in mycol.find({},{"restaurant_id":1,"name":1,"borough:":1,"cuisine":1}):
    print(x)
