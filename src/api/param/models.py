from src.database.mongo.base_model import BaseMongoDB


class HelloWorldModel(BaseMongoDB):
    meta = {
        'indexes': [
            {
                "fields": ["+name", "+age"],
                "unique": True
            }
        ],
        'auto_timestamp': True
    }
