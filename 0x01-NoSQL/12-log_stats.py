#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def get_log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Select the 'logs' database and 'nginx' collection
    collection = client.logs.nginx

    # Count the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of logs with method=GET and path=/status
    status_check = \
        collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_log_stats()
