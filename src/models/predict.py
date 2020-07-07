from src.features.dictionary import create_dictionary, term_document_matrix
from src.features.tokenize import tokenize_bigrams,tokenize_trigrams
from gensim.test.utils import datapath
import os
import gensim
from pprint import pprint

#Funcion para predecir un topic basado en un review
def predict(sentence : str, bigrams: bool = True):
    list_of_sentences = []
    list_of_sentences.append(sentence)
    if bigrams:
        dw = tokenize_bigrams(list_of_sentences)
    else:
        dw = tokenize_trigrams(list_of_sentences)
    if len(dw):
        id2word = create_dictionary(dw)
        print("Generando el corpus...")
        corpus = term_document_matrix(dw,id2word)
        print("Obteniendo el modelo LDA...")
        basePath = os.path.dirname(os.path.abspath(__file__))
        lda_model_file = datapath(basePath+"/../../models/lda_model")
        lda_model = gensim.models.ldamodel.LdaModel.load(lda_model_file)
        topic_r = -1
        p_topic = 0
        for topic in lda_model.get_document_topics(corpus)[0]:
            if topic[1] > p_topic:
                p_topic = topic[1]
                topic_r = topic[0]
        return 'Esta frase pertenece al tema no. '+str(topic_r)
    else:
        return 'Lo sentimos. La frase ingresada no se logró tokenizar. Por lo tanto, no se realizó la predicción.'