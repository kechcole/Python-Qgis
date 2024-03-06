# Query user , fill data in console
mb = QMessageBox()

# Attributes of instance 
print("Instance type - ",type(mb))

# Use method of a class to set message in dialogue box
mb.setText('Click OK to confirm')

# Apply class attribute on an instance above 
mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

# To view the dialogue box , call execute class method. Store the returned value
value = mb.exec()

# Access value
if value == QMessageBox.Ok:
    print('You selected OK')
else :
    print('Selected CANCEL')
    

