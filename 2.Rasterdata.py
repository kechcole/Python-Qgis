# Add raster 
landsat = 'F:/Programs/QGIS/Composite band 1-8/LE07_L1TP_168061_20180105_20180131_01_T1_Bstack_raster.tif'

# load layer and add to interface
# lyr = iface.addRasterLayer(landsat)

# load layer without adding to interface
lyr = QgsRasterLayer(fn)

# print some raster properties
print('height', lyr.height())
print('width', lyr.width())
print('bands', lyr.bandCount())