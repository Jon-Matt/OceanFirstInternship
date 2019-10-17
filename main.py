from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def sentiment_analysis(self, listgood, listbad):
    good = 0
    bad =0
    for word in listgood:
        if word in review:
            good +=1
    for word in listbad:
        if word in review:
            bad+=1
    slice = [bad , good]
    labeling = ['bad', 'good']
    colors = ['r', 'g']
    plt.pie(slice, labels=labeling, colors=colors, startangle=90, autopct='%.1f%%')
    plt.title("data")
    plt.show()


keywords = ["customer service", "company", "website", "atm","amigo", "fees", "interest", "loans", "account"]
customer_service = 0
company = 1
website = 2
atm = 3
amigo = 4
fees = 5
interest = 6
loans = 7
account = 8
    #customer service = row 1, company = row 2,website = row 3, atm = row 4, amigo = row 5, fees = row 6, interest = row 7, loans = 8, account = 9

counters = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #column 1 = number of times the keyword has been mentioned, column 2 = times mentioned with positive word, column 3 = times mentioned with negtive word
review = input("write your review \n")



def getGoodWords():
    f = open("Goodwords.txt", "r")
    f1 = f.readlines()
    listlength = len(f1)
    i =0
    while i<listlength:
        f1[i]=f1[i].strip('\n')
        i+=1
    return f1
def getBadWords():
    f = open("Badwords.txt" , "r")
    f1 = f.readlines()
    listlength = len(f1)
    i =0
    while i<listlength:
        f1[i]=f1[i].strip('\n')
        i+=1
    return f1

analysis = sentiment_analysis(review, getGoodWords(), getBadWords())
k = 0
key = "something"
with open("output.txt") as textFile:
    lines = [line.split() for line in textFile]
i =0
y=0
newarr = [[0 for i in range(3)] for j in range(9)]

for row in range(9):
    for col in range(3):
        newarr[row][col] = int(lines[row][col])






while k < len(keywords):
    key = keywords[k]
    if key in review:
        counters[k][0] +=1
        for word in getGoodWords():
            if word in review:
               if review.find(word)> review.find(key):
                    if (((review.find(word) - review.find(key))).__abs__())<=20:
                        counters[k][1]+=1
        for word in getBadWords():
            if word in review:
                if ((review.find(word) - review.find(key)).__abs__())<=20:
                    counters[k][2]+=1
    k+=1
array = np.add(newarr, counters)
df = pd.DataFrame(array)
np.savetxt(r'output.txt' , df.values, fmt='%d')


print(df)

