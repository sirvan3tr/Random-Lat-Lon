def getGridIndex(lon, lat, start_lon, start_lat, delta):
    col = round((lon - start_lon)/delta)
    row = round((lat - start_lat)/delta)
    if(col < 0):
        col = col * - 1
    if(row < 0):
        row = row * -1
    return [row, col]
    
def linearGrid(row, col, n):
    # rows and cols start with 1
    # actual lists start with 0
    # col + 1 because the lists start with 0
    g = n * row - (n - col + 1)
    return g


locs = [{
    'lon': -0.175548,
    'lat': 51.498627
    },
    {
    'lon': -0.217110,
    'lat': 51.512937
    },
    {
    'lon': -0.102408,
    'lat': 51.495914
    }]

lat0 = 51.661103
lon0 = -0.262534
n =  50 #grid width and height
d = 0.005 #grid diff in degrees

glocs = []

for i in locs:
    print(i)
    index = getGridIndex(i['lon'], i['lat'], lon0, lat0, d)
    g = linearGrid(index[0], index[1], n)
    glocs.append(g)

smallest_g = 999999999999999
for i in range(0,pow(n,2)):
    sum = 0
    for j in glocs:
        sum = sum + (m[i]['durations'][0][j]/60)
        mi = i
    if(sum < smallest_g) and sum != 0:
        smallest_g = sum
        print(smallest_g, mi)

