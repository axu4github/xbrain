# coding=utf-8

from xbrain.core.participles import JiebaParticiple
from xbrain.doraemon import Doraemon
from xbrain.configs import Config

import os


class TestJiebaParticiple(object):

    @classmethod
    def setup_class(cls):
        cls.business_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "words.dic")
        cls.stop_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "stopwords.dic")
        cls.corpus = os.path.join(
            Config.TEST_CORPUS_DIR, "sentences.txt")

    def test_jieba_participle_perform_segment_empty(self, app):
        with app.app_context():
            _jieba = JiebaParticiple()

            assert "".join(_jieba.perform_segment("\n")) == ""

    def test_jieba_participle_perform_segment(self, app):
        with app.app_context():
            sentence = Doraemon.get_file_contents(self.corpus)[0]

            assert "语言学" in JiebaParticiple().perform_segment(sentence)

    def test_jieba_participle_perform_segment_business_vocabs(self, app):
        with app.app_context():
            sentence = Doraemon.get_file_contents(self.corpus)[0]
            _jieba = JiebaParticiple()

            assert "复合时态" not in _jieba.segment(sentence)[0].split()

            _jieba.set_business_vocabularies(self.business_word_dics)

            assert "复合时态" in _jieba.segment(sentence)[0].split()

    def test_jieba_participle_perform_segment_stopwords_vocabs(self, app):
        with app.app_context():
            sentence = Doraemon.get_file_contents(self.corpus)[0]
            _jieba = JiebaParticiple()

            assert "在" in _jieba.segment(sentence)[0].split()

            _jieba.set_stopword_vocabularies(self.stop_word_dics)

            assert "在" not in _jieba.segment(sentence)[0].split()

    def test_jieba_participle_best_practices(self, app):
        with app.app_context():
            sentence = Doraemon.get_file_contents(self.corpus)[0]
            _jieba = JiebaParticiple(
                business_word_dics=self.business_word_dics,
                stop_word_dics=self.stop_word_dics)
            seged_sentence = _jieba.segment(sentence)[0]

            assert "复合时态" in seged_sentence.split()
            assert "在" not in seged_sentence.split()

    def test_jieba_participle_corpus_file(self, app):
        with app.app_context():
            output_file = "{0}.seged".format(self.corpus)

            assert not os.path.isfile(output_file)

            _jieba = JiebaParticiple(
                business_word_dics=self.business_word_dics,
                stop_word_dics=self.stop_word_dics)
            _jieba.segment(corpus=self.corpus)

            assert os.path.isfile(output_file)

            seged_sentence = "\n".join(Doraemon.get_file_contents(output_file))

            assert "复合时态" in seged_sentence.split()
            assert "在" not in seged_sentence.split()

            os.unlink(output_file)

            assert not os.path.isfile(output_file)

    def test_jieba_participle_corpus_dir(self, app):
        with app.app_context():
            output_file = "{0}.seged".format(self.corpus)

            assert not os.path.isfile(output_file)

            _jieba = JiebaParticiple(
                business_word_dics=self.business_word_dics,
                stop_word_dics=self.stop_word_dics)
            _jieba.segment(corpus=os.path.dirname(self.corpus))

            assert os.path.isfile(output_file)

            seged_sentence = "\n".join(Doraemon.get_file_contents(output_file))

            assert "复合时态" in seged_sentence.split()
            assert "在" not in seged_sentence.split()

            os.unlink(output_file)

            assert not os.path.isfile(output_file)
