# coding=utf-8

from xbrain.loggings import LoggableMixin


class Similarity(LoggableMixin):
    """ 相似度 """

    def __init__(self, *args, **kwargs):
        super(Similarity, self).__init__(*args, **kwargs)

    def most_similar(self):
        return "most_similar"
