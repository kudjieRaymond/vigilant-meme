from decouple import config

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://") :
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(Object):
    DEBUG =False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = config('SECRET_KEY', default='gess-me')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG=True
    DEVELOPMENT= True



class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT= True


class TestingConfig(Config):
    TESTING=True


