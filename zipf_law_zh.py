import re
import nltk
import jieba
import matplotlib.pyplot as plt
from zipf_law_en import count_freq, plot_freq, load_stop_words
plt.rcParams["font.family"] = 'Arial Unicode MS'


def load_book(filename):
    f = open(filename,'r', encoding='gb18030')
    book = f.read()
    f.close()
    return book

def clean_zh_corpus(corpus):
    rule = re.compile(r'[^\u4e00-\u9fa5]') # 去除汉字以外的所有字符，包括标点、英文字母等
    # rule = re.compile(u'[^a-zA-Z.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：' + digits + punctuation + '\u4e00-\u9fa5]+')
    s = rule.sub('', corpus)
    return s

def cut_word(text):
    jieba_list = list(jieba.cut(text, cut_all=False))
    jieba_txt = ' '.join(jieba_list)
    return jieba_txt, jieba_list


if __name__ == '__main__':
    filename = '毛泽东文选.txt'
    book = load_book(filename)
    book = clean_zh_corpus(corpus=book)
    text, words = cut_word(text=book)
    # print(words[:1000])
    stop_words_file = '停用词表.txt'
    stop_words = load_stop_words(stop_words_file=stop_words_file)
    words, freq = count_freq(words=words, n=50, stop_words=stop_words)
    plot_freq(words=words, freq=freq) # 画出单词-频率图


