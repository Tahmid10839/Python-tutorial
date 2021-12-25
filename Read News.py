
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("Today's News")
    url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=3c9e5a5f517b4068aeae739665b2ddfc"
    news = requests.get(url).text
    news_json = json.loads(news)
    arts = news_json["articles"]
    for ar in arts:
        print(ar["title"])
        print(ar['description'])
        speak(ar["title"])
        speak(ar['description'])
    speak("Thank you for listening the news. Have a good day")


