import datetime
import webbrowser
import os
import subprocess as sp
import pyjokes
import pyttsx3
import pywhatkit as kit
import pywhatkit
import speech_recognition as sr
import requests
import wikipedia
from email.message import EmailMessage
import smtplib
from decouple import config

paths = {
    'vscode': "C:\\Users\\Rahul Raj Mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'stopwatch': "C:\\Program Files (x86)\\FreeStopwatch\\FreeStopwatch.exe"

}

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")
    talk('Hello sir This is your Jarvis Assistant, How may I help you')

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('smartrahulmishra1999@gmail.com','9919095214Rahul@')
    server.sendmail('smartrahulmishra1999@gmail.com', to, content)
    server.close()
def get_trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key=2beb9587e05e0fbbee2af1bf375fbbaa").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]


def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=117b1efc36ea4319839631e83c90d06c&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=648f40aa45d29b58ba3827f22b035b77&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def open_calculator():
    sp.Popen(paths['calculator'])
def open_stopwatch():
    os.startfile(paths['stopwatch'])

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
if __name__ == "__main__":
    wishMe()
def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('just a second sir')
        talk('playing ' + song+'on youtube')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        talk('just a second sir')
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is my ip' in command:
        talk('just a second sir')
        talk('your IP address is: '+find_my_ip())
        print('Your IP address is : '+find_my_ip())
    elif 'date' in command:
        date = datetime.datetime.date()
        talk('Date is' + date)
    elif 'who is' in command:
        talk('just a second sir')
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open youtube' in command:
        talk('just a second sir')
        webbrowser.open("youtube.com")
        talk('opening youtube')
    elif 'open camera' in command:
        talk('just a second sir')
        sp.run("start microsoft.windows.camera:", shell=True)
        talk('opening camera')
    elif 'open calculator' in command:
        talk('just a second sir')
        sp.Popen(paths['calculator'])
        talk('opening calculator')
    elif 'open stopwatch' in command:
        os.startfile(paths['stopwatch'])
        talk('opening stopwatch')
    elif 'open vs code' in command:
        os.startfile(paths['vscode'])
        talk('opening vs code')
    elif 'open cmd' in command:
        os.system('start cmd')
        talk('opening cmd')
    elif 'open instagram' in command:
        talk('just a second sir')
        webbrowser.open("instagram.com")
        talk('opening instagram sir')
    elif 'open google' in command:
        webbrowser.open("google.com")
        talk('opening google sir')
    elif 'where is' in command:
        talk('just a second sir')
        person = command.replace('where is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        talk('just a second sir')
        person = command.replace('what is', ' ')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is your name' in command:
        talk('My name is Jarvis Assistant')
    elif 'who developed you' in command:
        talk('I am Developed by Rahul,Lakshay and vernit')
    elif 'show my location' in command:
        talk('you are currently at zero pusta road,shastri park ,New Delhi')
    elif 'which college i am in' in command:
        talk('i dont know')
    elif "trending movies" in command:
        talk('just a second sir')
        talk(f"Some of the trending movies are: {get_trending_movies()}")
        talk("For your convenience, I am printing it on the screen sir.")
        print(*get_trending_movies(), sep='\n')
    elif 'joke' in command:
        talk(f"Hope you like this one sir")
        joke = get_random_joke()
        talk(joke)
        talk("For your convenience, I am printing it on the screen sir.")
        print(joke)
    elif "advice" in command:
        talk(f"Here's an advice for you, sir")
        advice = get_random_advice()
        talk(advice)
        talk("For your convenience, I am printing it on the screen sir.")
        print(advice)

    elif "send whatsapp message" in command:
        talk('just a second sir')
        talk('On what number should I send the message sir? Please enter in the console: ')
        number = input("Enter the number: ")
        talk("What is the message sir?")
        message = take_user_input().lower()
        send_whatsapp_message(number, message)
        talk("I've sent the message sir.")
    elif 'send email' in command:
        try:
            talk("What should I say?")
            content =take_command()
            to = "vennitvaid@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my friend harry bhai. I am not able to send this email")
    elif 'tell me the weather outside' in command:
        talk('just a second sir')
        ip_address = find_my_ip()
        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        talk(f"Getting weather report for your city {city}")
        weather, temperature, feels_like = get_weather_report(city)
        talk(f"The current temperature is {temperature}, but it feels like {feels_like}")
        talk(f"Also, the weather report talks about {weather}")
        talk("For your convenience, I am printing it on the screen sir.")
        print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
    elif 'news' in command:
        talk('just a second sir')
        talk(f"I'm reading out the latest news headlines, sir")
        talk(get_latest_news())
        talk("For your convenience, I am printing it on the screen sir.")
        print(*get_latest_news(),  sep='\n')
    elif 'stop' in command:
        talk('bye sir have a great day')
        quit()

    else:
        talk('Please say the command again.')


while True:
    run_jarvis()
