from repository.database import create_data_base_if_not_exists, session_factory
from repository.query import *


def create_mission_table():
    pass


def load_missions_to_db():
    pass

def create_tabels_if_not_exists():
    create_mission_table()
    Base.metadata.create_all(engine)


def transfer_info_into_normalized_db():
    with session_factory() as session:
        session.execute(normalize_countries_query)
        session.execute(normalize_locations_query)
        session.execute(normalize_types_query)
        session.execute(normalize_targets_query)
        session.commit()


def initialize_db():
    create_data_base_if_not_exists()
    create_tabels_if_not_exists()
    load_missions_to_db()
    transfer_info_into_normalized_db()
