import pymongo


def read_mongo():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['test_db']
    collection = db['test_collection']
    return [document for document in collection.find({})]
