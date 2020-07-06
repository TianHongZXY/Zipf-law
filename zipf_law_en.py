import re
import nltk
import collections
import matplotlib.pyplot as plt
from nltk.corpus import  gutenberg
from nltk.stem import WordNetLemmatizer

def get_corpus_filename():
    doc = nltk.corpus.gutenberg.fileids()
    docs = []
    for d in doc:
        docs.append(d)
    return docs

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

def clean_corpus(corpus):
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

def plot_freq(words, freq):
    plt.plot(words, freq)
    plt.xticks(rotation=90)
    plt.xlabel('Words', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.show()


if __name__ == '__main__':
    wnl = WordNetLemmatizer()
    corpus = gutenberg.raw()
    _, words = clean_corpus(corpus=corpus)
    stop_words_file = '停用词表.txt'
    stop_words = load_stop_words(stop_words_file=stop_words_file)
    words, freq = count_freq(words=words, n=50, stop_words=stop_words)  # 统计频率，返回最高的50个单词及频率
    # print('一共有', len(words), '个单词')
    plot_freq(words=words, freq=freq) # 画出单词-频率图


