# coding=utf-8

import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_CONF_FILEPATH = os.path.join(BASE_DIR, "xbrain", "logging_config.ini")

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
