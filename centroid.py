points = [[-0.118092, 51.509865], [-4.063111, 39.867333], [10.26, 50.277009]]

lon = 0
lat = 0

for i in points:
    lon = lon + i[0]
    lat = lat + i[1]

lon = lon/3
lat = lat/3

print(lon, lat)
