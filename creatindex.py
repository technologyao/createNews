from pymongo import MongoClient
import json

client = MongoClient()

file = open ('client.json')
data = json.load(file)


db = client.testdb
collection = db.test_collection

collection.create_index([("Author", 1)], unique= True ,sparse= True)
collection.create_index([("Title", 1)], unique= True ,sparse= True)


#result = collection.insert_many(data['News']) #新增資料
#print(result.inserted_ids) _id=object


result_find = result = collection.find_one({'Detail':{'Author': 'Wally', 'Content': 'Hello World'}})  #找資料
#result_find = list(collection.find({'Title': 'NewsB'}))
print(result_find)
