from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
import matplotlib.pyplot as plt
import geocoder
import time

with open("oceanfirstaddresses.txt") as textFile:
    list = textFile.readlines()
    i = 0
    while i < len(list):
        list[i] = list[i].strip('\n')
        i += 1
print(list)
list2=[[]]

z = 0
while (z<len(list)):
    f = geocoder.locationiq(list[z], key='6774a6e0ff9f5f')
    time.sleep(1)
    list2.append([f.lng, f.lat])
    print(list2[z])
    z = z+1
list2.remove([])
points = np.array(list2)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
f = geocoder.locationiq('12 Paulette Drive, Freehold, New Jersey', key = '6774a6e0ff9f5f')
print(vor.point_region)
print (list2)