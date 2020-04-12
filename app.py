import sys

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

    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tempFiltredWidget = None
        self.tempWidget = None
        self.initActionUI()

    def initActionUI(self):
        self.ui.actionOpen_WAV_file_2.triggered.connect(self.open_file)
        self.ui.actionSave_WAV_file.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionSetting_filter.triggered.connect(self.open_settingWindow)
        self.ui.actionAbout.triggered.connect(self.open_aboutWindow)

        self.ui.startButton.clicked.connect(self.start_filtering)

    def start_filtering(self):
        window.count = window.count + 1
        print(window.count)
        if window.count >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
            self.tempFiltredWidget = None
            window.count = 0

        self.filtredSignal = filtrsignalwidget.filtrSignalWidget(self)
        self.tempFiltredWidget = self.filtredSignal
        self.ui.horizontalLayout.addWidget(self.tempFiltredWidget)


    def start_draw(self):
        window.count = window.count + 1
        print(window.count)
        if window.count >= 1:
            self.ui.horizontalLayout.removeWidget(self.tempFiltredWidget)
            self.tempFiltredWidget = None
            window.count = 0

        self.starterSignal = signalwidget.signalWidget(self)
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
            sample_rate, sample = wavfile.read(file_path)
            sample_time = sample.shape[0] / sample_rate

            self.start_draw()


    def update_singnalGraph(self):
        self.signalGraph = signalwidget.signalWidget(self)
        self.ui.horizontalLayout.addWidget(self.signalGraph)



    def save_file(self):
        pass


    def exit(self):
        pass


    def open_settingWindow(self):
        pass


    def open_aboutWindow(self):
        pass

#class WidgetPlot(QWidget):
 #   def __init__(self, *args, **kwargs):
  #      QWidget.__init__(self, *args, **kwargs)
   #     self.setLayout(QVBoxLayout())
    #    self.canvas = signalwidget.signalWidget(self)
     #   self.toolbar = NavigationToolbar(self.canvas, self)
      #  self.layout().addWidget(self.toolbar)
       # self.layout().addWidget(self.canvas)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = window()
    application.show()
    sys.exit(app.exec())


##sample_time = sample.shape[0] / sample_rate
#print(sample_time)

# Входные данные

# Порядок фильтра
#order = 10 
# Критическая чачтота или частоты 
#Wn = 0.05
# тип фильтра
#type = 'lowpass' 
# Аналоговый фильтр
#analog = True 
#Тип вывода: числитель / знаменатель («ba»), 
#ноль полюсов («zpk») или секции второго порядка («sos»). 
#Значение по умолчанию - «ba» для обратной совместимости,
#но «sos» следует использовать для фильтрации общего назначения.
#output = {'ba', 'zpk', 'sos'}
# Частота дискретизации цифровой системы.
#fs 

#times = np.linspace(0., sample_time, sample.shape[0])


#sos = signal.butter(order, Wn, btype=type, fs=1000, output='sos')
#filtered_sample = signal.sosfilt(sos, sample)
#fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)


#ax1.plot(times, sample[:, 0], label="Left channel")
#ax1.plot(times, sample[:, 1], label="Right channel")
#ax1.legend()

#ax2.plot(times, filtered_sample[:, 0], label="Left channel")
#ax2.plot(times, filtered_sample[:, 1], label="Right channel")
#ax2.legend()
#plt.tight_layout()

#plt.show()
