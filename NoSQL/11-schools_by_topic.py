#!/usr/bin/env python3
"""A Python function that returns the list of school having a specific topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """topic (string) will be topic searche"""
    return mongo_collection.find({"topics": topic})
