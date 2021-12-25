import requests
import json


def speak(co,ap,cat):
    from win32com.client import Dispatch

    url = f"http://newsapi.org/v2/top-headlines?country={co}&category={cat}&apiKey={ap}"
    speak = Dispatch("SAPI.SpVoice")
    json_data = requests.get(url).json()
    count=1
    index=0
    news_num=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    speak.Speak("Today's news")
    while count<11:
        news = json_data["articles"][count]['description']
        print(news)
        speak.Speak(f"{news_num[index]} news is{news}")
        count+=1
        index+=1

if __name__ == '__main__':
    co=input("Enter Country:")
    ap=input("Enter api key:")
    cat = input("Categories:\n\t1.health\n\t2.sports\n\t3.technology\n\t4.entertainment\n\t5.science\n\t6.business\nEnter the name of any categories:")
    speak(co,ap,cat)

