from model import Target
from returns.maybe import Maybe, Nothing, Some
from returns.result import Result, Success, Failure
from repository.database import session_factory
from sqlalchemy.exc import SQLAlchemyError
from typing import List


def insert_target(target: Target) -> Result[Target, Exception]:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            return Failure(e)




def get_target_by_id(target_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.get(Target, target_id)
        )



def delete_target_by_id(target_id: int) -> Result[Target, str]:
    with session_factory() as session:
        try:
            if target_to_delete := session.get(Target, target_id):
                session.delete(target_to_delete)
                session.commit()
                return Success(target_to_delete)
            else:
                return Failure(f"target by id:{target_id} was not found")
        except SQLAlchemyError as e:
            return Failure(e)


def update_target(target: Target) -> Result[Target, str]:
    with session_factory() as session:
        try:
            if target_to_update := session.get(Target, target.id):
                target_to_update = target
                session.commit()
                return Success(target_to_update)
            else:
                return Failure(f"target by id:{target.id} was not found")
        except SQLAlchemyError as e:
            return Failure(e)

