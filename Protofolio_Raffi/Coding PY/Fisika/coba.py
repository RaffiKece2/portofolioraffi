
import wikipedia
from gtts import gTTS
import os
import pygame
import time

wikipedia.set_lang("id")
user = input("Search: ")


jawaban = wikipedia.summary(user, sentences = 50)

print(jawaban)
tts = gTTS(text= jawaban, lang= "id")
tts.save("voice.mp3")
pygame.mixer.init()
pygame.mixer.music.load("voice.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)



