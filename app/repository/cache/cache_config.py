import aioredis


class RedisClient:
    connection = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def establish_connection(self):
        if self.connection is None or not self.connection.is_connected:
            self.connection = await aioredis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)

    async def close_connection(self):
        if self.connection:
            await self.connection.close()

    async def get_connection(self):
        if self.connection is None or self.connection.closed:
            await self.establish_connection()
        return self.connection


redis_client = RedisClient()
