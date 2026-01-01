import requests
import wikipedia
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from datetime import datetime
import json
import random

waktu = datetime.now()

wikipedia.set_lang("id")

with open("chatbot.json") as file:
    data = json.load(file)


model = MultinomialNB()
        
le = CountVectorizer()

class Jarvis:
    def __init__(self):
        self.text = []
        self.label = []
        self.data = data
    
    def prediksi_input(self):
        for intents in self.data["intenst"]:
            for patterns in intents["patterns"]:
                self.text.append(patterns)
                self.label.append(intents["tag"])
        
        for tanya in self.data["tanya"]:
            for patterns in tanya["patterns"]:
                self.text.append(patterns)
                self.label.append(tanya["tag"])
            
        
        X = le.fit_transform(self.text)
        y = self.label
        
        model.fit(X,y)
    
    def prediksi_output(self):
        while True:
            user = input("Kamu: ").lower()
            user_vec = le.transform([user])
            
            user_pred = model.predict(user_vec)[0]
            
            if user in ["k"]:
                break
            
            for intents in self.data["intenst"]:
                if intents["tag"] == user_pred:
                    respone = random.choice(intents["respones"])
            
            for tanya in self.data["tanya"]:
                if tanya['tag'] == user_pred:
                    respone = wikipedia.summary(user,sentences = 500)
                elif tanya['tag'] == user_pred:
                    respone = wikipedia.search(user)
                elif tanya['tag'] == user_pred:
                    page = wikipedia.page(user)
                    respone = page.content
                    print(page.url)
                    
            print(f"ChatBot: {respone}")

jarvis = Jarvis()
jarvis.prediksi_input()
jarvis.prediksi_output()

                
                
        
        
    
        