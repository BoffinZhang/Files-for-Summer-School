import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("It doesn't exist")

# extra line
# print(myclient.list_database_names())
