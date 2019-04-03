# coding=utf-8

from xbrain.loggings import LoggableMixin
from xbrain.core.participles import JiebaParticiple
from xbrain.utils import Utils

import gensim
import os


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
              workers=1, **kwargs):
        if is_segment:
            corpus = JiebaParticiple(
                business_word_dics=business_word_dics,
                stop_word_dics=stop_word_dics).segment(corpus=corpus)

        self.logger.debug("corpus => [{0}]".format(", ".join(corpus)))

        sentences = [row.split()
                     for row in Utils.get_resources_contents(corpus)]
        model = gensim.models.word2vec.Word2Vec(
            sentences, sg=0, hs=1, size=size, workers=workers,
            window=window, min_count=min_count, **kwargs)

        if save_model_path is not None:
            if os.path.isfile(save_model_path):
                os.unlink(save_model_path)

            model.save(save_model_path)

        return model

    def large_train(self, corpus, is_segment=False,
                    business_word_dics=None, stop_word_dics=None,
                    save_model_path=None, size=500, window=5, min_count=10,
                    workers=1, batch_size=1000000, **kwargs):
        if save_model_path is None:
            raise Exception(
                "save_model_path [{0}] is not exists.".format(save_model_path))

        self.logger.debug("corpus => [{0}]".format(", ".join(corpus)))
        f, i = open(corpus), 1
        _jieba = JiebaParticiple(
            business_word_dics=business_word_dics,
            stop_word_dics=stop_word_dics)
        model = gensim.models.word2vec.Word2Vec(
            sg=0, hs=1, size=size, workers=workers,
            window=window, min_count=min_count, **kwargs)
        model.build_vocab([[""]])
        while True:
            self.logger.debug(
                "Process Line: {0} To {1}".format(i, i + batch_size))
            lines = f.readlines(batch_size)
            if not lines:
                break
            else:
                sentences = _jieba.segment(lines)
                model.build_vocab(
                    [sentence.split() for sentence in sentences],
                    update=True)
                model.train(
                    sentences,
                    epochs=model.iter,
                    total_examples=model.corpus_count)
                model.save(save_model_path)

            i += batch_size

        return model

    def load(self, model):
        if not os.path.isfile(model):
            raise Exception("Model Path [{0}] is Not Found.".format(model))

        return gensim.models.Word2Vec.load(model)
