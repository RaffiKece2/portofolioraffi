from gtts import gTTS
import os
import pygame
import time

import google.generativeai as genai

genai.configure(api_key="AIzaSyBql19RKaa2T0Om44nrFnCSZbo_zqNfzQQ")

model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Jelaskan apa itu kecerdasan buatan dalam bahasa sederhana."
response = model.generate_content(prompt)
pygame.mixer.init()

while True:
    user_input = input("Kamu: ")
    if user_input.lower() == "exit":
        break
    
    
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    

    pygame.mixer.music.stop()
    time.sleep(0.2)
    pygame.mixer.music.unload()
  
    
    
    
    response = model.generate_content(user_input)
    print("Gemini:", response.text)
    
    
    try:
        
        tts = gTTS(text= response.text, lang= "id")
    
        tts.save("virtual.mp3")
        pygame.mixer.music.load("virtual.mp3")
        pygame.mixer.music.play()
        
    except PermissionError:
        print("maaf saya masih bebicara!!")
        time.sleep(1)


