from flask import Blueprint, jsonify, request
from model import Target
import service.target_service as target_service


target_blueprint = Blueprint("mission", __name__)


@target_blueprint.route('/<int:target_id>', methods=['GET'])
def get_target_by_id(target_id):
    return jsonify({}, 400)

@target_blueprint.route('/', methods=['GET'])
def get_all_targets():
    return jsonify({}, 400)



@target_blueprint.route('/create', methods=['POST'])
def create_target():
    return (
            target_service.insert_target(request.json)
            .map(lambda target: (jsonify(target), 201 ))
            .value_or((jsonify({}), 400))
            )