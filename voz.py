import speech_recognition as sr
import time
r = sr.Recognizer()
mic = sr.Microphone()
print("Grabando")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
print("Terminamos")
print(r.recognize_google(audio,language='es'))