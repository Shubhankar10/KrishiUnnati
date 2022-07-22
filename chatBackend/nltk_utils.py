import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    #splitting sentence into array of words/tokens
    return nltk.word_tokenize(sentence)


def stem(word):
    #finding the root form of the word
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """"return bag of words array:1 for word that exists in sentence,otherwise 0"""
    # stemming each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initializing bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag