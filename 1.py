from email.mime import audio
import pyttsx3
from setuptools import Command
import speech_recognition as sr
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print("   ")
    Assistant.runAndWait()

def takeCommand():
    Command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning......")
        Command.pause_threshold = 1
        audio=Command.listen(source)

        try:
            print("Recognizing")
            query = Command.recognize_google(audio,language='en-in')
            print(f"You said : {query}" )

        except Exception as Error:
            return "none"

            return query.low


