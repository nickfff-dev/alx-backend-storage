#!/usr/bin/env python3

import redis
import uuid
from typing import Any, Union, Callable, Optional
from functools import wraps

"""
This module provides a Cache class for
storing data in Redis.
"""


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts how many times a method is called.
    """

    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """ Increments the count for a method in Redis."""
        # Use the qualified name of the method as the key
        key = method.__qualname__
        # Increment the count for this key in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of
    inputs and outputs for a particular function.
    """

    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """ Stores the input and output of a method in Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Store the input arguments
        self._redis.rpush(input_key, str(args))
        # Execute the wrapped function and store its output
        result = method(self, *args)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a
        random key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
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
        if not data:
            return
        if fn is int:
            return self.get_int(key)
        if fn is str:
            return self.get_str(key)
        if callable(fn):
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        Retrieves the data associated with the given
        key from Redis and converts it to a string.
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """
        Retrieves the data associated with the given
        key from Redis and converts it to an integer.
        """
        return int(data)


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function.
    """
    key = method.__qualname__
    cache = redis.Redis()
    func_calls = cache.get(key).decode("utf-8")
    inputs = [
        call.decode("utf-8") for call in cache.lrange(f"{key}:inputs", 0, -1)
    ]
    outputs = [
        call.decode("utf-8") for call in cache.lrange(f"{key}:outputs", 0, -1)
    ]

    print(f"{key} was called {func_calls} times:")
    for input_args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, input_args, output))
