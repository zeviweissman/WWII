from flask import Blueprint, jsonify, request
from model import Target
import service.target_service as target_service


target_blueprint = Blueprint("mission", __name__)


@target_blueprint.route('/', methods=['GET'])
def get_all_targets():
    return (
            target_service.get_all_targets()
            .map(lambda li: (jsonify(li), 200 ))
            .value_or((jsonify({}), 404))
            )


@target_blueprint.route('/<int:target_id>', methods=['GET'])
def get_target_by_id(target_id):
    return (
            target_service.get_target_by_id(target_id)
            .map(lambda target: (jsonify(target), 200 ))
            .value_or((jsonify({}), 404))
            )

@target_blueprint.route('/delete/<int:target_id>', methods=['DELETE'])
def delete_target_by_id(target_id):
    return (
            target_service.delete_target_by_id(target_id)
            .map(lambda target: (jsonify(target), 200 ))
            .value_or((jsonify({}), 404))
            )


@target_blueprint.route('/create', methods=['POST'])
def create_target():
    return (
            target_service.insert_target(request.json)
            .map(lambda target: (jsonify(target), 201 ))
            .value_or((jsonify({}), 400))
            )


@target_blueprint.route('/update', methods=['PUT'])
def update_target():
    return (
        target_service.update_target(request.json)
        .map(lambda target: (jsonify(target), 201))
        .value_or((jsonify({}), 400))
    )