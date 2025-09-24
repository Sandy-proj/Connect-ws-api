from motor.motor_asyncio import AsyncIOMotorClient

from ..application.settings import settings


def get_mongo_client() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    return client
