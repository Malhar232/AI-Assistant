import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser as web
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is mojo and I'm your assistant! How may I help you?")

def tasks():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"Your Request : {query}")
    except Exception as e:
        # print(e)
        print("Sorry! Didn't catch that.. Say that again please.")
        return "None"
    return query

def send_email(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("deshkarmm@rknec.edu","Malhar232*")
    server.sendmail("deshkarmm@rknec.edu",to,content)
    server.close()

if __name__=="__main__":
    wish()
    
while True:
    query=tasks().lower()
    if "on wikipedia" in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia","")
        summary=wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)

    elif "open google" in query:
        speak("Starting Google...")
        web.open("google.com")
        
    elif "on youtube" in query:
        
        speak("Starting Youtube...")
        query=query.replace("on youtube","")
        query=query.replace("search","")
        query=query.replace(" ","")

        web.open(f"https://www.youtube.com/{query}")

    elif "on google" in query:
        speak("Searching...")
        query=query.replace("search","")
        query=query.replace("on google","")
        web.open(f"https://www.google.com/search?q={query}")
    
    elif "the time"  in query:
        
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is : {strtime}")
        speak(f"The time is : {strtime}")
    
    elif  "open vs code" in query:
        
        speak("Opening VS Code...")
        code_path="C:\\Users\\malha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif "play music" in query:
        speak("Playing songs...")
        music_dir="C:\\Users\\malha\\Desktop\\music"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif "send email" in query:
        try:
            speak("To whom?")
            rec=input()
            to=rec.replace(" ","")
            
            speak("What should I write?")
            content=tasks()
            send_email(to,content)
            speak("Email Sent!")
        except Exception as e:
            speak("Sorry Cannot send your email!")
    
    elif "exit" in query:
        speak("It was a pleasure meeting you! bye bye!")
        break