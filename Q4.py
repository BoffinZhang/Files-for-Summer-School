# Add zip code
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["restaurant"]

for x in mycol.find({},{"_id":0,"restaurant_id":1,"name":1,"borough":1,"address":1}):
    print(x["restaurant_id"],x["name"],x["borough"],x["address"]["zipcode"])
