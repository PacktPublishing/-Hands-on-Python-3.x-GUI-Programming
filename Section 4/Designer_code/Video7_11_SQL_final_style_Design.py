# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Video6_11_SQL_final_style_Design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget{\n"
"background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_set_label{\n"
"background-color: rgb(255, 0, 255);\n"
"}\n"
"")
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_set_label = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_set_label.setObjectName("pushButton_set_label")
        self.horizontalLayout.addWidget(self.pushButton_set_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setObjectName("tab_2")
        self.pushButton_convert = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_convert.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.pushButton_convert.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 321, 101))
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 321, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_convert = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_convert.setObjectName("label_convert")
        self.horizontalLayout_2.addWidget(self.label_convert)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.radioButton_ui = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_ui.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_ui.setObjectName("radioButton_ui")
        self.radioButton_exe = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_exe.setGeometry(QtCore.QRect(120, 20, 82, 17))
        self.radioButton_exe.setObjectName("radioButton_exe")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3_network = QtWidgets.QWidget()
        self.tab_3_network.setStyleSheet("")
        self.tab_3_network.setObjectName("tab_3_network")
        self.groupBox_2_client1 = QtWidgets.QGroupBox(self.tab_3_network)
        self.groupBox_2_client1.setGeometry(QtCore.QRect(10, 10, 121, 191))
        self.groupBox_2_client1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2_client1.setObjectName("groupBox_2_client1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2_client1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 19, 101, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_client1 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_client1.setObjectName("textEdit_client1")
        self.verticalLayout_4.addWidget(self.textEdit_client1)
        self.lineEdit_client1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_client1.setObjectName("lineEdit_client1")
        self.verticalLayout_4.addWidget(self.lineEdit_client1)
        self.pushButton_client1_send = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_client1_send.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_client1_send.setObjectName("pushButton_client1_send")
        self.verticalLayout_4.addWidget(self.pushButton_client1_send)
        self.groupBox_3_client2 = QtWidgets.QGroupBox(self.tab_3_network)
        self.groupBox_3_client2.setGeometry(QtCore.QRect(140, 10, 121, 191))
        self.groupBox_3_client2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_3_client2.setObjectName("groupBox_3_client2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3_client2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 19, 101, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit_client2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_client2.setObjectName("textEdit_client2")
        self.verticalLayout_5.addWidget(self.textEdit_client2)
        self.lineEdit_client2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_client2.setObjectName("lineEdit_client2")
        self.verticalLayout_5.addWidget(self.lineEdit_client2)
        self.pushButton_client2_send = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_client2_send.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_client2_send.setObjectName("pushButton_client2_send")
        self.verticalLayout_5.addWidget(self.pushButton_client2_send)
        self.groupBox_4_server = QtWidgets.QGroupBox(self.tab_3_network)
        self.groupBox_4_server.setGeometry(QtCore.QRect(270, 100, 61, 101))
        self.groupBox_4_server.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.groupBox_4_server.setObjectName("groupBox_4_server")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4_server)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4_port_number = QtWidgets.QLineEdit(self.groupBox_4_server)
        self.lineEdit_4_port_number.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.lineEdit_4_port_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4_port_number.setObjectName("lineEdit_4_port_number")
        self.pushButton_3_start = QtWidgets.QPushButton(self.groupBox_4_server)
        self.pushButton_3_start.setGeometry(QtCore.QRect(10, 70, 41, 23))
        self.pushButton_3_start.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3_start.setObjectName("pushButton_3_start")
        self.tabWidget.addTab(self.tab_3_network, "")
        self.tab_4_SQL = QtWidgets.QWidget()
        self.tab_4_SQL.setStyleSheet("QWidget{\n"
"background-color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.tab_4_SQL.setObjectName("tab_4_SQL")
        self.tableView = QtWidgets.QTableView(self.tab_4_SQL)
        self.tableView.setGeometry(QtCore.QRect(95, 11, 321, 181))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4_SQL)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 81, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_SQL_view_data = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_SQL_view_data.setObjectName("button_SQL_view_data")
        self.verticalLayout_3.addWidget(self.button_SQL_view_data)
        self.button_SQL_add = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_SQL_add.setObjectName("button_SQL_add")
        self.verticalLayout_3.addWidget(self.button_SQL_add)
        self.button_SQL_delete = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_SQL_delete.setObjectName("button_SQL_delete")
        self.verticalLayout_3.addWidget(self.button_SQL_delete)
        self.button_SQL_create_db = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.button_SQL_create_db.setObjectName("button_SQL_create_db")
        self.verticalLayout_3.addWidget(self.button_SQL_create_db)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_4_SQL, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/new_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear label"))
        self.pushButton_set_label.setText(_translate("MainWindow", "Set label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Label"))
        self.pushButton_convert.setText(_translate("MainWindow", "Convert"))
        self.groupBox.setTitle(_translate("MainWindow", "UI and PY conversions"))
        self.label_convert.setText(_translate("MainWindow", "<click radio button>"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.radioButton_ui.setText(_translate("MainWindow", "UI to PY"))
        self.radioButton_exe.setText(_translate("MainWindow", "PY to EXE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Conversions"))
        self.groupBox_2_client1.setTitle(_translate("MainWindow", "TCP Client"))
        self.pushButton_client1_send.setText(_translate("MainWindow", "Connect to Server"))
        self.groupBox_3_client2.setTitle(_translate("MainWindow", "TCP Client"))
        self.pushButton_client2_send.setText(_translate("MainWindow", "Connect to Server"))
        self.groupBox_4_server.setTitle(_translate("MainWindow", "Server"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.lineEdit_4_port_number.setText(_translate("MainWindow", "12345"))
        self.pushButton_3_start.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3_network), _translate("MainWindow", "Network"))
        self.button_SQL_view_data.setText(_translate("MainWindow", "View Data"))
        self.button_SQL_add.setText(_translate("MainWindow", "Add Row"))
        self.button_SQL_delete.setText(_translate("MainWindow", "Delete Row"))
        self.button_SQL_create_db.setText(_translate("MainWindow", "Create DB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4_SQL), _translate("MainWindow", "SQL"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.statusbar.setStatusTip(_translate("MainWindow", "Statusbar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

