#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from mainWindow import *
from proxySwitch import ProxySwitch
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self) #setup方法是继承Ui_MainWindow的，然后setup方法的 参数类型 是QMainWindow
        self.ps = ProxySwitch() #初始化ProxySwitch类
        self.__add_logic()

    def pushButton_SetOn_clicked(self):
        proxyURL=self.lineEdit_proxyURL.text()
        print(proxyURL)
        self.ps.set_proxy_on(proxyURL)


    def pushButton_SetOff_clicked(self):
        self.ps.set_proxy_off()

    def __add_logic(self):
        self.pushButton_SetOn.clicked.connect(self.pushButton_SetOn_clicked)
        self.pushButton_SetOff.clicked.connect(self.pushButton_SetOff_clicked)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())