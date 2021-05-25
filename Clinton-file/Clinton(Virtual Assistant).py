import pyaudio
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import cv2
import numpy as np
import sample_lib
import pipwin
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen



print('Loading Clinton......')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
        print("Good Evening Sir")

def introduction():
    assname =("Clinton 1 point o")
    speak("I am your Assistant")
    speak(assname)

def usrname():
    speak("What should i call you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        


wishMe()
introduction()



if __name__=='__main__':


    while True:
        usrname()
        response = takeCommand()
        if response==0:
            continue
        speak("How can i Help you Sir!")
        print("How can i Help you Sir!")
        statement = takeCommand().lower()
        if statement==0:
            continue
            

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Clinton is shutting down,Good bye')
            print('Clinton is shutting down,Good bye')
            break
        
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        elif "send message " in statement:
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "don't listen" in statement or "stop listening" in statement:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Clinton version 1 point o your persoanl assistant created by Emmanuel. I am programmed to perform minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from punch and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Emmanuel")
            print("I was built by Emmanuel")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif "who am i" in statement:
            speak("If you talk then definately your human.")

        elif "why you came to this world" in statement:
            speak("Thanks to Emmanuel. further It's a secret")
 
        elif 'power point presentation' in statement:
            speak("opening Power Point presentation")
            power = r"C:\Users\Ebube\Documents\Clinton.pptx"
            os.startfile(power)

        elif 'manual' in statement:
            speak("opening manual")
            manual = r"C:\Users\Ebube\Documents\Start\Clinton's manual.docx"
            os.startfile(manual)

        elif 'open chrome' in statement:
            codePath = r"C:\Users\Ebube\AppData\Local\Programs\Opera\launcher.exe"
            os.startfile(codePath)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://punchng.com/?amp")
            speak('Here are some headlines from Punch,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'change background' in statement:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")

        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in statement:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Clinton.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        

        elif "Clinton" in statement:
             
            wishMe()
            speak("Clinton 1 point o in your service Mister")
            speak(assname)
 

        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
