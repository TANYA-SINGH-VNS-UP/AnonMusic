from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("⚙️ Mongo database fetching")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("🗂️ Successfully fetched database.")
except:
    LOGGER(__name__).error("🚫 Failed to connect to your Mongo Database.")
    exit()
