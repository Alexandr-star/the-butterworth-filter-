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

    types = {
        1: np.int8,
        2: np.int16,
        4: np.int32
    }

    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tempFiltredWidget = None
        self.tempWidget = None

        self.sample = None
        self.sample_rate = None
        self.sample_time = None

        self.initActionUI()

    def initActionUI(self):
        self.ui.actionOpen_WAV_file_2.triggered.connect(self.open_file)
        self.ui.actionSave_WAV_file.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionSetting_filter.triggered.connect(self.open_settingWindow)
        self.ui.actionAbout.triggered.connect(self.open_aboutWindow)

        self.ui.startButton.clicked.connect(self.start_filtering)

    def start_filtering(self):
        butteroworthFiltringSignal = ButterworthFiltringSignal()
        filtredSepmle = butteroworthFiltringSignal.butter_bandpass_filter(self.sample)
        width, height = butteroworthFiltringSignal.AFRfilter()

        print(filtredSepmle)
        print(width, "  ", height)


    def start_draw(self):
        window.count = window.count + 1
        print(window.count)
        if window.count >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
            self.tempFiltredWidget = None
            window.count = 0

        s = self.sample
        self.starterSignal = signalwidget.signalWidget(s, self)
        self.tempWidget = self.starterSignal
        self.ui.horizontalLayout.addWidget(self.tempWidget)


    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open file", "","WAV Files (*.wav)", options=options)
        self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
        self.ui.horizontalLayout.removeWidget(self.tempWidget)

        if file_path:
            file_name = file_path.split("/")
            self.ui.sampleLabel.setText(file_name[-1])
            print(file_path)
            self.sample_rate, self.sample = wavfile.read(file_path)
            self.sample_time = self.sample.shape[0] / self.sample_rate

            print("Good")
            print(self.sample)


            self.start_draw()


    def update_singnalGraph(self):
        self.signalGraph = signalwidget.signalWidget(self, self.sample)
        self.ui.horizontalLayout.addWidget(self.signalGraph)



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