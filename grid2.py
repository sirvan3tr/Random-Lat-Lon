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
lat0 = 51.678288
lon0 = -0.471079
x = [
11,12,13,14,
21,22,23,24,
31,32,33,34,
41, 42, 43, 44
]

json_file = []
n =  200 #grid width and height
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

toc = time.perf_counter()
print(f"Dumped json at: {toc - tic:0.4f} seconds")

duration_matrix = []

total_count = 0
total = pow(n,4)
i_count = 0
for i in json_file:
    start = str(i['lon'])+","+str(i['lat'])
    j_count = 0
    for j in json_file:
        if(j_count<=i_count):
            duration_matrix.append(0)
        else:
            end = str(j['lon'])+","+str(j['lat'])
            car_dur = getCarTravelTime(start, end)
            duration_matrix.append(car_dur)
        j_count = j_count + 1
        print(total_count,total)
        total_count = total_count + 1
    i_count = i_count + 1

with open('duration_matrix2', 'wb') as fp:
    pickle.dump(duration_matrix, fp)

toc = time.perf_counter()
print(f"Calculated travel time: {toc - tic:0.4f} seconds")
'''
with open ('duration_matrix', 'rb') as fp:
    itemlist = pickle.load(fp)
'''