'''
Creating a geo gridv2
Author: S Almasi
'''

import random, math, csv, json, requests, pickle, time

tic = time.perf_counter()

'''
Get Car Travel Time
Both start and end are lon,lat string formats.
e.g. "-0.2801,51.5028"
'''
def getCarTravelTime(starting, ending):
    try:
        r = requests.get("http://127.0.0.1:5000/route/v1/driving/"+starting+";"+ending+"?steps=false")
        car_dur = round((r.json()['routes'][0]['duration']/60)*1.3,0) # /60 to convert to minutes
    except:
        car_dur = 0

    return car_dur

# Initial starting point
# Top right

lat0 = 51.661103
lon0 = -0.262534

json_file = []
n =  50 #grid width and height
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

with open('grid3.json', 'w') as file:
    json.dump(json_file, file)

toc = time.perf_counter()
print(f"Dumped json at: {toc - tic:0.4f} seconds")

duration_matrix = []
# Concat the grid coords
coords = ""
for i in json_file:
    coords = coords + str(i['lon'])+","+str(i['lat'])+";"
coords = coords[:-1]

# sources
sources = "-0.175548,51.498627;-0.260069,51.512937;-0.125999,51.425689"

count = 0
total = pow(n,2)
for i in json_file:
    start = str(i['lon'])+","+str(i['lat'])
    # do the heavy lifting
    r = requests.get("http://127.0.0.1:5000/table/v1/driving/"+start+";"+coords+"?sources=0")
    print("length: ", len(r.json()['durations']))
    duration_matrix.append(r.json())
    print(count, total)
    count = count + 1

with open('duration_matrix3', 'wb') as fp:
    pickle.dump(duration_matrix, fp)

# The timer
toc = time.perf_counter()
print(f"Calculated travel time: {toc - tic:0.4f} seconds")
