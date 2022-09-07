import pymongo
from loguru import logger


def add_info_to_mongo(data: dict[str: str]):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['test_db']
    collection = db['test_collection']
    collection.insert_one(data).inserted_id
    logger.success('Data was added successfully!')


# add_info_to_mongo(d)
