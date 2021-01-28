import os
from flask import Flask, request

def create_app():
    from flask_cors import CORS
    from flask_jwt_extended import JWTManager

    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_object('src.config.Development')
    from .blueprints import root, v1013

    app.register_blueprint(root)
    app.register_blueprint(v1013)

    @app.after_request
    def apply_caching(response):
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        return response

    cors = CORS(app)
    jwt = JWTManager(app)
    jwt._set_error_handler_callbacks(app)


    return app