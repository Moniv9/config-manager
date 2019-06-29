from flask import Flask, jsonify, request
from flask import make_response
from bson.json_util import dumps
from urllib import parse

from api.configuration_manager import save_config, get_configs, update_config, delete_config, search_config

app = Flask(__name__)


@app.route('/configs', methods=['GET'])
def get_all():
    result = get_configs(None)
    return make_response(dumps(result), 200)


@app.route('/configs/<name>', methods=['GET'])
def get_by_name(name):
    result = get_configs(name)
    return make_response(dumps(result), 200)


@app.route('/search', methods=['GET'])
def search():
    return search_config()


@app.route('/configs', methods=['POST'])
def post():
    if request.is_json:
        return save_config(request.get_json())

    return make_response(jsonify({'error': 'bad request'}), 400)


@app.route('/configs/<name>', methods=['PUT'])
def put(name):
    if request.is_json:
        update_config(name, request.get_json())
        return make_response(jsonify({'message': 'record updated'}), 200)

    return make_response(jsonify({'error': 'bad request'}), 400)


@app.route('/configs/<name>', methods=['DELETE'])
def delete(name):
    message = delete_config(name)
    make_response(jsonify({'message': message}), 200)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
