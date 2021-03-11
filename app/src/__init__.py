import os
from .config import config_by_name
from flask import Flask, request
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS()
jwt = JWTManager()
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config_by_name[config_name])

    from .blueprints import v1, v2

    app.register_blueprint(v1)
    app.register_blueprint(v2)

    @app.after_request
    def apply_caching(response):
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        return response

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
    jwt._set_error_handler_callbacks(app)

    return app