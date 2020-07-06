import gensim
import spacy
import re

from gensim.utils import simple_preprocess
from gensim.models import Phrases
from gensim.models.phrases import Phraser
from langdetect import detect,DetectorFactory

from spacy.lang.en import English

from typing import List

from src.features import stop_words

#Funcion para realizar data cleaning
def clean_data(data : List[str]) -> List:
    # Eliminar emails
    datos = [re.sub(r'\S*@\S*\s?', '', sent) for sent in data]

    # Eliminar newlines
    datos = [re.sub(r'\s+', ' ', sent) for sent in datos]

    # Eliminar comillas
    datos = [re.sub(r"\'", "", sent) for sent in datos]

    # Eliminar datos que no esten en ingles
    DetectorFactory.seed = 0
    datos = [sent for sent in datos if detect(sent)=='en']
    
    return datos

#Convierte un listado de oraciones a un listado que contiene listados de palabras
def sent_to_words(sentences: List) -> List[List[str]]:
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True elimina la puntuación

#Funcion para hacer bigrams
def learn_bigrams(data_words: List[List[str]]):
    bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return bigram,[bigram_mod[doc] for doc in data_words]

#Funcion para hacer trigrams
def learn_trigrams(data_words: List[List[str]],bigram: gensim.interfaces.TransformedCorpus):
    # We learn ngrams
    trigram = gensim.models.Phrases(bigram[data_words], threshold=100) 
    trigram_mod = gensim.models.phrases.Phraser(trigram)
    return [trigram_mod[bigram_mod[doc]] for doc in data_words]

#Funcion para hacer ngrams
def make_ngrams(data_words: List[List[str]],lngram: List[gensim.interfaces.TransformedCorpus] = None, lngram_mod: List[Phraser] = None):
    lngram_result = []
    lngram_mod_result = []
    document_words_ngrams = []
    
    if lngram_mod: #Se haran ngrams
        ngram = gensim.models.Phrases(lngram[-1][data_words], threshold=100) 
        ngram_mod = gensim.models.phrases.Phraser(ngram)
        
        lngram_result = lngram.copy()
        lngram_result.append(ngram)
        
        lngram_mod_result = lngram_mod.copy()
        lngram_mod_result.append(ngram_mod)

        for doc in data_words:
            ngramev = lngram_mod[0][doc]
            for i_ng_mod in range(1,len(lngram_mod)):
                ngramev = lngram_mod[i_ng_mod][ngramev]
            document_words_ngrams.append(ngram_mod[ngramev])
    else: #Se haran bigrams
        bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        
        lngram_result.append(bigram)
        lngram_mod_result.append(bigram_mod)
        document_words_ngrams = [bigram_mod[doc] for doc in data_words]
        
    return lngram_result,lngram_mod_result,document_words_ngrams 

# Eliminar stopwords
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

# Lematización basada en el modelo de POS de Spacy
def lemmatization(nlp: English, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out