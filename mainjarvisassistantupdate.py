import datetime
import webbrowser
import os
import subprocess as sp
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

paths = {
    'vscode': "C:\\Users\\Rahul Raj Mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])


def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.date()
        talk('Date is' + date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
        talk('opening youtube')
    elif 'open camera' in command:
        sp.run("start microsoft.windows.camera:", shell=True)
        talk('opening camera')
    elif 'open calculator' in command:
        sp.Popen(paths['calculator'])
        talk('opening calculator')
    elif 'open vs code' in command:
        os.startfile(paths['vscode'])
        talk('opening vs code')
    elif 'open cmd' in command:
        os.system('start cmd')
        talk('opening cmd')
    elif 'open instagram' in command:
        webbrowser.open("instagram.com")
        talk('opening instagram sir')
    elif 'open google' in command:
        webbrowser.open("google.com")
        talk('opening google sir')
    elif 'where is' in command:
        person = command.replace('where is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is your name' in command:
        talk('My name is Jarvis Assistant')
    elif 'who developed you' in command:
        talk('I am Developed by Rahul,Lakshay and vernit')
    elif 'what is my location' in command:
        talk('you are currently at zero pusta road,shastri park ,New Delhi')
    elif 'which college i am in' in command:
        talk('i dont know')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
