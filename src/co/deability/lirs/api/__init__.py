"""
Copyright © 2021 William L Horvath II

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from flask import Flask
from flask_cors import CORS

from co.deability.lirs.api.blueprints import analytics_blueprint

def init_app() -> Flask:

    app: Flask = Flask(__name__)
    app.url_map.strict_slashes = False

    CORS(app)
    _register_error_handlers(app)
    _register_blueprints(app)
    return app


def _register_error_handlers(app) -> None:
    ...

def _register_blueprints(app) -> None:
    app.register_blueprint(analytics_blueprint)
