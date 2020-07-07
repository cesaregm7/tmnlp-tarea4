from typing import List
import gensim
from gensim.corpora import Dictionary

#Funcion para crear un diccionario
def create_dictionary(documents: List[List[str]]):
    return Dictionary(documents)

#Funcion para crear el term document matrix
def term_document_matrix(documents, dictionary: Dictionary):
    return [dictionary.doc2bow(text) for text in documents]