import re
import collections
import nltk
import jieba
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = 'Arial Unicode MS'


def load_book(filename):
    f = open(filename,'r')
    book = f.read()
    f.close()
    return book

def load_stop_words(stop_words_file):
    stop_words = []
    with open(stop_words_file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            stop_words.append(line)
    return stop_words

def count_freq(words, n=None, stop_words=None):
    freq = collections.Counter([w for w in words])
    cnt = []
    words = []
    for key, value in freq.most_common():
        # print(key, ':', value)
        if stop_words and key in stop_words:
            continue
        words.append(key)
        cnt.append(value)
        if(n and len(words) == n):
            break
    return words, cnt

def clean_zh_corpus(corpus):
    rule = re.compile(r'[^\u4e00-\u9fa5]') # 去除汉字以外的所有字符，包括标点、英文字母等
    s = rule.sub('', corpus)
    return s

def cut_word(text):
    jieba_list = list(jieba.cut(text, cut_all=False))
    jieba_txt = ' '.join(jieba_list)
    return jieba_txt, jieba_list

def plot_freq(words, freq):
    plt.figure(figsize=(12, 9), dpi=300)
    plt.plot(words, freq)
    plt.xticks(fontsize=13, rotation=90)
    plt.xlabel('Words', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.show()

if __name__ == '__main__':
    filename = '诛仙.txt'
    book = load_book(filename)
    book = clean_zh_corpus(corpus=book)
    text, words = cut_word(text=book)
    # print(words[:1000])
    stop_words_file = '停用词表.txt'
    stop_words = load_stop_words(stop_words_file=stop_words_file)
    words, freq = count_freq(words=words, n=50, stop_words=stop_words)
    plot_freq(words=words, freq=freq) # 画出单词-频率图


