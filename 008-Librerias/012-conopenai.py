from gtts import gTTS
import pygame
import os
import time
import speech_recognition as sr
from openai import OpenAI

r = sr.Recognizer()
client = OpenAI()

def mi_openai(entrada):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
           
            {
                "role": "user",
                "content": entrada
            }
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1
    )
    message_content = response.choices[0].message.content
    return message_content

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
            respuesta = mi_openai(text)
            text_to_speech(respuesta, lang='es')
        except sr.UnknownValueError:
            print("e1")
        except sr.RequestError:
            print("e2")
