from repository.database import create_data_base_if_not_exists, create_tabels_if_not_exists



def initialize_db():
    create_data_base_if_not_exists()
    create_tabels_if_not_exists()
