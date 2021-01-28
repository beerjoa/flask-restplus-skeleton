import datetime

class Config(object):
    DEBUG = False
    TESTING = False

class Production(Config):
    JWT_SECRET_KEY = 'flask-secret-jwt'
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True

class Development(Config):
    SECRET_KEY = "flask-secret"
    DEBUG = True

class Testing(Development):
    SECRET_KEY = "flask-secret-test"
    TESTING = True