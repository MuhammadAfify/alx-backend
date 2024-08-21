#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching"""

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
