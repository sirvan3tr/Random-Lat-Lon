import random, math, csv, json
import psycopg2
'''
CREATE TABLE listings (
	id SERIAL PRIMARY KEY,
	geom GEOMETRY(Point, 26910),
	name VARCHAR(128),
	beds SMALLINT,
	price INTEGER,
	gridID INTEGER,
	propType VARCHAR(128)
);
'''
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
    
    propTypes = ['Studio', 'Flat', 'Semi-detached House', 'Detached House']
    price = random.randint(100000,1500000)
    beds = random.randint(1,10)
    propType = propTypes[random.randint(0,3)]
    return(randLat, randLon, beds, price, propType)


print(generateLatLon(y0, x0, r))

jsonObjs = []
for i in range(0,500000):
    lat, lon, beds, price, propType = generateLatLon(y0, x0, r)
    jsonObj = {"lat": lat,
                "lon": lon,
                "price": price,
                "beds": beds,
                "propType": propType
            }
    jsonObjs.append(jsonObj)
    point = str(lon)+" "+str(lat)
    cur.execute("INSERT INTO listings (geom, beds, price, propType) VALUES (ST_GeomFromText('POINT("+point+")', 26910), %s, %s, %s)", (beds, price, propType))
    conn.commit()
with open("randGeo.json", "w") as jsonFile:
    json.dump(jsonObjs, jsonFile)

cur.close()
conn.close()
