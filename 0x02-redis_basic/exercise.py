#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, int)

# Usage example
if __name__ == "__main__":
    cache = Cache()
    test_cases = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }
    for value, fn in test_cases.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
