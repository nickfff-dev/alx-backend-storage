#!/usr/bin/env python3
"""
This module contains the update_topics function,
which updates the 'topics' field of all documents
in a given MongoDB collection based on the school's name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents in a
    MongoDB collection based on the school's name.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list): The list of topics approached
        in the school.

    Returns:
        UpdateResult: The result of the update operation.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
