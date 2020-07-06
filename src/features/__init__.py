import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import spacy

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
nlp = spacy.load('en_core_web_lg', disable=['parser', 'ner'])
