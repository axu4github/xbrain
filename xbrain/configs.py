# coding=utf-8

import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    LOG_DIR = os.path.join(BASE_DIR, "logs")
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_CONF_FILEPATH = os.path.join(BASE_DIR, "xbrain", "logging_config.ini")

    TEST_DIR = os.path.join(BASE_DIR, "tests")
    TEST_RESOURCES_DIR = os.path.join(TEST_DIR, "resources")
    TEST_CORPUS_DIR = os.path.join(TEST_RESOURCES_DIR, "corpus")
    TEST_DICS_DIR = os.path.join(TEST_RESOURCES_DIR, "dics")
    TEST_MODELS_DIR = os.path.join(TEST_RESOURCES_DIR, "models")

    DEFAULT_W2V_SAVE_MODEL_PATH = os.path.join(
        TEST_MODELS_DIR, "default_w2v.model")

    DEFAULT_W2V_MODEL_SIZE = 500
    DEFAULT_W2V_MODEL_WINDOW = 5
    DEFAULT_W2V_MODEL_MIN_COUNT = 10
    DEFAULT_W2V_MODEL_WORKER = 2
    DEFAULT_W2V_MODEL_BATCH_SIZE = 100000

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
