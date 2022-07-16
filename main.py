from win32com.client import Dispatch
import requests
import json
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Lets Start today's news. We will read only title of every news.")
    url = "https://newsapi.org/v2/top-headlines?q=cricket&from=2022-07-15&to=2022-07-15&sortBy=popularity&apiKey=a23441b217ed489b8350cf8ca4ba317f"
    news = requests.get(url).text
    news_code = requests.get(url)
    print(news_code.status_code)
    newsParsed = json.loads(news)
    print(news)
    print(newsParsed['articles'][0]['title'])
    arts = newsParsed['articles']
    for articles in arts:
         print(articles['title'])
         speak(articles['title'])
         speak("Moving on to next news.... Listen Carefully!")