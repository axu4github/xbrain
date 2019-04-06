# coding=utf-8

from xbrain.core.word2vectors import GensimWord2Vector
from xbrain.core.participles import JiebaParticiple
from xbrain.configs import Config
from xbrain.doraemon import Doraemon
from xbrain.utils import Utils

import random
import os


class TestGensimWord2Vector(object):
    """ 测试 Gensim 词向量"""

    @classmethod
    def setup_class(cls):
        cls.business_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "words.dic")
        cls.stop_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "stopwords.dic")
        cls.corpus = os.path.join(
            Config.TEST_CORPUS_DIR, "sentences.txt")
        cls.save_model = os.path.join(
            Config.TEST_MODELS_DIR, "w2v.model")

    def test_train_large_model(self, app):
        with app.app_context():
            model = GensimWord2Vector().large_train(
                self.corpus, min_count=1, batch_size=2,
                save_model_path=self.save_model, is_segment=True)

            assert "复合时态" in model.wv.vocab

            if os.path.isfile(self.save_model):
                os.unlink(self.save_model)

    def test_train_model_is_not_segment(self, app):
        with app.app_context():
            corpus = JiebaParticiple().segment(corpus=self.corpus)

            assert os.path.isfile(corpus[0])

            model = GensimWord2Vector().train(corpus, min_count=1)

            assert len(model.wv.vocab) == len(
                list(set(
                    "\n".join(Doraemon.get_file_contents(corpus[0])).split())))

            os.unlink(corpus[0])

            assert not os.path.isfile(corpus[0])

    def test_train_model_is_segment(self, app):
        with app.app_context():
            model = GensimWord2Vector().train(
                self.corpus, is_segment=True, min_count=1)

            assert "分词" in model.wv.vocab

            os.unlink(Utils.get_segmented_filepath(self.corpus))

    def test_train_model_segment_business_word_dics(self, app):
        with app.app_context():
            model = GensimWord2Vector().train(
                self.corpus, is_segment=True, min_count=1,
                business_word_dics=self.business_word_dics)

            assert "复合时态" in model.wv.vocab

            os.unlink(Utils.get_segmented_filepath(self.corpus))

    def test_train_model_segment_stop_word_dics(self, app):
        with app.app_context():
            model = GensimWord2Vector().train(
                self.corpus, is_segment=True, min_count=1,
                stop_word_dics=self.stop_word_dics)

            assert "在" not in model.wv.vocab

            os.unlink(Utils.get_segmented_filepath(self.corpus))

    def test_train_model_save_model(self, app):
        with app.app_context():
            model_filepath = os.path.join(
                Config.TEST_MODELS_DIR,
                "word2vecs",
                "{0}.model".format(random.random()))

            assert not os.path.isfile(model_filepath)

            GensimWord2Vector().train(
                self.corpus, is_segment=True, min_count=1,
                save_model_path=model_filepath)

            assert os.path.isfile(model_filepath)

            os.unlink(model_filepath)
            os.unlink(Utils.get_segmented_filepath(self.corpus))

    def test_load_model(self, app):
        with app.app_context():
            model_filepath = os.path.join(
                Config.TEST_MODELS_DIR,
                "word2vecs",
                "{0}.model".format(random.random()))
            word = "分词"

            assert not os.path.isfile(model_filepath)

            _gensim = GensimWord2Vector()
            before_model = _gensim.train(
                self.corpus, is_segment=True, min_count=1,
                save_model_path=model_filepath)

            assert word in before_model.wv.vocab
            assert os.path.isfile(model_filepath)

            after_model = _gensim.load(model_filepath)

            assert word in after_model.wv.vocab
            assert before_model.wv.most_similar(
                word) == after_model.wv.most_similar(word)

            os.unlink(model_filepath)
            os.unlink(Utils.get_segmented_filepath(self.corpus))
