from src.features.dictionary import create_dictionary, term_document_matrix
from src.features.tokenize import tokenize_bigrams,tokenize_trigrams
from gensim.test.utils import datapath
import os
import gensim

def predict(sentence : str, bigrams: bool = True):
    if bigrams:
        dw = tokenize_bigrams([sentence])
    else:
        dw = tokenize_trigrams([sentence])
    print("Creando el diccionario...")
    id2word = create_dictionary(dw)
    
    print("Generando el corpus...")
    corpus = term_document_matrix(dw,id2word)
    print("Obteniendo el modelo LDA...")
    basePath = os.path.dirname(os.path.abspath(__file__))
    lda_model_file = datapath(basePath+"/../../models/lda_model")
    lda_model = gensim.models.ldamodel.LdaModel.load(lda_model_file)
    topic_r = -1
    p_topic = 0
    for topic in lda_model.get_document_topics(corpus):
        if topic[1] > p_topic:
            p_topic = topic[1]
            topic_r = topic[0]
    return 'Esta frase pertenece al tema no. '+str(topic_r)