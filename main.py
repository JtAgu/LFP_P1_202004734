# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AnalizadorLexico import AnalizadorLexico
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
import copy
import webbrowser
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Cargar_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Cargar_BTN.setGeometry(QtCore.QRect(350, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Cargar_BTN.setFont(font)
        self.Cargar_BTN.setObjectName("Cargar_BTN")
        self.Cargar.clicked.connect(self.CargarArchivo)

        self.Analizar_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Analizar_BTN.setGeometry(QtCore.QRect(510, 10, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Analizar_BTN.setFont(font)
        self.Analizar_BTN.setObjectName("Analizar_BTN")
        self.Cargar.clicked.connect(self.AnalizarArchivo)

        self.Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(20, 90, 621, 241))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Imagen.setFont(font)
        self.Imagen.setObjectName("Imagen")
        self.Prev_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Prev_BTN.setGeometry(QtCore.QRect(90, 480, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Prev_BTN.setFont(font)
        self.Prev_BTN.setObjectName("Prev_BTN")
        self.Next_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Next_BTN.setGeometry(QtCore.QRect(490, 480, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Next_BTN.setFont(font)
        self.Next_BTN.setObjectName("Next_BTN")
        self.Pause_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_BTN.setGeometry(QtCore.QRect(190, 480, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Pause_BTN.setFont(font)
        self.Pause_BTN.setObjectName("Pause_BTN")
        self.Play_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Play_BTN.setGeometry(QtCore.QRect(290, 480, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Play_BTN.setFont(font)
        self.Play_BTN.setObjectName("Play_BTN")
        self.Stop_BTN = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_BTN.setGeometry(QtCore.QRect(390, 480, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.Stop_BTN.setFont(font)
        self.Stop_BTN.setObjectName("Stop_BTN")
        self.informacion_Area = QtWidgets.QTextEdit(self.centralwidget)
        self.informacion_Area.setGeometry(QtCore.QRect(20, 350, 621, 121))
        font = QtGui.QFont()
        font.setFamily("Technic")
        font.setPointSize(11)
        self.informacion_Area.setFont(font)
        self.informacion_Area.setObjectName("informacion_Area")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cargar_BTN.setText(_translate("MainWindow", "CARGAR"))
        self.Analizar_BTN.setText(_translate("MainWindow", "ANALIZAR"))
        self.Imagen.setText(_translate("MainWindow", "MUSICA"))
        self.Prev_BTN.setText(_translate("MainWindow", "PREV"))
        self.Next_BTN.setText(_translate("MainWindow", "NEXT"))
        self.Pause_BTN.setText(_translate("MainWindow", "PAUSE"))
        self.Play_BTN.setText(_translate("MainWindow", "PLAY"))
        self.Stop_BTN.setText(_translate("MainWindow", "STOP"))
        self.informacion_Area.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Technic\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">INFORMACION</p></body></html>"))

    def FuncionPresionar(self):
        buscar = QFileDialog.getOpenFileName()
        size=len(buscar[0])
        final=""

        for x in buscar[0]:
            if size<6:
                final+=x
            size-=1
        if final==".mt3":
            print(":D")
        else:
            msg=QMessageBox()
            msg.setWindowTitle("OCURRIO UN ERROR")
            msg.setText("Extension de archivo incorrecta")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
