import argparse
from utils import load_stop_words, load_book, plot_freq, cut_word, clean_zh_corpus, count_freq

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--zh_corpus', default="诛仙.txt", type=str)
    parser.add_argument('--stop_words', default='停用词表.txt', type=str)
    args = parser.parse_known_args()[0]
    zh_corpus = args.zh_corpus
    stop_words_file = args.stop_words

    book = load_book(zh_corpus)
    book = clean_zh_corpus(corpus=book)
    text, words = cut_word(text=book)
    stop_words = load_stop_words(stop_words_file=stop_words_file)
    words, freq = count_freq(words=words, n=50, stop_words=stop_words)
    plot_freq(words=words, freq=freq, label_fs=14, ticks_fs=13) # 画出单词-频率图


