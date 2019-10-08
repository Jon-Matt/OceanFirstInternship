from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

class emotionwords:
    def getGood(self):
        URL = 'https://www.thesaurus.com/browse/good#'
        Response = requests.get(URL)
        Content = BeautifulSoup(Response.content, "html.parser")
        word_menu = Content.find(class_="css-1lc0dpe et6tpn80")
        word_array = word_menu.findAll('a')
        array = []
        for word in word_array:
            array.append(word.text)
        array.remove("bad")
        array.append("good")
        return array
    def getBad(self):
        URLbad = 'https://www.thesaurus.com/browse/bad?s=t'
        Response = requests.get(URLbad)
        Content = BeautifulSoup(Response.content, "html.parser")
        bad = Content.find(class_="css-1lc0dpe et6tpn80")
        word_array = bad.findAll('a')
        array=[]
        for word in word_array:
            array.append(word.text)
        array.append("bad")
        return array
    def print(self, array):
        for word in array:
            print(word)

words = emotionwords
Lords = [words.getGood(emotionwords),words.getBad(emotionwords)]
df = pd.DataFrame(Lords)
review = "your company is bad"


df=df.T
print(df[0])


