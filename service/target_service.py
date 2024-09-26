import repository.target_repository as target_repos
import toolz as t
from model import Target
from returns.maybe import Some, Nothing, Maybe
from dictalchemy.utils import asdict
from typing import Dict
from utils.target_utils import *


def convert_to_target(target_json: Dict[str, str]) -> Maybe[Target]:
    return pipe(
        target_json,
        target_has_all_keys,
        t.partial(return_target_if_json_has_all_keys, target_json)
    )


def insert_target(target_json: Dict[str, str]) -> Maybe[Target]:
    return (
            convert_to_target(target_json)
            .bind(target_repos.insert_target)
            .map(asdict)
            )

