'''
Created on Mar 8, 2019
@author: Burkhard A. Meier
'''





import sys
from PyQt5 import QtWidgets
from Section3.Designer_code.Video3_First_Design import Ui_MainWindow


class RunDesignerGUI():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_MainWindow()                           
        self.ui.setupUi(self.MainWindow)
        
        self.MainWindow.setWindowTitle('PyQt5 GUI')         # change window title        
        
        self.MainWindow.show()
        sys.exit(app.exec_())
    
 
if __name__ == "__main__":
    RunDesignerGUI()   


















