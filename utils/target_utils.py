from typing import List, Dict
from model import Target
from returns.maybe import Some, Nothing, Maybe


def target_has_all_keys(d: Dict[str, str]) -> bool:
    return all(k in d for k in ['priority', 'location_id', 'type_id'])


def json_to_target_model(json: Dict[str, str]) -> Target:
    return Target(
        priority=json.get('priority'),
        location_id=json.get('location_id'),
        type_id=json.get('type_id')
    )

def return_target_if_json_has_all_keys(json: Dict[str, str], has_all_keys: bool) -> Maybe[Target]:
    return Some(json_to_target_model(json)) if has_all_keys else Nothing