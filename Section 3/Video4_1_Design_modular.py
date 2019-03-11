'''
Created on Mar 8, 2019
@author: Burkhard A. Meier
'''







from PyQt5 import QtWidgets
from Section3.Designer_code.Video3_First_Design import Ui_MainWindow



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    


















