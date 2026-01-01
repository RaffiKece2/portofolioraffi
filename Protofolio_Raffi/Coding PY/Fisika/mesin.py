from gtts import gTTS
import os
import pygame
import time



text = "halo saya raffi virtual"

tts = gTTS(text= text, lang= "id")


tts.save("suara.mp3")

pygame.mixer.init()
pygame.mixer.music.load("suara.mp3")
pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    time.sleep(0.1)
    
