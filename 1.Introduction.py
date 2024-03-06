'''
READ - https://courses.spatialthoughts.com/pyqgis-in-a-day.html

The interface in QGIS is known as PyGIS. Its a API that allows users 
to write python code. This interface, known as QgisInterface, contains classes with 
various methods that provide mechanism for intercation in QGIS enviroment.
The interface allows access to Qgis's toolbar, menu, canvas and others parts of the 
application. When QGIS is running a variable iface is set up to as an instance of a class
QgisInterface.
'''

# Add layers to the qgis  interface

# Assign attributes to a variable
dist = 'F:/Programs/QGIS/data/districts.shp'
rvs = 'F:/Programs/QGIS/data/rivers.shp'
tns = 'F:/Programs/QGIS/data/towns.shp'

# Add layers to map 
#dist = iface.addVectorLayer(dist, '', 'ogr')
#rvs = iface.addVectorLayer(rvs, '', 'ogr')
#tns = iface.addVectorLayer(tns, '', 'ogr')

# Load layer without adding to interface
tns = QgsVectorLayer(tns)


# Get file path
# print("DATA SOURCE PATH - ", dist.dataProvider().dataSourceUri())


# Field information
for field in tns.fields():
    print("QGIS FIELD Object Memory location - ",field)                # Memory location 
    print("Name - ", field.name())
    print("Character length - ", field.type())
    print("<-------------------------->")
    

# Show attribute table in window
# iface.showAttributeTable(tns)


