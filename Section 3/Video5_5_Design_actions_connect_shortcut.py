'''
Created on Mar 8, 2019
@author: Burkhard A. Meier
'''




import sys
from PyQt5 import QtWidgets
from Section3.Designer_code.Video5_First_Design import Ui_MainWindow


class RunDesignerGUI():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        
        self.ui = Ui_MainWindow()                           
        self.ui.setupUi(self.MainWindow)
        
        self.update_widgets()
        self.widget_actions()
        
        self.MainWindow.show()
        sys.exit(app.exec_())
    
    def widget_actions(self):
        self.ui.actionExit.setStatusTip('Click to exit the application')        # use ui reference to update status bar
        self.ui.actionExit.triggered.connect(self.close_GUI)                    # connect widget to method when triggered (clicked)
        self.ui.actionExit.setShortcut('Ctrl+Q')                                # keyboard shortcut, window has focus 
        
    def close_GUI(self): 
        self.MainWindow.close()         # call MainWindow close method, which closes the GUI
    
    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')         # use: self.MainWindow
        self.ui.pushButton.setText('New Button text')       # use: self.ui to access widgets

 
if __name__ == "__main__":
    RunDesignerGUI()   


















