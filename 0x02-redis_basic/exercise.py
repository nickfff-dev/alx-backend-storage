#!/usr/bin/env python3
"""
This module provides a Cache class for
storing data in Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    A class for caching data in Redis.
    """
    def __init__(self):
        """
        Initializes the Cache instance with a Redis
        client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a
        random key and returns the key.
        """
        key = str(uuid.uuid4())
        if isinstance(data, str):
            self._redis.set(key, data)
        elif isinstance(data, bytes):
            self._redis.set(key, data)
        elif isinstance(data, int):
            self._redis.set(key, str(data))
        elif isinstance(data, float):
            self._redis.set(key, str(data))
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """
        Retrieves the data associated with
        the given key from Redis.
        If a conversion function is provided,
        it is used to convert the data back to the desired format.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves the data associated with the given
        key from Redis and converts it to a string.
        """
        my_str = self._redis.get(key)
        return my_str.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        Retrieves the data associated with the given
        key from Redis and converts it to an integer.
        """
        answer = self._redis.get(key)
        try:
            answer = int(answer.decode("utf-8"))
        except Exception:
            answer = 0
        return answer
