#!/usr/bin/env python3
"""
This module contains the insert_school function,
which inserts a new document into a given MongoDB
collection based on keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection
    based on keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        **kwargs: Keyword arguments representing the fields
        of the document to be inserted.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert(kwargs)
    return result.inserted_id
