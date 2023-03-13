#This is a software which is similar to alexa

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import requests
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def weather(city):
    api_key = "<YOUR API KEY>"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))


def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak Now...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'name' in command:
        talk('my name is alexa')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    #elif 'who the heck is' in command:
        #person = command.replace('who the heck is', '')
        #info = wikipedia.summary(person, 1)
        #print(info)
        #Talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'weather' in command:
        #engine_talk('Please tell name of the city')
        city = 'Hong Kong'
        #city = 'Mumbai'
        talk('The temperature in Hong Kong is' + weather(city) + 'degree celcius')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()