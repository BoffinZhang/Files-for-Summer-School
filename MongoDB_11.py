import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]
# 11.1
# myquery = {"name":"John"}
# mycol.delete_one(myquery)
# 11.2
# myquery = {"name":{"regex":"^J"}}

# 11.3
x = mycol.delete_many({})
print(x.deleted_count," documents deleted.")



