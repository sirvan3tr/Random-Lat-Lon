'''
Creating a geo grid
Author: S Almasi
'''

import random, math, csv, json

# Initial starting point
# Top right
lat0 = 51.678288
lon0 = -0.471079

json_file = []
for i in range(1,200):
    tlon = lon0
    lat0 = lat0 - 0.005
    for j in range(1,200):
        tlon = tlon + 0.005
        temp = {
            'lon': tlon,
            'lat' : lat0
        }

        json_file.append(temp)

with open('grid.json', 'w') as file:
    json.dump(json_file, file)
