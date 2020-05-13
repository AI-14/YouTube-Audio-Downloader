__author__ = 'Amaan Izhar'
"""
    FRONT-END:
    This is the GUI of YAD-YouTube Audio Downloader (made using Qt Designer and some css).
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 688)
        MainWindow.setMaximumSize(QtCore.QSize(962, 688))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #373b44, stop:1 #4286f4);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.destination_button = QtWidgets.QPushButton(self.centralwidget)
        self.destination_button.setGeometry(QtCore.QRect(360, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.destination_button.setFont(font)
        self.destination_button.setAcceptDrops(False)
        self.destination_button.setStyleSheet("#destination_button {\n"
                                              " background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #00b4db, stop:1 #0083b0);\n"
                                              "border-radius: 4px;\n"
                                              "color: #17141c;\n"
                                              "}\n"
                                              "\n"
                                              "#destination_button:pressed {\n"
                                              "  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                              "                                      stop: 0 #edbc61, stop: 1 #f0ad30);\n"
                                              "}")
        self.destination_button.setObjectName("destination_button")
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(200, 60, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("#input_text {\n"
                                      "background-color: #f0e9c0;\n"
                                      "color: #141417;\n"
                                      "border-radius: 4px;\n"
                                      "}")
        self.input_text.setText("")
        self.input_text.setObjectName("input_text")
        self.paste_link_label = QtWidgets.QLabel(self.centralwidget)
        self.paste_link_label.setGeometry(QtCore.QRect(10, 59, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.paste_link_label.setFont(font)
        self.paste_link_label.setStyleSheet("#paste_link_label {\n"
                                            "  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                            "                                      stop: 0 #edbc61, stop: 1 #f0ad30);\n"
                                            "border-radius: 4px;\n"
                                            "color: #18161c;\n"
                                            "}")
        self.paste_link_label.setAlignment(QtCore.Qt.AlignCenter)
        self.paste_link_label.setObjectName("paste_link_label")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(360, 570, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.download_button.setFont(font)
        self.download_button.setStyleSheet("#download_button {\n"
                                           "background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #43cea2, stop:1 #185a9d);\n"
                                           "border-radius: 4px;\n"
                                           "color: #18161c;\n"
                                           "}\n"
                                           "\n"
                                           "#download_button:pressed {\n"
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                      stop: 0 #edbc61, stop: 1 #f0ad30);\n"
                                           "}")
        self.download_button.setObjectName("download_button")
        self.add_list_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_list_button.setGeometry(QtCore.QRect(790, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_list_button.setFont(font)
        self.add_list_button.setStyleSheet("#add_list_button {\n"
                                           " background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                      stop: 0 #edbc61, stop: 1 #f0ad30);\n"
                                           "border-radius: 4px;\n"
                                           "color: #18161c;\n"
                                           "}\n"
                                           "\n"
                                           "#add_list_button:pressed {\n"
                                           "background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #43cea2, stop:1 #185a9d);\n"
                                           "}")
        self.add_list_button.setObjectName("add_list_button")
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(5, 130, 951, 371))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_widget.setFont(font)
        self.list_widget.setStyleSheet("#list_widget {\n"
                                       "background: #fafad9;\n"
                                       "color: #171714;\n"
                                       "border-radius: 4px\n"
                                       "}")
        self.list_widget.setObjectName("list_widget")
        self.clear_list_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_list_button.setGeometry(QtCore.QRect(420, 510, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.clear_list_button.setFont(font)
        self.clear_list_button.setStyleSheet("#clear_list_button {\n"
                                             "background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #43cea2, stop:1 #185a9d);\n"
                                             "border-radius: 4px;\n"
                                             "color: #18161c;\n"
                                             "}\n"
                                             "\n"
                                             "#clear_list_button:pressed {\n"
                                             "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                             "                                      stop: 0 #edbc61, stop: 1 #f0ad30);\n"
                                             "}")
        self.clear_list_button.setObjectName("clear_list_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Audio Downloader"))
        self.destination_button.setText(_translate("MainWindow", "Select Destination Folder"))
        self.paste_link_label.setText(_translate("MainWindow", "Paste YouTube Link:"))
        self.download_button.setText(_translate("MainWindow", "Download "))
        self.add_list_button.setText(_translate("MainWindow", "Add to the list"))
        self.clear_list_button.setText(_translate("MainWindow", "Clear List"))

