import requests
import wikipedia
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime

waktu = datetime.now()

wikipedia.set_lang("id")



class Jarvis:
    def __init__(self):
        self.text = []
        self.label = []
    
    
        