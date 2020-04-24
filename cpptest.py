'''
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

lon1 = -0.125999
lat1 = 51.395689
strr = ""
for i in range(0,50):
    lon1 = lon1 + 0.0005
    lat1 = lat1 + 0.0005
    strr = strr + str(lon1)+","+str(lat1)+";"

strr = strr[:-1]
print(strr)
'''
for i in range(0,3):
    start = "-0.125999,51.395689"
    end = "-0.260069,51.512937"
'''

r = requests.get("http://127.0.0.1:5000/table/v1/driving/"+strr)
print(r.json())
print("length: ", len(r.json()['sources']))


toc = time.perf_counter()
print(f"Calculated travel time: {toc - tic:0.4f} seconds")



'''
curl 'http://router.project-osrm.org/table/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219'

# Returns a 1x3 duration matrix
curl 'http://router.project-osrm.org/table/v1/driving/13.388860,52.517037  ;13.397634,52.529407  ;13.428555,52.523219?sources=0'


'''