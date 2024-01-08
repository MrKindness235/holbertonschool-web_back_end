#!/usr/bin/env python3
"""a Python script that provides some stats about
Nginx logs stored in MongoDB"""

import pymongo

from pymongo import MongoClient


from pymongo import MongoClient
# intance mongo - Local host
client = MongoClient("mongodb://localhost:27017/")

database = client.logs
collection = database.nginx
count_document = collection.count_documents({})
print(f"{count_document} logs")
