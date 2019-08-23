# Filter the Result#

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["costomers"]



# myquery = {"address":"Apple st 652"}
# myquery = {"address":{"$gt":"S"}}


myquery = {"address":{"$regex":"^J"}} # find address start with J

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
