from src.scheduler.user_access_url import access_url_receive_consumer
from src.database.mongo import MongoDBInit


MongoDBInit.init_client(config={
    'MONGO_URI': "mongodb://localhost:27017",
    'DB_NAME': "devDB"
})
access_url_receive_consumer()
