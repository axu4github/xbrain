# coding=utf-8

from xbrain.similarity import Word2VectorSimilarity
from xbrain.configs import Config

import json
import os


class TestWord2VectorSimilarity(object):
    """ 测试词向量的相似度 """

    @classmethod
    def setup_class(cls):
        cls.business_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "words.dic")
        cls.stop_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "stopwords.dic")
        cls.corpus = os.path.join(
            Config.TEST_CORPUS_DIR, "sentences.txt")

    def test_most_similar(self, app):
        with app.app_context():
            words = ["分词", "拉丁语", "中国"]
            similars = Word2VectorSimilarity(
                self.corpus, is_segment=True, min_count=1).most_similar(words)

            assert similars["中国"] == []


class TestWord2VectorSimilarityApi(object):
    """ 测试词向量的相似度接口 """

    @classmethod
    def setup_class(cls):
        cls.business_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "words.dic")
        cls.stop_word_dics = os.path.join(
            Config.TEST_DICS_DIR, "stopwords.dic")
        cls.corpus = os.path.join(
            Config.TEST_CORPUS_DIR, "sentences.txt")

    def test_similarity(self, client):
        response = client.post(
            "/apis/similar",
            data=dict(corpus=self.corpus, is_segment=1, words="分词,拉丁语,中国"))
        response_data = json.loads(response.data)

        assert response_data["status"] == 0
        assert response_data["response"]["中国"] == []
