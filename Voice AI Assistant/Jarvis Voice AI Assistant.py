import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=9 and hour<12:
        print("Good Night")
        speak("Good Night")
    elif hour>=12 and hour<4:
        print("Midnight")
        speak("Midnight")
    elif hour>=4 and hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=13 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    elif hour>=18 and hour<21:
        print("Good evening")
        speak("Good evening")

    print("I am Jarvis Sir. Please tell me how may i help you")
    speak("I am Jarvis Sir. Please tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-bd')
        print(f"User said: {query}\n")
        #speak(query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("biswasshuvo851@gmail.com","123456789GETONTHE") #Must turn on less secure access apps in google account
    server.sendmail('biswasshuvo851@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    dict = {"jarvis":"hossaint216@gmail.com"}
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            print("Searching wikipedia....")
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            print("Opening Stackoverflow....")
            speak("Opening Stackoverflow....")
            webbrowser.open("stackoverflow.com")

        elif 'play movie' in query:
            movie_dir = "D:\\War 2019.Hindi.Bluray.1080p.DD.5.1.HEVC-DDR"
            movies = os.listdir(movie_dir)
            print("Playing movie...")
            speak("Playing movie...")
            print(movies)
            os.startfile(os.path.join(movie_dir,movies[random.randint(0,len(movies)-1)]))
        elif 'play music' in query:
            song_dir = "F:\\Music"
            songs = os.listdir(song_dir)
            print("Playing music...")
            speak("Playing music...")
            print(songs)
            os.startfile(os.path.join(song_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strtime}")
            speak(f"The time is {strtime}")

        elif 'open firefox' in query:
            pypath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            print("Opening Mozilla Firefox")
            speak("Opening Mozilla Firefox")
            os.startfile(pypath)

        elif 'send email' in query:
            print("Whom do you want to send the email?")
            speak("Whom do you want to send the email?")
            take = takecommand().lower()
            if take in dict:
                try:
                    print("What should i say?")
                    speak("What should i say?")
                    content = takecommand()
                    to = dict[take]
                    sendmail(to,content)
                    print("Email has been successfully sent")
                    speak("Email has been successfully sent")
                except Exception as e:
                    print("Sorry Sir. I am not be able to sent the email")
                    speak("Sorry Sir. I am not be able to sent the email")
            else:
                print("Sorry Sir. Email not existed")
                speak("Sorry Sir. Email not existed")


        elif 'quit' in query:
            print("Quiting... Thank you for giving your time")
            speak("Quiting... Thank you for giving your time")
            exit()