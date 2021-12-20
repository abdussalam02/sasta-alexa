# Importing all the required modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia as wk
import pyjokes

# defining variables
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)