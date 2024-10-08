import repository.target_repository as target_repos
import toolz as t
from model import Target
from returns.maybe import Some, Nothing, Maybe
from dictalchemy.utils import asdict
from typing import Dict
from utils.target_utils import *


def insert_target(target_json: Dict[str, str]) -> Maybe[Target]:
    return (
            convert_to_target_for_create(target_json)
            .bind(target_repos.insert_target)
            .map(target_as_dict)
            )

def get_target_by_id(target_id):
    return (
        target_repos.get_target_by_id(target_id)
        .map(target_as_dict)
    )

def get_all_targets():
    return (
        target_repos.get_all_targets()
        .map(lambda li: {"targets":[target_as_dict(trgt) for trgt in li]})
    )


def delete_target_by_id(target_id):
    return (
        target_repos.delete_target_by_id(target_id)
        .map(target_as_dict)
    )


def update_target(target_json: Dict[str, str]) -> Maybe[Target]:
    return (
            convert_to_target_for_update(target_json)
            .bind(target_repos.update_target)
            .map(target_as_dict)
            )