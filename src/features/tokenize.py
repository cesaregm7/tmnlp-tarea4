from typing import List

from src.features import nlp
from src.features.utils import clean_data,sent_to_words, remove_stopwords, learn_bigrams, learn_trigrams, make_ngrams, lemmatization

#Funcion para tokenizar mediante bigrams
def tokenize_bigrams(documents: List[str]) -> List[List[str]]:
    document_words = clean_data(documents)
    document_words = list(sent_to_words(document_words))
    document_words = remove_stopwords(document_words)

    #Learn bigrams
    lngram,lngram_mod,document_words_bigrams = make_ngrams(document_words)
    #bigram, document_words_bigrams = learn_bigrams(document_words)

    #Lemmatize bigrams
    document_words_bigrams = lemmatization(nlp, document_words_bigrams)

    return document_words_bigrams

#Funcion para tokenizar mediante trigrams
def tokenize_trigrams(documents: List[str]) -> List[List[str]]:
    document_words = clean_data(documents)
    document_words = list(sent_to_words(document_words))
    document_words = remove_stopwords(document_words)

    #Learn bigrams
    lngram,lngram_mod,document_words_bigrams = make_ngrams(document_words)
    #bigram, document_words_bigrams = learn_bigrams(document_words)

    #Learn trigrams
    lngram,lngram_mod,document_words_trigrams = make_ngrams(document_words,lngram,lngram_mod)
    #document_words_trigrams = learn_trigrams(document_words,bigram)

    #Lemmatize trigrams
    document_words_trigrams = lemmatization(nlp, document_words_trigrams)

    return document_words_trigrams