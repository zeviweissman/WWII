from repository.initialize_database import initialize_db
from repository.database import drop_data_base_if_exists
from model import *

drop_data_base_if_exists()
initialize_db()