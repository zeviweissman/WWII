from flask import Blueprint, jsonify, request
from model import Mission

target_blueprint = Blueprint("mission", __name__)


@target_blueprint.route('<int:target_id>', ['GET'])
def get_target_by_id(target_id):
    return jsonify({}, 400)

@target_blueprint.route('/', ['GET'])
def get_all_targets():
    return jsonify({}, 400)