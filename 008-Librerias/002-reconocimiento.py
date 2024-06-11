import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source, timeout=5)
    print("Recognizing...")
    try:
        text = r.recognize_google(audio_data)
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
