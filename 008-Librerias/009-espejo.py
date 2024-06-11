from gtts import gTTS
import pygame
import os
import time
import speech_recognition as sr

r = sr.Recognizer()

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

while True:
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source, timeout=5)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio_data, language='es-ES')
            text_to_speech(text, lang='es')
        except sr.UnknownValueError:
            print("e1")
        except sr.RequestError:
            print("e2")
