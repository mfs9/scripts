import pprint

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodbaddress")
db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author":"Mike"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\nRecuperando info da coleção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Joao'}]

result = db.profile.insert_many(user_profile_user)

print("\nColeções armazenadas no mongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# db['posts'].drop()


for post in posts.find():
    pprint.pprint(post)

# print(posts.delete_one({"author":"Mike"}))

client.drop_database('test')
print(db.list_collection_names())
