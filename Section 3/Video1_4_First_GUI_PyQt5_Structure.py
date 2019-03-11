'''
Created on Mar 7, 2019
@author: Burkhard A. Meier
'''






# Structure of PyQt5 GUIs
#------------------------

# Imports
import sys 
from PyQt5.QtWidgets import QApplication, QWidget

# Create Application  
app = QApplication(sys.argv)                    # sys.argv accepts arguments when run from the command line

# Create Window
gui = QWidget()                                 # creates top-level window


# Add widgets, call methods, change attributes 
gui.setWindowTitle('PyQt5 GUI')                 # give our Window a title
gui.resize(400, 300)                            # specify Window size: width, height


# show the constructed PyQt5 window
gui.show()                                      # have to call show() to make it visible 

# execute the application
sys.exit(app.exec_())                           # sys.exit catches any exceptions





















