from flask import Flask
from flask_cors import CORS

from co.deability.jars.api.blueprints.analytics_blueprint import analytics_blueprint

def init_app() -> Flask:

    app: Flask = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_pyfile("../config.py")

    CORS(app)
    _register_error_handlers(app)
    _register_blueprints(app)
    return app


def _register_error_handlers(app) -> None:
    ...

def _register_blueprints(app) -> None:
    app.register_blueprint(analytics_blueprint)
