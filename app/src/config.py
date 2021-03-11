import datetime
import os

BASE_DIR = os.path.join(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    RESTX_MASK_SWAGGER = False

class Production(Config):
    JWT_SECRET_KEY = 'flask-secret-jwt'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, 'sample_flask_prod.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SECRET_KEY = "flask-secret"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, 'sample_flask_dev.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ERROR_404_HELP= False

class Testing(Development):
    SECRET_KEY = "flask-secret-test"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, 'sample_flask_test.db'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev=Development,
    test=Testing,
    prod=Production
)
