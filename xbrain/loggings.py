# coding=utf-8

from flask import current_app
from logging.config import fileConfig

import logging


class LoggableMixin(object):

    def __init__(self):
        fileConfig(current_app.config["LOG_CONF_FILEPATH"])
        self.logger = logging.getLogger()
