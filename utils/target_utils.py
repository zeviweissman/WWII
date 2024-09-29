from typing import List, Dict
from model import Target
from returns.maybe import Some, Nothing, Maybe
import toolz as t

def target_has_all_keys_except_id(d: Dict[str, str]) -> bool:
    return all(k in d for k in ['priority', 'location_id', 'type_id'])


def target_has_all_keys(d: Dict[str, str]) -> bool:
    return all(k in d for k in ['id', 'priority', 'location_id', 'type_id'])


def json_to_target_model(json: Dict[str, str]) -> Target:
    return Target(
        id=json.get('id'),
        priority=json.get('priority'),
        location_id=json.get('location_id'),
        type_id=json.get('type_id')
    )

def return_target_if_json_has_all_keys(json: Dict[str, str], has_all_keys: bool) -> Maybe[Target]:
    return Some(json_to_target_model(json)) if has_all_keys else Nothing


def convert_to_target_for_create(target_json: Dict[str, str]) -> Maybe[Target]:
    return t.pipe(
        target_json,
        target_has_all_keys_except_id,
        t.partial(return_target_if_json_has_all_keys, target_json)
    )


def convert_to_target_for_update(target_json: Dict[str, str]) -> Maybe[Target]:
    return t.pipe(
        target_json,
        target_has_all_keys,
        t.partial(return_target_if_json_has_all_keys, target_json)
    )


def target_as_dict(target: Target):
    return {
        "id": target.id,
        "priority": target.priority,
        "city": target.location.city,
        "country": target.location.country.country,
        "lat": target.location.lat,
        "lon": target.location.lon,
        "type": target.type.type
    }