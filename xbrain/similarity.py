# coding=utf-8

from xbrain.core.word2vectors import GensimWord2Vector
from xbrain.loggings import LoggableMixin


class Similarity(LoggableMixin):
    """ 相似度 """

    def __init__(self, *args, **kwargs):
        super(Similarity, self).__init__(*args, **kwargs)

    def most_similar(self):
        pass


class Word2VectorSimilarity(Similarity):
    """ 基于词向量实现相似度 """

    def __init__(self, corpus, model_path=None, *args, **kwargs):
        super(Word2VectorSimilarity, self).__init__(*args, **kwargs)

        wv = GensimWord2Vector()
        if model_path is None:
            self.model = wv.train(corpus, **kwargs)
        else:
            self.model = wv.load(model_path)

    def most_similar(self, words):
        result = {}
        if not isinstance(words, list):
            words = [words]

        for word in words:
            try:
                word_similars = [
                    list(similar)
                    for similar in self.model.wv.most_similar(word)]
            except KeyError:
                word_similars = []

            result[word] = word_similars

        return result
