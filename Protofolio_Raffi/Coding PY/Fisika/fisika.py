import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

with open("catbot.json") as file:
    data = json.load(file)
    

X = []
y = []

for intents in data["intents"]:
    for pattern in intents["pattern"]:
        X.append(pattern)
        y.append(intents["tag"])
        
        
le = CountVectorizer()

data_c = le.fit_transform(X)
data_l = y

model = MultinomialNB()
model.fit(data_c,data_l)


respone = {
    intents["tag"] : intents["respones"]
    for intents in data["intents"]
}



while True:
    user = input("Kamu: ").lower()
    
    if user in ["k"]:
        break
    
    
    user_vec = le.transform([user])
    user_pred = model.predict(user_vec)[0]
    
    respones = random.choice(respone[user_pred])
    print(f"Chatbot: {respones}")


