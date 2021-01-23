# -- coding: utf-8 --
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import unittest

from flask_script import Manager
from flask import Flask, request
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from blueprints.root import blueprint as root
from blueprints.v1013 import blueprint as v1013

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

app.register_blueprint(root)
app.register_blueprint(v1013)

cors = CORS(app)
manager = Manager(app)
app.secret_key = 'flask-secret-key'
app.config['JWT_SECRET_KEY'] = 'flask-secret-key'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True
jwt = JWTManager(app)
jwt._set_error_handler_callbacks(app)


@manager.command
def test():
    """
        unit tests
    """
    tests = unittest.TestLoader().discover('src/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1



@manager.command
def run():
    """
        run server
    """
    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    manager.run()
