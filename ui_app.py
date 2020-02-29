# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appdesigne.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 481, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_WAV_file = QtWidgets.QAction(MainWindow)
        self.actionSave_WAV_file.setObjectName("actionSave_WAV_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCtrl_O = QtWidgets.QAction(MainWindow)
        self.actionCtrl_O.setObjectName("actionCtrl_O")
        self.actionOpen_WAV_file_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_WAV_file_2.setObjectName("actionOpen_WAV_file_2")
        self.actionSetting_filter = QtWidgets.QAction(MainWindow)
        self.actionSetting_filter.setObjectName("actionSetting_filter")
        self.menuFile.addAction(self.actionOpen_WAV_file_2)
        self.menuFile.addAction(self.actionSave_WAV_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSetting_filter)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "sample"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave_WAV_file.setText(_translate("MainWindow", "Save WAV-file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCtrl_O.setText(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_WAV_file_2.setText(_translate("MainWindow", "Open  WAV-file"))
        self.actionSetting_filter.setText(_translate("MainWindow", "Setting filter"))
