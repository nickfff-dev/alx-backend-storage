#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
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
    def wrapper(self, *args, **kwargs):
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
    def wrapper(self, *args, **kwargs):
        """ Stores the input and output of a method in Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Store the input arguments
        self._redis.rpush(input_key, str(args))
        # Execute the wrapped function and store its output
        result = method(self, *args, **kwargs)
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


def replay(method: Callable) -> None:
    """
    Displays the history of calls of a particular function.
    """
    key = method.__qualname__
    cache = redis.Redis()
    funcs = cache.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, funcs))
    inputs = cache.lrange(f"{key}:inputs", 0, -1)
    outputs = cache.lrange(f"{key}:outputs", 0, -1)
    for input_args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, input_args.decode("utf-8"),
                                     output.decode("utf-8")))
