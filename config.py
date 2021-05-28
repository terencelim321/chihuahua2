import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = os.environ['postgres://ooxeoyhmzkoaet:5d0156ba0cd2041fcce04a1af768b93c5834e877d9086390d7c2111dd608f8cf@ec2-34-200-94-86.compute-1.amazonaws.com:5432/ddfcrdjbfcqmlo']

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

