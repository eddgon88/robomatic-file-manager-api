# application/__init__.py
import config
import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    with app.app_context():
        from .file_manager import file_manager_blueprint
        app.register_blueprint(file_manager_blueprint)
        return app
