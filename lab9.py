#!/usr/bin/env python3


from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://nmagee:20oRGqjmo88JOF0k@cluster0.pnxzwgz.mongodb.net/")

# switch to my database
db = client.jww2fj

# insert documents into new collection
newcollection = db.newcollection
newcollection.insert_many([
    {"name": "lily", "age": 20, "school": "UVA"},
    {"name": "anna", "age": 21, "school": "UVA"},
    {"name": "sarah", "age": 19, "school": "Clemson"},
    {"name": "peyton", "age": 20, "school": "Tennessee"},
    {"name": "emma", "age": 21, "school": "UVA"}
])

# query to get 3 documents
query_result = newcollection.find({"school": "UVA"}).limit(3)

# Print the query result
for document in query_result:
    print(document)
