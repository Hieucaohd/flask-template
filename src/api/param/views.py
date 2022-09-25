from flask import Blueprint, jsonify
from src.common.utils.docs_register import register_view
from src.api.param.controller import HelloWorldController

blueprint = Blueprint('param', __name__)


@blueprint.route('/api/create_hello_world', methods=['POST'])
def make_hello_world():
    return jsonify(HelloWorldController.create_hello_world_message())


@blueprint.route('/api/get_all_hello_world', methods=['GET'])
def get_all_hello_world():
    return jsonify({
        "hello": "world"
    })


def register_docs(docs):
    register_view(docs, blueprint, [
        make_hello_world,
    ])

