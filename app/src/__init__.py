import os
from .config import config_by_name
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

cors = CORS()
jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(config_by_name[config_name])

    from .blueprints import root, v1013

    app.register_blueprint(root)
    app.register_blueprint(v1013)

    @app.after_request
    def apply_caching(response):
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        return response

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
    jwt._set_error_handler_callbacks(app)

    from src import models

    return app