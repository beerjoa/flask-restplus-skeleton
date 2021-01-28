import datetime

class Config(object):
    DEBUG = False
    TESTING = False

class Production(Config):
    pass

class Development(Config):
    SECRET_KEY = "flask-secret"
    DEBUG = True

class Testing(Development):
    SECRET_KEY = "flask-secret-test"
    TESTING = True