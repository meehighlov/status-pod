from flask import Flask

from status_pod.api.v1.blueprint import activity
from status_pod.app.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(activity)

    return app
