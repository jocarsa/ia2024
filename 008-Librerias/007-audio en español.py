#pip install gtts
#pip install pygame

from gtts import gTTS
import pygame
import os
import time

def text_to_speech(text, lang='es'):
    epoch = time.time()
    tts = gTTS(text=text, lang=lang)
    audio_file = "audiotemp/"+str(epoch)+".mp3"
    tts.save(audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    try:
        os.remove(audio_file)
    except:
        pass

text = "Hola, ¿como estás?"
text_to_speech(text)
text = "Este es un segundo texto"
text_to_speech(text)
