from flask import request

from src.api.param.services import HelloWorldService


class HelloWorldRequestDataParam:
    name = "name"
    age = "age"


class HelloWorldController:
    @classmethod
    def create_hello_world_message(cls):
        request_data = request.json
        result = HelloWorldService.create_hello_world(
            request_data.get(HelloWorldRequestDataParam.name),
            request_data.get(HelloWorldRequestDataParam.age)
        )
        return {
            "data": {
                'inserted_id': str(result.inserted_id)
            },
            "message": "request thanh cong"
        }
