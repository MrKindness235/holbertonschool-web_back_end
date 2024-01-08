#!/usr/bin/env python3
"""A Python function that inserts a
new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """mongo_collection will be the pymongo collection object"""
    document_id = mongo_collection.insert_one(kwargs).inserted_id
    return document_id
