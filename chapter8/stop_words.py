# -*- coding:utf-8 -*-

def read_stopwords():
    return [line.strip() for line in open('English.txt').readlines()]

def is_stopword(word, stop_words):
    return word in stop_words
