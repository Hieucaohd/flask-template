from src.api.param.models import HelloWorldModel


class HelloWorldService:
    model = HelloWorldModel

    @classmethod
    def create_hello_world(cls, name, age):
        return cls.model.collection.insert_one({
            "name": name,
            "age": age
        })

