import pandas as pd
import numpy as np
with open("output.txt") as textFile:
    lines = [line.split() for line in textFile]
i =0
y=0
array = [[0 for i in range(3)] for j in range(9)]
keywords = ["customer service", "company", "website", "atm","amigo", "fees", "interest", "loans", "account"]
for row in range(9):
    for col in range(3):
        array[row][col] = int(lines[row][col])

def keywordgood():
    maxnum = array[0][1]
    count = 1
    wordcount = 0
    while count < 9:
        if array[count][1] > maxnum:
            maxnum = array[count][1]
            wordcount = count
        count = count+1
    print("The most positively reviewed word is " + keywords[wordcount] + " with " + str(maxnum) + " positive reviews")
def keywordbad():
    maxnum = array[0][2]
    count = 1
    wordcount = 0
    while count < 9:
        if array[count][2] > maxnum:
            maxnum = array[count][2]
            wordcount = count
        count = count+1
    print("The most negatively reviewed word is " + keywords[wordcount] + " with " + str(maxnum) + " negative reviews")
def keyword():
    maxnum = array[0][0]
    count = 1
    wordcount = 0
    while count < 9:
        if array[count][0] > maxnum:
            maxnum = array[count][0]
            wordcount = count
        count = count+1
    print("The most reviewed word is " + keywords[wordcount] + " with " + str(maxnum) + " reviews")
def keywordstats():
    k = 0
    while k < len(keywords):
        key = keywords[k]
        if key in temp:
            print(key + " has been mentioned " + str(array[k][0]) + " times, has had a positive emotion word attached to it " + str(array[k][1]) + " times, and has had a negative emotion word attached to it " + str(array[k][2]) + " times")
        k = k+1
print("what task would you like completed ")
print("1. Most liked aspect of company")
print("2. Least liked aspect of company")
print("3. Most reviewed aspect of company")
print("4. Stats about a specific keyword")
user_input = input()
if (user_input == "1"):
    keywordgood()
if (user_input == "2"):
    keywordbad()
if(user_input =="3"):
    keyword()
if(user_input == "4"):
    temp = input("What keyword would you like to know the stats for?")
    keywordstats()
if(user_input =="5"):
    df = pd.DataFrame(array)
    df.columns=["keyword", "good", "bad"]
    print(df)



