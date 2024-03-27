#!/usr/bin/env python3
"""
This module provides a function to get the
HTML content of a URL and cache the result with Redis,
using decorators for caching and tracking.
"""
from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Decorator for counting requests and caching the HTML content of a URL.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper for the decorator that handles counting requests and caching.
        """
        # Increment the count for this URL
        redis_.incr(f"count:{url}")
        # Check if the content is already cached
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            # If cached, return the cached content
            return cached_html.decode('utf-8')
        else:
            # If not cached, fetch the content, cache it, and return it
            html = method(url)
            redis_.setex(f"cached:{url}", 10, html)
            return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a URL.
    """
    req = requests.get(url)
    return req.text
