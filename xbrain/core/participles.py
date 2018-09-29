# coding=utf-8

from xbrain.loggings import LoggableMixin
from xbrain.utils import Utils
from xbrain.doraemon import Doraemon
from collections import defaultdict

import jieba


class Participles(LoggableMixin):
    """ 分词 """

    def __init__(self, business_word_dics=None, stop_word_dics=None):
        super(Participles, self).__init__()
        self.business_vocabularies = self.generate_vocabularies(
            business_word_dics)
        self.stopword_vocabularies = self.generate_vocabularies(stop_word_dics)

    def generate_vocabularies(self, dicts=None):
        """ 生成词库 """
        vocabularies = defaultdict(int)
        if dicts is not None:
            for word in Utils.get_resources_contents(dicts):
                if word.strip() != "":
                    vocabularies[word.strip()] += 1

        return vocabularies

    def set_business_vocabularies(self, business_word_dics=None):
        self.business_vocabularies = self.generate_vocabularies(
            business_word_dics)

    def set_stopword_vocabularies(self, stop_word_dics=None):
        self.stopword_vocabularies = self.generate_vocabularies(stop_word_dics)

    def add_business_vocabularies(self):
        """ 添加业务词库 """
        pass

    def filter_stopword_vocabularies(self, sentence):
        """ 过滤停用词 """
        def filter_word(word):
            return word.strip() not in self.stopword_vocabularies

        return filter(filter_word, sentence)

    def perform_segment(self, sentences):
        """ 执行句子分词算法 """
        pass

    def perform_segment_file(self, input_filepath, output_filepath=None):
        """ 执行文件分词算法 """
        result = []
        for sentence in Doraemon.get_file_contents(input_filepath):
            if "" != sentence.strip():
                result.append(self.filter_segmented(sentence))

        if output_filepath is not None:
            Doraemon.put_file_contents(output_filepath, result)

        return result

    def filter_segmented(self, sentence):
        """ 过滤分词后的结果 """
        return " ".join(self.filter_stopword_vocabularies(
            self.perform_segment(sentence.strip())))

    def segment(self, sentences=None, corpus=None, output_file=None):
        """ 分词 """
        result = []
        self.add_business_vocabularies()
        if sentences is not None:
            if not isinstance(sentences, list):
                sentences = [sentences]
                self.logger.debug(
                    "sentences => [{0}]".format(", ".join(sentences)))

            for sentence in sentences:
                if "" != sentence.strip():
                    result.append(self.filter_segmented(sentence))

            if output_file is not None:
                Doraemon.put_file_contents(result)
                result = [output_file]
        elif corpus is not None:
            if not isinstance(corpus, list):
                corpus = [corpus]
                self.logger.debug(
                    "corpus => [{0}]".format(", ".join(corpus)))

            for _corpus in corpus:
                for _file in Doraemon.get_files(_corpus):
                    output_file = "{0}.seged".format(_file)
                    self.perform_segment_file(_file, output_file)
                    result.append(output_file)

        self.logger.debug("result => [{0}]".format(", ".join(result)))
        return result


class JiebaParticiple(Participles):
    """ 结巴分词 """

    def __init__(self, *args, **kwargs):
        super(JiebaParticiple, self).__init__(*args, **kwargs)

    def add_business_vocabularies(self):
        for word in self.business_vocabularies.keys():
            jieba.add_word(word)

    def perform_segment(self, sentence):
        return jieba.cut(sentence.strip(), cut_all=False)
