from flask import Flask
from controllers.target_controller import target_blueprint
from repository.initialize_database import initialize_db
from repository.database import drop_data_base_if_exists
from model import *



def create_flask_app():
    drop_data_base_if_exists()
    initialize_db()
    app = Flask(__name__)
    app.register_blueprint(target_blueprint, url_prefix="/api/targets")
    return app


if __name__ == "__main__":
    create_flask_app().run()