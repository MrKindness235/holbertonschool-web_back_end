#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    a_list = []
    if mongo_collection is not None:
        documents = mongo_collection.find()
        return documents

    return a_list