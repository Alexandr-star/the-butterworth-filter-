# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appdesigne.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Butterworth")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sampleLabel = QtWidgets.QLabel(self.centralwidget)
        self.sampleLabel.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.sampleLabel.setObjectName("sampleLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.label_3.setObjectName("label_3")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 500, 75, 23))
        self.startButton.setObjectName("startButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 10, 750, 530))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.signalWidget = signalWidget(self.horizontalLayoutWidget)
        #self.signalWidget.setObjectName("signalWidget")
        #self.horizontalLayout.addWidget(self.signalWidget)
        #self.filtrSignalWidget = filtrSignalWidget(self.horizontalLayoutWidget)
        #self.filtrSignalWidget.setObjectName("filtrSignalWidget")
        #self.horizontalLayout.addWidget(self.filtrSignalWidget)
        self.SliderFreq = QtWidgets.QSlider(self.centralwidget)
        self.SliderFreq.setGeometry(QtCore.QRect(10, 290, 160, 22))
        self.SliderFreq.setOrientation(QtCore.Qt.Horizontal)
        self.SliderFreq.setObjectName("SliderFreq")
        self.SpinBoxFreq = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SpinBoxFreq.setGeometry(QtCore.QRect(10, 260, 161, 22))
        self.SpinBoxFreq.setObjectName("SpinBoxFreq")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 90, 51, 16))
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 110, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(130, 110, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 181, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 166, 111, 20))
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(40, 190, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(130, 190, 62, 22))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 190, 21, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
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
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_WAV_file_2)
        self.menuFile.addAction(self.actionSave_WAV_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSetting_filter)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sampleLabel.setText(_translate("MainWindow", "Treks"))
        self.label_2.setText(_translate("MainWindow", "min dB:"))
        self.label_3.setText(_translate("MainWindow", "Частота дискретизации"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "max dB:"))
        self.label_4.setText(_translate("MainWindow", "Полоса пропускания:"))
        self.label_5.setText(_translate("MainWindow", "Граничные частоты"))
        self.label_6.setText(_translate("MainWindow", "полосы пропускания:"))
        self.label_7.setText(_translate("MainWindow", "от"))
        self.label_8.setText(_translate("MainWindow", "до"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        #self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        #self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        #self.actionSave_WAV_file.setText(_translate("MainWindow", "Save WAV-file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCtrl_O.setText(_translate("MainWindow", "Ctrl+O"))
        self.actionOpen_WAV_file_2.setText(_translate("MainWindow", "Open  WAV-file"))
        #self.actionSetting_filter.setText(_translate("MainWindow", "Setting filter"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
from filtrsignalwidget import filtrSignalWidget
from signalwidget import signalWidget
