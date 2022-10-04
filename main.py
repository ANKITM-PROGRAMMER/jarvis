import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
#import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[2].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING , SIR")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON , SIR")
    else:
        speak("GOOD EVENING , SIR")
    speak("I AM JARVIS SIR. PLEASE TELL ME HOW MAY I HELP YOU!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTNING.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("RECOGNISING.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER SAID: {query}\n")
    except Exception as e:
        #print(e)
        print("SAY THAT AGIAN PLEASE........")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ankitmohapatra.programmer@gmail.com','n1z8u8q77')
    server.sendmail('ankitmohapatra.programmer@gmail.com', to, content)


if __name__=="__main__":
    wishMe()
    while True: 
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('SEARCHING WIKIPEDIA.......');
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
            

