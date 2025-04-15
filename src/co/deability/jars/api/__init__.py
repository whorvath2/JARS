from flask import Flask
from flask_cors import CORS

from co.deability.jars.api.blueprints.analytics_blueprint import analytics_blueprint
from co.deability.jars.error import handling


def init_app() -> Flask:

    app: Flask = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_pyfile("../config.py")

    CORS(app)
    _register_error_handlers(app)
    _register_blueprints(app)
    return app


def _register_error_handlers(app) -> None:
    app.register_error_handler(AssertionError, handling.handle_assertion_errors)
    app.register_error_handler(EnvironmentError, handling.handle_jars_errors)
    app.register_error_handler(404, handling.handle_url_not_found)
    app.register_error_handler(500, handling.handle_internal_errors)


def _register_blueprints(app) -> None:
    app.register_blueprint(analytics_blueprint)
