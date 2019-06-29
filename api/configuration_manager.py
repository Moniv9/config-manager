from flask import jsonify
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['configurations']


def get_configs(name):
    configs = db.configs

    if not name:
        return configs.find({})

    return configs.find_one({'name': name})


def save_config(payload):
    configs = db.configs
    result = configs.insert_one(payload)

    return 'inserted record with id: {0}'.format(result.inserted_id)


def update_config(name, payload):
    configs = db.configs
    result = configs.find_one_and_update({'name': name}, {'$set': payload})

    return result


def search_config():
    configs = db.configs

    return configs.find({})


def delete_config(name):
    configs = db.configs
    configs.delete_one({'name': name})

    return 'record deleted'
