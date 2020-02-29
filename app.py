import sys

from PyQt5 import QtWidgets

from ui_app import Ui_MainWindow

from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


class window(QtWidgets.QMainWindow):
    sampleRate = 0
    sample = 0
    sampleTime = 0


    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.initActionUI()

    def initActionUI(self):
        self.ui.actionOpen_WAV_file_2.triggered.connect(self.open_file)
        self.ui.actionSave_WAV_file.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionSetting_filter.triggered.connect(self.open_settingWindow)
        self.ui.actionAbout.triggered.connect(self.open_aboutWindow)

        self.ui.startButton.clicked.connect(self.start_filtering)

    def start_filtering(self):
        pass

    def open_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Open file", "","WAV Files (*.wav)", options=options)
        
        if file_path:
            file_name = file_path.split("/")
            self.ui.sampleLabel.setText(file_name[-1])
            sample_rate, sample = wavfile.read(file_path)
            sample_time = sample.shape[0] / sample_rate
            window.sample = sample
            window.sampleRate = sample_rate
            window.sampleTime = sample_time
            
    
    def save_file(self):
        pass
    
    def exit(self):
        pass

    def open_settingWindow(self):
        pass

    def open_aboutWindow(self):
        pass
    
    

app = QtWidgets.QApplication([])
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

































