import speech_recognition as sr
import wikipedia
import pywhatkit
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(command):
  engine.say(command)
  engine.runAndWait()

def commands():

  try:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source)
      print('listening  madorchod')
      audioin = r.listen(source)
      my_text =r.recognize_google(audioin)
      my_text = my_text.lower()
      print(my_text)
      speak(my_text)

  except:
    print("404")  

commands()      




