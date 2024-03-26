#!/usr/bin/env python3
"""
This module contains the schools_by_topic function,
which returns a list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection object.
        topic (str): The topic searched.

    Returns:
        list: A list of schools that have the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
