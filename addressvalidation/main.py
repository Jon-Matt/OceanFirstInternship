import sys
import geocoder
import time
import pandas as pd
import numpy as np
def dogeocode():
        array =[]
        t = open('notvalid.txt','w')
        q = open('valid.txt','w')
        with open("addresses.txt") as textFile:
            list = textFile.readlines()
            i=0
            while i<len(list):
                list[i]=list[i].strip('\n')
                i+=1
        listgood =[]
        listbad = []
        z =0

        while z < len(list):
            p=0
            f = geocoder.locationiq(list[z],key='API KEY)
            address = f.address
            location = f.location
            if location.find(" Blvd")!=-1:
                location =location.replace(" Blvd", " Boulevard")
            if location.find(" Rd")!=-1:
                location =location.replace(" Rd", " Road")
            if location.find(" Rt")!=-1:
                location =location.replace(" Rt", " Route")
            if location.find(" Hwy")!=-1:
                location =location.replace(" Hwy", " Highway")
            if location.find(" Pkway")!=-1:
                location =location.replace(" Pkwy", " Parkway")
            time.sleep(1)
            y = 0
            string = ""
            while location[y] != ",":
                string = string + location[y]

                y= y + 1
            if f.address.replace(',','').find(string)!=-1:
                print(list[z] + " Is Valid")
                listgood.append(list[z])
                q.write(f.location+"\n")
                q.write("\n")
            else:
                print(list[z] + " Is not Valid")

                print(f.address)
                listbad.append(list[z])
                t.write("Current: " + f.location+"\n")
                t.write("Closest: "+f.address+"\n")
                t.write("\n")
            z = z + 1
        t.close()

dogeocode()
