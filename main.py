import random, math, csv, json
import psycopg2

conn = psycopg2.connect(user="postgres", host="localhost", port="5432", database="smartCommuter")
cur = conn.cursor()
print (conn.get_dsn_parameters(),"\n")

y0 = 51.509865 #London's latitude
x0 = -0.118092 #London's longitude
r = 15000/111300 #15km radius

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
    
    price = random.randint(100000,1500000)
    beds = random.randint(1,10)
    return(randLat, randLon, price, beds)


print(generateLatLon(y0, x0, r))

#file = open('rand_geo.csv', 'w')
#writer = csv.writer(file)

jsonObjs = []
for i in range(0,10):
    lat, lon, price, beds = generateLatLon(y0, x0, r)
    jsonObj = {"lat": lat, "lon": lon, "price": price, "beds": beds }
    jsonObjs.append(jsonObj)
    point = str(lon)+" "+str(lat)
    print(point)
    cur.execute("INSERT INTO listings (geo) VALUES (ST_GeomFromText('POINT(-0.32376842224456137 51.48206695356913)', 26910))")
with open("randGeo.json", "w") as jsonFile:
    json.dump(jsonObjs, jsonFile)

cur.close()
conn.close()
