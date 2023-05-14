import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') 
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
def wishme():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("good morning!")
   elif hour>=12 and hour<18:
      speak("good afternoon")  
   else:
      speak("good evening!")

   speak(" How may i help you  ")

def takecommand():
   
   # it takes microphone input from the user and return string output
   r = sr.Recognizer()
   with sr.Microphone()as source:
      print("listening....")
      r.pause_threshold = 1
      audio = r.listen(source)

   try: 
       print("recognizing....")   
       query = r.recognize_google(audio, language='en-in')
       print(f"User said:{query}\n")


   except Exception as e:
      print("Say that again please")
      speak("Say that again please")
      return "None"
   return query 

if __name__ == "__main__":
   wishme()
   while True:
      query = takecommand().lower()
      #Logic for executing tasks based on query

      if 'Wikipedia' in query:
        speak('searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)  


      elif'open youtube' in query:
         speak('searching Youtube...')
         webbrowser.open("youtube.com")

      elif'open google' in query:
         speak('searching google...')
         webbrowser.open("google.com")

      elif'open kite' in query:
         speak('searching from google...')
         webbrowser.open("kite.zerodha.com")

      elif 'show me  time 'in query:
         strtime = datetime.datetime.now().strftime("%H:%M:%S")
         speak('time is...')
         speak(f"sir, The time is{strtime} ")
         print(f"sir, The time is{strtime} ")

      elif'open code'in query:
         codepath ="C:\\Users\\athar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)
      