# coding=utf-8

from xbrain.doraemon import Doraemon


class Utils(object):
    """ 工具类 """

    @staticmethod
    def get_resources_contents(resources):
        """ 获取所有文件或者目录下文件的内容 """
        if not isinstance(resources, list):
            resources = [resources]

        for resource in resources:
            for _file in Doraemon.get_files(resource):
                for row in Doraemon.get_file_contents(_file):
                    yield row.strip()
