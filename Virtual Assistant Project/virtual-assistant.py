import speech_recognition as sr from gtts
import gTTS import os
from time import sleep
import random
from playsound import playsound
# for wikipedia definitions
import re
import wikipedia
# for weather
import requests
import json
# for time
from datetime import datetime
import wolframalpha

from bs4 import BeautifulSoup

'''
import pyttsx3
voiceEngine = pyttsx3.init() voiceEngine.say('Hello World! This is a speech synthesis test.')
voiceEngine.runAndWait()
'''

# --- functions ---
n = 1


def tts(message):
    global n
    text_to_speech = gTTS(message) filename = str("message" + str(n) + ".mp3") text_to_speech.save(filename) playsound(filename)
    # os.system('mpg123.exe -q message.mp3')
    os.remove(filename)
    print("Alice says: " + message)
    n += 1


r = sr.Recognizer()


def listening_for_commands():
    with sr.Microphone() as source:
        print("\nSay something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        predicted_text = r.recognize_google(audio)
        print("Alice thinks you said: " + predicted_text)
        return predicted_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return "noidea"


def message_checker(message, words):
    words_of_message = message.split()
    if set(words).issubset(set(words_of_message)):
        return True
    else:
        return false


def find_weather():
    api_key = "<api_key>"
    base_url = "http://api.openweathermap.org/data/2.5/weather?" city_name = "<city>" complete_url = base_url + "q=" + city_name + "&APPID=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temp_K = y["temp"]
        current_temp_c = current_temp_K - 273.15
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        tts("Today looks like a " + str(weather_description) + ". The current temperature is " +
            str(round(current_temp_c, 2)) + " degree celsius and the humidity is " + str(current_humidity) + "percent.")
    else:
        tts("I'm sorry. I'm afraid I can't do that at the moment.")


def search_wiki(pred_text):
    words_of_text = pred_text.split()
    words_of_text.remove('define')
    cleaned_text ='join(words_of_text)
    try:
        wiki data = wikipedia.summary(cleaned_text, sentences=3)
        regEx = re.compile(r'([^\(\*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)

        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki data)

        wiki_data = wiki_data.replace("'", "")
        tts(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        tts('Can you please be more specific? You may choose something from the following.')
    print(
        "Can you please be more specific? You may choose something from the following.; {0}".format(e))


def search wolfram(search_query):
    app_id = '888A9Y-E2Q4P887JH' client = wolframalpha.Client(app_id)
    res = client.query(search_query)

    def removeBrackets(variable):
        return variable.split('O[O')


def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable('plaintext']
    # Wolfram cannot resolve the question
    if res['@success'] = 'false':
        print('Question cannot be resolved.')

    # Wolfram was able to resolve question
    else:
        result = ""
        # pod[0] is the question
        pod0 = res['pod'][0]
        # pod[1] may contains the answer
        pod1 = res['pod'][1]
        # checking if podl has primary=true or title=result|definition
        if (('definition' in podl['@title').lower()) or ('result' in pod1['@title').lower()) or (pod1.get('@primary', 'false') == 'true')):
            # extracting result from podl
            result = resolveListOrDict(pod1['subpod'])
            tts(removeBrackets(result))
        else:
            tts("could you repeat the question?")


def read_news():
    ndtv_url = "https: // ndtv.com/latest/'
    r = requests.get(ndtv_url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    headings = soup.find_all('div', attrs={'class': 'nstory_header"})
    count = 1
    for heading in headings:
    if count <= 3:
        tts(heading.text.stripo) count += 1
    else:
        break


# ---- assistant greeting ----
name = "Ashley"
tts("Hi there" + name + ". Nice to meet you. What would you like me to do?")

# -- features added --
# general conversation
# flip coin - " flip a coin"
# telling a joke - "tell me a joke"
# countdown - "give me a countdown"
# lucky number - "what's my lucky number"
# weather - "how's the weather?"
# wikipedia - "define program"
# telling time - "what's the time?"
# wolfram - "how far is the earth from the moon?"
# news - "give me the news headlines"

# --- main loop ---
while True:
    pred_text = listening_for_commands()

    # defining general conversation material
    joke_list = ["What happens to a frog's car when it breaks down? It gets toad away.", "Why was six afraid of seven? Because seven eight nine.",
        "Did you hear about the kidnapping at school? It's okay. He woke up", "Why couldn't the leopard play hide and seek? Because he was always spotted.", "How do you count cows? With a cowculator."]
    coin_outcome = ["heads", "tails"]
    default_strings = ["I'm sorry, I didn't get you. Would you mind repeating that for me?", "I couldn't quite catch what you were saying. Could you please repeat that?",
        "I'm afraid I didn't get that.", "I don't think I know how to do that.", "Could you repeat that once again?", "Sorry, I can't seem to do that. "]

    # if - elif for checking various questions
    if pred_text == 'who are you' or pred text == "what's your name" or pred_text = "what is your name":
        tts("I'm Alice, you're friendly virtual assistant! How can I help?") elif pred_text == 'where are you from':

    elif message_checker(pred_text, ["flip", "coin"]):
        tts("Okay I will flip a coin for you.")
        playsound('D:/Project/Codes/Sound Effects/coinflip.mp3')
        tts("You got " + coin_outcome[random.randint(0, 1)])

    elif pred_text = "who is your creator":
        tts("My creator is Ashley James.")

    elif message_checker(pred_text, ("joke", "tell"]):
        ans = "yes"
        joke_prev = 100
        while ans = "yes":
            joke_index = random.randint(0, len(joke list) - 1)
            while joke_index == joke_prev:
                joke_index = random.randint(0, len(joke_list) - 1) tts("Here's a joke for you." + joke_list[joke_index])
                tts("Do you want to hear another one?")
                ans = listening_for_commands()
                if ans == "no" or ans == "nope":
                    tts("Okay. Ask me something else.")
                break
            joke_prev = joke_index

    elif message checker(pred text, ["self", "destruct"]) or message checker(pred_text, ["countdown"]):
        tts("ten. nine. eight. seven. six. five. four. three. two. one")
    elif message_checker(pred_text, ["lucky", "number"]):
        tts("Your lucky number is " + str(random.randint(1, 100)))

    # telling the time
    elif message_checker(pred_text, ["time"]):
        tts("The time is " + datetime.strftime(datetime.now(), '%1:%M %p'))

    # finding a definition from wikipedia
    elif message_checker(pred_text, ["define"]):
        search_wiki(pred_text)

    # finding weather
    elif message_checker(pred_text, ["how", "weather"]):
        find_weather()

    # reading news headlines
    elif message_checker(pred_text, ['headlines']):
    read_news()

    # searching wolframalpha
    elif pred_text.split([0] in ("how", "when", "why", "what", "who"]:
        search_wolfram(pred_text)

    # shut down
    elif message_checker(pred_text, ["shutdown"]) === True:
        tts("Shutting down. Bye!")
        break
    else:
        tts(default strings[random.randint(0, len(default_strings)-1)])
