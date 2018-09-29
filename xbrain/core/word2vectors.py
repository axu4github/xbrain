# coding=utf-8

from xbrain.loggings import LoggableMixin
from xbrain.core.participles import JiebaParticiple
from xbrain.utils import Utils
from xbrain.doraemon import Doraemon

import gensim
import os


class Sentences(object):

    def __init__(self, resources):
        self.resources = resources

    def __iter__(self):
        return Utils.get_resources_contents(self.resources).split()


class Word2Vectors(LoggableMixin):
    """ 词向量 """

    def __init__(self, *args, **kwargs):
        super(Word2Vectors, self).__init__(*args, **kwargs)

    def train(self, corpus):
        pass

    def load(self, model):
        pass


class GensimWord2Vector(Word2Vectors):
    """ 基于 Gensim 实现的词向量 """

    def __init__(self, *args, **kwargs):
        super(GensimWord2Vector, self).__init__(*args, **kwargs)

    def train(self, corpus, is_segment=False,
              business_word_dics=None, stop_word_dics=None,
              save_model_path=None, size=500, window=5, min_count=10,
              **kwargs):
        if is_segment:
            corpus = JiebaParticiple(
                business_word_dics=business_word_dics,
                stop_word_dics=stop_word_dics).segment(corpus=corpus)

        self.logger.debug("corpus => [{0}]".format(", ".join(corpus)))

        sentences = [row.split()
                     for row in Utils.get_resources_contents(corpus)]
        model = gensim.models.word2vec.Word2Vec(
            sentences, sg=0, hs=1, size=size, workers=1,
            window=window, min_count=min_count, **kwargs)

        if save_model_path is not None:
            if os.path.isfile(save_model_path):
                os.unlink(save_model_path)

            model.save(save_model_path)

        return model

    def load(self, model):
        if not os.path.isfile(model):
            raise Exception("Model Path [{0}] is Not Found.".format(model))

        return gensim.models.Word2Vec.load(model)
