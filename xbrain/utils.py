# coding=utf-8

from xbrain.doraemon import Doraemon


class Utils(object):
    """ 工具类 """

    @staticmethod
    def get_files_contents(_dirs):
        if not isinstance(_dirs, list):
            _dirs = [_dirs]

        for _dir in _dirs:
            for _file in Doraemon.get_files(_dir):
                for line in Doraemon.get_file_contents(_file):
                    yield line.strip()
