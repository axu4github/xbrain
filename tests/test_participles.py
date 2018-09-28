# coding=utf-8

from xbrain.core.participles import JiebaParticiple
from xbrain.doraemon import Doraemon

business_words_file = "/Users/axu/code/axuProject/xbrain/tests/resources/dics/words.dic"
stop_words_file = "/Users/axu/code/axuProject/xbrain/tests/resources/dics/stop_words.dic"
corpus = "/Users/axu/code/axuProject/xbrain/tests/resources/corpus/sentences.txt"


def test_participle(app):
    with app.app_context():
        participle = JiebaParticiple(
            business_words_dir=business_words_file,
            stop_words_dir=stop_words_file)
        sentences = Doraemon.get_file_contents(corpus)[0]
        print(participle.cut(sentences))
