import os
from typing import Union

import redis


class RedisConnector:
    pool = redis.ConnectionPool.from_url(
        f"redis://:"
        f"{os.environ.get('REDIS_PASSWORD')}@"
        f"{os.environ.get('REDIS_HOST')}:"
        f"{os.environ.get('REDIS_PORT')}"
    )

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "instance"):
            return cls.instance
        instance = super().__new__(cls)
        cls.instance = instance
        return instance

    def __init__(self):
        self.connection: Union[redis.Redis, None] = None

    def __enter__(self):
        if not self.connection:
            self.connection = redis.Redis(
                connection_pool=self.pool, decode_responses=True
            )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        self.connection = None
