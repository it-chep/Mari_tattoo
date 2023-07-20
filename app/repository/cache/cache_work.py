from .cache_config import redis_client


class RedisRepository:
    def __init__(self):
        self.redis = redis_client

    async def set_value(self, key: str, value: str, timeout=None):
        await self.redis.connection.set(key, value, ex=timeout)

    async def get_value(self, key: str, ):
        return await self.redis.connection.get(key)

    async def delete_value(self, key):
        return await self.redis.connection.delete(key)
    