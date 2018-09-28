# coding=utf-8

from xbrain import create_app


def test_config():
    assert create_app().testing
