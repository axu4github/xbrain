# coding=utf-8

from xbrain.loggings import LoggableMixin
from xbrain.core.participles import JiebaParticiple
from xbrain.utils import Utils
from xbrain.configs import Config

import gensim
import os
import datetime


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
                    save_model_path=Config.DEFAULT_W2V_SAVE_MODEL_PATH,
                    size=Config.DEFAULT_W2V_MODEL_SIZE,
                    window=Config.DEFAULT_W2V_MODEL_WINDOW,
                    min_count=Config.DEFAULT_W2V_MODEL_MIN_COUNT,
                    workers=Config.DEFAULT_W2V_MODEL_WORKER,
                    batch_size=Config.DEFAULT_W2V_MODEL_BATCH_SIZE,
                    **kwargs):
        save_model_dir = os.path.dirname(save_model_path)
        if not os.path.isdir(save_model_dir):
            os.makedirs(save_model_dir)

        self.logger.debug("corpus => [{0}]".format(corpus))
        _jieba = JiebaParticiple(
            business_word_dics=business_word_dics,
            stop_word_dics=stop_word_dics)
        model = gensim.models.word2vec.Word2Vec(
            sg=0, hs=1, size=size, workers=workers,
            window=window, min_count=min_count, **kwargs)
        batch_total, start, lines, i, f = 0, True, [], 1, open(corpus)
        while True:
            line = f.readline()
            if not line and len(lines) == 0:
                break
            else:
                lines.append(line)
                batch_total += 1
                if batch_total == batch_size:
                    self.logger.debug(
                        "Process Line: {0} To {1}".format(i, i + batch_size))

                    segment_start = datetime.datetime.now()
                    sentences = lines
                    if is_segment:
                        sentences = _jieba.large_segment(
                            lines, workers=workers)

                    self.logger.debug(
                        "Segment Spend Time: {0}".format(
                            datetime.datetime.now() - segment_start))

                    build_vocab_start = datetime.datetime.now()
                    w2v_vocab = [sentence.split() for sentence in sentences]
                    if start:
                        model.build_vocab(w2v_vocab)
                    else:
                        model.build_vocab(w2v_vocab, update=True)

                    self.logger.debug(
                        "Build Vocab Spend Time: {0}".format(
                            datetime.datetime.now() - build_vocab_start))

                    model_train_start = datetime.datetime.now()
                    model.train(
                        sentences,
                        epochs=model.iter,
                        total_examples=model.corpus_count)
                    self.logger.debug(
                        "Model Train Spend Time: {0}".format(
                            datetime.datetime.now() - model_train_start))

                    model_save_start = datetime.datetime.now()
                    model.save(save_model_path)
                    self.logger.debug(
                        "Model Save Spend Time: {0}".format(
                            datetime.datetime.now() - model_save_start))

                    batch_total, start, lines = 0, False, []
                    i += batch_size
                    self.logger.debug(
                        "Process Batch Total Spend Time: {0}".format(
                            datetime.datetime.now() - segment_start))

        return model

    def load(self, model):
        if not os.path.isfile(model):
            raise Exception("Model Path [{0}] is Not Found.".format(model))

        return gensim.models.Word2Vec.load(model)
