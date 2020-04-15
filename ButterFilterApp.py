import sys
import os

from PyQt5 import QtWidgets

from ui_app import Ui_MainWindow

from scipy.io import wavfile

import signalwidget
import filtrsignalwidget
from butterworth_filter import ButterworthFiltringSignal

class window(QtWidgets.QMainWindow):
    NOT_FILTRED = False
    FILTRES = True
    minDbRange = -200.0
    maxDbRange = 200.0
    minWRange = 0.0
    maxWRange = 50000.0

    count = 0
    countS = 0

    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tempFiltredWidget = None
        self.tempWidget = None

        self.file_name = None
        self.filtredSepmle = None

        self.sample = None
        self.sample_rate = None
        self.sample_time = None

        self.wp = 0
        self.ws = 0
        self.max = 0
        self.min = 0
        self.samplingFrequency = 8000.00

        self.initActionUI()

    def initActionUI(self):
        self.ui.actionOpen_WAV_file_2.triggered.connect(self.open_file)
        # self.ui.actionSave_WAV_file.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit)
        # self.ui.actionSetting_filter.triggered.connect(self.open_settingWindow)
        #self.ui.actionAbout.triggered.connect(self.open_aboutWindow)

        self.ui.doubleSpinBox.setRange(window.minDbRange, window.maxDbRange)
        self.ui.doubleSpinBox.valueChanged.connect(self.setMinDB)
        self.ui.doubleSpinBox.setValue(20.00)

        self.ui.doubleSpinBox_2.setRange(window.minDbRange, window.maxDbRange)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.setMaxDB)
        self.ui.doubleSpinBox_2.setValue(60.00)


        self.ui.doubleSpinBox_3.setRange(window.minWRange, window.maxWRange)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.setWP)
        self.ui.doubleSpinBox_3.setValue(60.00)


        self.ui.doubleSpinBox_4.setRange(window.minWRange, window.maxWRange)
        self.ui.doubleSpinBox_4.valueChanged.connect(self.setWS)
        self.ui.doubleSpinBox_4.setValue(80.00)


        self.ui.SliderFreq.setRange(8000.0, 50000.0)
        self.ui.SliderFreq.setPageStep(0.01)
        self.ui.SliderFreq.valueChanged.connect(self.changeFreq)
        self.ui.SpinBoxFreq.setRange(8000.0, 50000.0)
        self.ui.SpinBoxFreq.valueChanged.connect(self.changeSpinFreq)

        self.ui.startButton.clicked.connect(self.start_filtering)

    def start_filtering(self):
        if (self.sample is None): return
        if self.min == 0 or self.max == 0 or self.wp == 0 or self.ws == 0:
            self.ui.labelExept.setText("divide by zero encountered")
            return
        else:
            self.ui.labelExept.setText("")
        butteroworthFiltringSignal = ButterworthFiltringSignal(self.samplingFrequency)
        butteroworthFiltringSignal.setOrderAndCritFreq(self.wp, self.ws, self.max, self.min)

        self.filtredSepmle = butteroworthFiltringSignal.butter_bandpass_filter(self.sample)
        width, height = butteroworthFiltringSignal.AFRfilter()
        self.start_draw(self.filtredSepmle)
        self.start_drawFilt(width, height)

    def start_drawFilt(self, *filt):
        window.count = window.count + 1
        if window.count >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
            self.tempFiltredWidget = None
            window.count = 0
            print("DEL")

        self.filtSignal = filtrsignalwidget.filtrSignalWidget(filt, parent=self)
        self.tempFiltredWidget = self.filtSignal
        self.ui.horizontalLayout.addWidget(self.tempFiltredWidget)



    def start_draw(self, *filt):
        window.countS = window.countS + 1
        print(window.countS)
        if window.countS >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempWidget)
            self.tempWidget = None
            window.countS = 0

        s = self.sample
        self.starterSignal = signalwidget.signalWidget(s, self.sample_time, filt, parent=self)
        self.tempWidget = self.starterSignal
        self.ui.horizontalLayout.addWidget(self.tempWidget)


    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        url = os.path.abspath(__file__)
        url = url.split('\\')
        url = url[:(len(url) - 1)]
        url = "\\".join(url)
        print(url)


        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open file", url, "WAV Files (*.wav)", options=options)
        self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
        self.ui.horizontalLayout.removeWidget(self.tempWidget)

        if file_path:
            self.file_name = file_path.split("/")
            self.ui.sampleLabel.setText(self.file_name[-1])
            print(file_path)
            self.sample_rate, self.sample = wavfile.read(file_path)
            self.sample_time = self.sample.shape[0] / self.sample_rate
            print(self.sample_rate)
            print(self.sample.shape[0])

            print(self.sample)

            self.start_draw()



    def setMinDB(self, value):
        self.min = value

    def setMaxDB(self, value):
        self.max = value

    def setWP(self, value):
        self.wp = value

    def setWS(self, value):
        self.ws = value


    def changeFreq(self, value):
        self.ui.SpinBoxFreq.setValue(float(value))
        self.samplingFrequency = value

    def changeSpinFreq(self, value):
        self.ui.SliderFreq.setValue(value)
        self.samplingFrequency = value

    # def save_file(self):
    #     if self.filtredSepmle is None:
    #         return
    #     if self.file_name is not None:
    #         options = QtWidgets.QFileDialog.Options()
    #         file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Open file", "", "WAV Files (*.wav)", options=options)
    #         print('__________________')
    #         if file_path:
    #             filename = file_path.split("/")
    #             print(filename)
    #             print(self.filtredSepmle)
    #             wavfile.write(filename[-1], self.sample_rate, np.array(self.filtredSepmle))

    def exit(self):
        pass


    def open_settingWindow(self):
        pass


    def open_aboutWindow(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.setFixedSize(1050, 600)
    application.show()
    sys.exit(app.exec())