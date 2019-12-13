# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_SetOn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetOn.setGeometry(QtCore.QRect(430, 40, 81, 41))
        self.pushButton_SetOn.setObjectName("pushButton_SetOn")
        self.pushButton_SetOff = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SetOff.setGeometry(QtCore.QRect(430, 100, 81, 41))
        self.pushButton_SetOff.setObjectName("pushButton_SetOff")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 150, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_proxyURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_proxyURL.setGeometry(QtCore.QRect(110, 50, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_proxyURL.setFont(font)
        self.lineEdit_proxyURL.setText("")
        self.lineEdit_proxyURL.setClearButtonEnabled(True)
        self.lineEdit_proxyURL.setObjectName("lineEdit_proxyURL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_SetOn.setText(_translate("MainWindow", "启用代理"))
        self.pushButton_SetOff.setText(_translate("MainWindow", "停用代理"))
        self.label.setText(_translate("MainWindow", "当前代理："))
        self.pushButton.setText(_translate("MainWindow", "切换下一个代理"))
        self.pushButton_2.setText(_translate("MainWindow", "获取免费代理"))
        self.lineEdit_proxyURL.setPlaceholderText(_translate("MainWindow", "手动输入代理地址"))

