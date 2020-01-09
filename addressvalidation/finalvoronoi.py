from scipy.spatial import Voronoi, voronoi_plot_2d, cKDTree
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import geocoder
import time

def create_connection(db_file): #creates connection to database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_address(conn, address): #creates an empty table in the database which will contain closest and second closest bank locations
    sql = ''' INSERT INTO address(address, First, Second)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, address)
    return cur.lastrowid

with open("longitude.txt") as textFile: #open the text file containing list of branch longitudes
    lnglist = textFile.readlines() #creates list of longitudes inside code
    for i in range(len(lnglist)):
        lnglist[i] = lnglist[i].strip('\n')

with open("addresslocations.txt") as textFile: #creates list of customer addresses using text file
    list = textFile.readlines()
    i = 0
    for i in range(len(list)):
        list[i] = list[i].strip('\n')

for num in lnglist: #changes value of longitude from string to float
    num = float(num)

with open("latitude.txt") as textFile: #opens text file containing list of branch location latitudes
    latlist = textFile.readlines() #creates list containing the latitudes
    i = 0
    for i in range(len(latlist)):
        latlist[i] = latlist[i].strip('\n')
for num in latlist: #changes values of latitude from string to float
    num = float(num)

banklist = [(latlist[i],lnglist[i]) for i in range(0,len(lnglist))] #creates 2d array containing latidue and longitude of banks
print(banklist)
CustomerList=[[]]
for i in range(len(list)): #creates 2dlist of customer longitudes and latitudes
    f = geocoder.locationiq(list[i], key = '6774a6e0ff9f5f')
    CustomerList.append([f.lat, f.lng])
    time.sleep(1)

CustomerList.pop(0)
vor = Voronoi(banklist) #creates visual voronoi graph
voronoi_plot_2d(vor, show_vertices=False)
new_point = [f.lat, f.lng, 'ro']
plt.plot(new_point[0], new_point[1], 'ro')
plt.show()

voronoi_kdtree=cKDTree(banklist) #creates voronoi which can find regions in which customers are contained
print(CustomerList)
test_point_dist, test_point_regions = voronoi_kdtree.query(CustomerList) #finds closest region

FirstClosest=[] #list holds the voronoi region for each customer address
for x in test_point_regions: #adds regions to the list for the first closest
    FirstClosest.append(x)
    print(x)
temp = [0,0] #will hold temporary point of first closet bank location to be substituted
print(" ")
SecondClosest =[] #list holds the voronoi region for second closest bank to customer address

for i in range(len(CustomerList)):
    temp = banklist[FirstClosest[i]]
    banklist[FirstClosest[i]]=[8.7832, 34.5085] #arbitrary address in africa so we can find second closest voronoi region
    voronoi_kdtree=cKDTree(banklist)
    test_point_dist2,test_point_regions1 = voronoi_kdtree.query(CustomerList[i]) #finds second closest region
    banklist[FirstClosest[i]]= temp
    print(test_point_regions1)
    SecondClosest.append(test_point_regions1)

print(vor.point_region) #prints the regions in order as seen on graph
database = r"C:\sqlite\db\newdb.db"
conn = create_connection(database)
#creates connection to database and adds information in a table (name of address, first closest region index, second closest region index
for i in range(len(CustomerList)):
    with conn:
        print(i)
        address = (str(list[i]), int(FirstClosest[i]), int(SecondClosest[i]))
        create_address(conn, address)
