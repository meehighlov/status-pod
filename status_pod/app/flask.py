from flask import Flask

from status_pod.api.v1.views import activity
from status_pod.app.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.url_map.strict_slashes = False
    app.register_blueprint(activity)

    print(app.url_map)

    return app
