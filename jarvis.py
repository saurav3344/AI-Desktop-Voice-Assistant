import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Jarvis sir.Please tell me how may i help you")

def takeCommand():
# it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognition..")
        query = r.recognize_google(audio, Language='en')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server.ehlo
    server = smtplib.SMTP('smtp.gmailcom',587)
    server.starttls
    server.login('saurav334455@gmail.com','sam,./123')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # logic for executing tasks based on query
    if "wikipedia" in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    
    elif 'play music' in query:
        music_dir = "F:\\jarvis\\song"
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
    
    elif 'open code' in query:
        codePath = "C:\\Users\\SAURAV-PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif 'email to saurav' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "saurav123gautam@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!!")

        except Exception as e:
            print(e)
        speak("Sorry my friend saurav bro. I am not able to send this mail")