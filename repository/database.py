from config.base import _session_factory, Base, engine
from sqlalchemy_utils import database_exists, create_database, drop_database


def create_data_base_if_not_exists():
    if not database_exists(engine.url):
        create_database(engine.url)

def drop_data_base_if_exists():
    if database_exists(engine.url):
        drop_database(engine.url)



def session_factory():
    return _session_factory()

