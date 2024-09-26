from flask import Flask
from controllers.target_controller import target_blueprint

def create_flask_app():
    app = Flask(__name__)
    app.register_blueprint(target_blueprint, url_prefix="/api/targets")
    return app


if __name__ == "__main__":
    create_flask_app().run()