class Config(object):
    """
    Common configurations
    """

    # Common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1974tanya5@localhost/departments_db_1'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://pnnclnxtllplex:e27b2e5623dc0b6bd609f3418a0e98e8a011df985c125812e3cdcb98369b3123@ec2-54-220-53-223.eu-west-1.compute.amazonaws.com:5432/deon0a3nehg6cq'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI='sqlite:///departments_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


