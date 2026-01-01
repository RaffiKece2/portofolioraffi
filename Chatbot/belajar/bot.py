import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import wikipedia
from datetime import datetime

jam = datetime.now()

wak = datetime.now().hour


wikipedia.set_lang("id")


with open("catbot.json") as file:
    data = json.load(file)
    
    


text = []
label = []

for intents in data["intents"]:
    for pattern in intents["patterns"]:
        text.append(pattern)
        label.append(intents["tag"])

for command in data["command"]:
    for pattern in command["patterns"]:
        text.append(pattern)
        label.append(command["tag"])
        
for kritikan in data["kritikan"]:
    for pattern in kritikan["patterns"]:
        text.append(pattern)
        label.append(kritikan["tag"])

for pujian in data["saran"]:
    for pattern in pujian["patterns"]:
        text.append(pattern)
        label.append(pujian["tag"])

for waktu in data["jam"]:
    for pattern in waktu["patterns"]:
        text.append(pattern)
        label.append(waktu["tag"])
    
        
le = CountVectorizer()

X = le.fit_transform(text)
y = label

model = MultinomialNB()
model.fit(X,y)




while True:
    user = input("Kamu: ").lower()
    if user in ["k"]:
        break
    
    user_vec = le.transform([user])
    user_pred = model.predict(user_vec)[0]
    
    
    for intenst in data["intents"]:
        if intenst["tag"] == user_pred:
            respone = random.choice(intenst["respones"])
            
    for command in data["command"]:
        if command["tag"] == user_pred:
            wiki_sum = wikipedia.summary(user,sentences = 20 )
            respone = wiki_sum
    
    for kritikan in data["kritikan"]:
        if kritikan["tag"] == user_pred:
            respone = random.choice(kritikan["respones"])
    
    for pujian in data["saran"]:
        if pujian["tag"] == user_pred:
            respone = random.choice(pujian["respones"])
    
    for waktu in data["jam"]:
        if waktu["tag"] == user_pred:
            respone = jam.strftime("%H:%M:%S")

                
                    
                
                    
                
                
                        
    print(f"Chatbot: {respone}")