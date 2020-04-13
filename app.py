import sys
import wave

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from ui_app import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import random

import signalwidget
import filtrsignalwidget
from butterworth_filter import ButterworthFiltringSignal

class window(QtWidgets.QMainWindow):
    NOT_FILTRED = False
    FILTRES = True

    count = 0
    countS = 0

    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tempFiltredWidget = None
        self.tempWidget = None

        self.sample = None
        self.sample_rate = None
        self.sample_time = None

        self.orderFiltr = 0
        self.criticalFrequency = 0
        self.samplingFrequency = 0

        self.initActionUI()

    def initActionUI(self):
        self.ui.actionOpen_WAV_file_2.triggered.connect(self.open_file)
        self.ui.actionSave_WAV_file.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionSetting_filter.triggered.connect(self.open_settingWindow)
        self.ui.actionAbout.triggered.connect(self.open_aboutWindow)

        self.ui.SliderOrder.setRange(-5000, 5000)
        self.ui.SliderOrder.setPageStep(1)
        self.ui.SliderOrder.valueChanged.connect(self.changeOrder)
        self.ui.spinBoxOrger.setRange(-5000, 5000)
        self.ui.spinBoxOrger.valueChanged.connect(self.changeSpinOrder)


        self.ui.SliderCrit.setRange(-5000.00, 5000.00)
        self.ui.SliderCrit.setPageStep(1)
        self.ui.SliderCrit.valueChanged.connect(self.changeCrit)
        self.ui.spinBoxCrit.setRange(-5000.00, 5000.00)
        self.ui.spinBoxCrit.valueChanged.connect(self.changeSpinCrit)


        self.ui.SliderFreq.setRange(-5000.0, 5000.0)
        self.ui.SliderFreq.setPageStep(0.01)
        self.ui.SliderFreq.valueChanged.connect(self.changeFreq)
        self.ui.SpinBoxFreq.setRange(-5000.0, 5000.0)
        self.ui.SpinBoxFreq.valueChanged.connect(self.changeSpinFreq)

        self.ui.startButton.clicked.connect(self.start_filtering)

    def start_filtering(self):
        butteroworthFiltringSignal = ButterworthFiltringSignal(orderFiltr=self.orderFiltr,
                                                                criticalFrequency=self.criticalFrequency,
                                                               samplingFrequency=self.samplingFrequency)
        filtredSepmle = butteroworthFiltringSignal.butter_bandpass_filter(self.sample)
        width, height = butteroworthFiltringSignal.AFRfilter()
        print("ok")
        self.start_draw(filtredSepmle)
        self.start_drawFilt(filtredSepmle, width, height, self.sample_rate)

    def start_drawFilt(self, *filt):
        print(filt)
        window.count = window.count + 1
        print(window.count)
        if window.count >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
            self.tempFiltredWidget = None
            window.count = 0
            print("DEL")

        s = self.sample
        self.filtSignal = filtrsignalwidget.filtrSignalWidget(s, filt, parent=self)
        self.tempFiltredWidget = self.filtSignal
        self.ui.horizontalLayout.addWidget(self.tempFiltredWidget)


    def start_draw(self, *filt):
        window.countS = window.countS + 1
        print(window.countS)
        if window.countS >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempWidget)
            self.tempWidget = None
            window.countS = 0
            print("DEL")

        s = self.sample
        self.starterSignal = signalwidget.signalWidget(s, filt, parent=self)
        self.tempWidget = self.starterSignal
        self.ui.horizontalLayout.addWidget(self.tempWidget)


    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open file", "","WAV Files (*.wav)", options=options)
        self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
        self.ui.horizontalLayout.removeWidget(self.tempWidget)

        print(self.orderFiltr)
        print(self.criticalFrequency)
        print(self.samplingFrequency)

        if file_path:
            file_name = file_path.split("/")
            self.ui.sampleLabel.setText(file_name[-1])
            print(file_path)
            self.sample_rate, self.sample = wavfile.read(file_path)
            self.sample_time = self.sample.shape[0] / self.sample_rate

            print("Good")
            print(self.sample)

            self.start_draw()


    def changeOrder(self, value):
        self.ui.spinBoxOrger.setValue(value)
        self.orderFiltr = value


    def changeFreq(self, value):
        self.ui.SpinBoxFreq.setValue(float(value))
        self.criticalFrequency = value


    def changeCrit(self, value):
        self.ui.spinBoxCrit.setValue(value)
        self.samplingFrequency = value


    def changeSpinOrder(self, value):
        self.ui.SliderOrder.setValue(value)
        self.orderFiltr = value


    def changeSpinFreq(self, value):
        self.ui.SliderFreq.setValue(value)
        self.criticalFrequency = value


    def changeSpinCrit(self, value):
        self.ui.SliderCrit.setValue(value)
        self.samplingFrequency = value


    def save_file(self):
        pass


    def exit(self):
        pass


    def open_settingWindow(self):
        pass


    def open_aboutWindow(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.show()
    sys.exit(app.exec())