#pip install gtts
#pip install pygame

from gtts import gTTS
import pygame
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.remove(audio_file)

text = "Hello, how are you doing today?"
text_to_speech(text)
