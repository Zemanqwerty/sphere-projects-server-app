import os
basedir = os.path.abspath(os.path.dirname('app.py'))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.urandom(32)
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql://zeman:postgres@localhost:5432/sphere-projects-server-app'
    SESSION_TYPE = 'filesystem'


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True