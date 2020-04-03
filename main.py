import random, math, csv, json

y0 = 51.509865 #London's latitude
x0 = -0.118092 #London's longitude
r = 10000/111300 #10km radius

'''
y0 = Latitude
x0 = Longitude
r = radius from the centre (meters)
'''
def generateLatLon(y0, x0, r):    
    u = random.random()
    v = random.random()
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    x1 = x / math.cos(y0)

    randLat = y + y0
    randLon = x0 + x1
    
    return(randLat, randLon)


print(generateLatLon(y0, x0, r))

#file = open('rand_geo.csv', 'w')
#writer = csv.writer(file)

jsonObjs = []
for i in range(0,10000):
    lat, lon = generateLatLon(y0, x0, r)
    jsonObj = {"lat": lat, "lon": lon}
    jsonObjs.append(jsonObj)

with open("randGeo.json", "w") as jsonFile:
    json.dump(jsonObjs, jsonFile)

