import re
import nltk
import jieba
import collections
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer


def get_corpus_filename():
    doc = nltk.corpus.gutenberg.fileids()
    docs = []
    for d in doc:
        docs.append(d)
    return docs

def load_stop_words(stop_words_file):
    stop_words = []
    with open(stop_words_file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            stop_words.append(line)
    return stop_words

def load_book(filename):
    f = open(filename,'r')
    book = f.read()
    f.close()
    return book

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN

def clean_zh_corpus(corpus):
    rule = re.compile(r'[^\u4e00-\u9fa5]') # 去除汉字以外的所有字符，包括标点、英文字母等
    s = rule.sub('', corpus)
    return s

def clean_en_corpus(corpus):
    wnl = WordNetLemmatizer()
    pat_letter = re.compile(r'[^a-zA-Z \']+')
    new_text = pat_letter.sub(' ', corpus).strip().lower()
    new_words = new_text.split()
    new_num = len(new_words)
    tag = nltk.pos_tag(new_words)
    # print(tag[:10])
    for i in range(new_num):
        pos = get_wordnet_pos(tag[i][1])
        new_words[i] = wnl.lemmatize(word=new_words[i], pos=pos)
    return new_text, new_words

def cut_word(text):
    jieba_list = list(jieba.cut(text, cut_all=False))
    jieba_txt = ' '.join(jieba_list)
    return jieba_txt, jieba_list

def count_freq(words, n=None, stop_words=None):
    freq = collections.Counter([w for w in words])
    cnt = []
    words = []
    if stop_words:
        for key, value in freq.most_common():
            # print(key, ':', value)
            if key in stop_words:
                continue
            words.append(key)
            cnt.append(value)
            if(n and len(words) == n):
                break
    else:
        for key, value in freq.most_common(n):
            # print(key, ':', value)
            words.append(key)
            cnt.append(value)
    return words, cnt

def plot_freq(words, freq, label_fs=14, ticks_fs=12):
    plt.rcParams["font.family"] = 'Arial Unicode MS'
    plt.figure(figsize=(12, 9), dpi=300)
    plt.plot(words, freq)
    plt.xticks(fontsize=ticks_fs, rotation=90)
    plt.xlabel('Words', fontsize=label_fs)
    plt.ylabel('Frequency', fontsize=label_fs)
    plt.show()
