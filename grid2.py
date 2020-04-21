'''
Creating a geo gridv2
Author: S Almasi
'''

import random, math, csv, json

# Initial starting point
# Top right
lat0 = 51.678288
lon0 = -0.471079
x = [
11,12,13,14,
21,22,23,24,
31,32,33,34,
41, 42, 43, 44
]

json_file = []
n 200 #grid width and height
d = 0.005 #grid diff in degrees
for i in range(0,n):
    tlon = lon0
    lat0 = lat0 - d #rows
    for j in range(0,n):
        tlon = tlon + d #cols
        temp = {
            'lon': tlon,
            'lat' : lat0
        }

        json_file.append(temp)

with open('grid2.json', 'w') as file:
    json.dump(json_file, file)

duration_matrix = []