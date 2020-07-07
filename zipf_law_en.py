from nltk.corpus import gutenberg
from utils import clean_en_corpus, plot_freq, count_freq


if __name__ == '__main__':
    corpus = gutenberg.raw()
    text, words = clean_en_corpus(corpus=corpus)
    words, freq = count_freq(words=words, n=50)  # 统计频率，返回最高的50个单词及频率
    plot_freq(words=words, freq=freq, label_fs=16, ticks_fs=15) # 画出单词-频率图


