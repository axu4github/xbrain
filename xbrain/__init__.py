# coding=utf-8

from flask import Flask
from xbrain.configs import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["testing"])

    from .apis import apis
    app.register_blueprint(apis)

    return app
