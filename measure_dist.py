'''
A class is prototype of an object, like a blueprint. 
'''

# Import classes
from qgis.core import QgsDistanceArea
from qgis.core import QgsUnitTypes

# Create a set  of coordinates of locations
san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)
las_vegas = (36.1699, -115.1398)

# Route  --> san_francisco - las_vegas - new_york

# instantiate a class by creating an object d
d = QgsDistanceArea()
# Apply methods of a class above to object d, set ellipsoid as wgs84 to access algorithms
d.setEllipsoid('WGS84')


# Get set values
lat1, lon1 = san_francisco
lat2, lon2 = new_york
lat3, lon3 = las_vegas

# Create objects remember the order is X,Y
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)
point3 = QgsPointXY(lon3, lat3)

# measure distance btn objects following the route 
distance1 = d.measureLine([point1, point3])      # san faransisco to las vegas
distance2 = d.measureLine([point3, point2])       # las vegas to new york 
distance = distance1 + distance2          # in meters 

# manual conversion 
# print(f"{distance/1000} kilometers ")

# convert distance 
distance_km = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceKilometers)
print(distance_km)
