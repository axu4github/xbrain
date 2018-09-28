# coding=utf-8

from xbrain.loggings import LoggableMixin
from xbrain.utils import Utils
from xbrain.doraemon import Doraemon
from collections import defaultdict

import jieba


class Participles(LoggableMixin):
    """ 分词 """

    def __init__(self,
                 business_words_dir=None,
                 stop_words_dir=None,
                 *args, **kwargs):
        super(Participles, self).__init__(*args, **kwargs)

        self.business_words = self.init_dic_words(business_words_dir)
        self.stop_words = self.init_dic_words(stop_words_dir)

    def init_dic_words(self, words_dir):
        dic_words = defaultdict(int)
        if words_dir is not None:
            for word in Utils.get_files_contents(words_dir):
                dic_words[word] += 1

        return dic_words

    def append_business_words(self, business_words):
        pass

    def filter_stop_words(self, sentences):
        return filter(lambda word: word not in self.stop_words, sentences)

    def perform_cut(self, sentences):
        pass

    def perform_cut_file(self, _file, output_file=None):
        cuted = []
        for line in Doraemon.get_file_contents(_file):
            cuted.append(" ".join(
                self.filter_stop_words(self.perform_cut(line))))

        if output_file is not None:
            Doraemon.put_file_contents(output_file, cuted)

        return cuted

    def cut(self, sentences=None, corpus=None):
        cuted = []
        self.append_business_words(self.business_words.keys())
        if sentences is not None:
            if not isinstance(sentences, list):
                sentences = [sentences]

            for sentence in sentences:
                cuted.append(" ".join(
                    self.filter_stop_words(self.perform_cut(sentence))))
        elif corpus is not None:
            if not isinstance(corpus, list):
                corpus = [corpus]

            for corpus_dir in corpus:
                for _file in Doraemon.get_files(corpus_dir):
                    output_file = "{0}.cuted".format(_file)
                    self.perform_cut_file(_file, output_file)
                    cuted.append(output_file)

        return cuted


class JiebaParticiple(Participles):
    """ 结巴分词 """

    def __init__(self, *args, **kwargs):
        super(JiebaParticiple, self).__init__(*args, **kwargs)

    def append_business_words(self, business_words):
        for word in business_words:
            jieba.add_word(word)

    def perform_cut(self, sentences):
        return jieba.cut(sentences.strip(), cut_all=False)
