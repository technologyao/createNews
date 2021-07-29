from pymongo import MongoClient
import json

client = MongoClient()

file = open ('client.json')
data = json.load(file)


db = client.testdb
collection = db.test_collection


result = collection.insert_many(data['News'])
#print(result.inserted_ids)

#result_find = result = collection.find_one({'Title': 'NewsA'})
#result_find = list(collection.find({'Title': 'NewsB'}))
#print(result_find)
