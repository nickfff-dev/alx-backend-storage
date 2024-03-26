#!/usr/bin/env python3
"""
This module contains the list_all function,
which lists all documents in a given MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.

    Returns:
        list: A list of all documents in the collection.
        If the collection is empty, returns an empty list.
    """
    # Use the find method without any arguments to retrieve all documents
    documents = mongo_collection.find()
    # Convert the cursor to a list and return it
    return list(documents)
