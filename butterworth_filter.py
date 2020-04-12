import numpy
from scipy import signal

from sample import SampleSignal

class ButterworthFiltringSignal(SampleSignal):
    
    def __init__(self,
                    lowcut=500.0,
                    highcut = 1250.0,
                    orderFiltr=12,
                    criticalFrequency=32,
                    samplingFrequency=1,
                    typeFiltr="lowpass",
                    analog=True):

        self.__lowcut = lowcut
        self.__highcut = highcut
        # Порядок фильтра
        self.__orderFiltr = orderFiltr 
        # Критическая чачтота или частоты 
        self.__criticalFrequency = criticalFrequency
        # тип фильтра
        self.__typeFiltr = typeFiltr 
        # Аналоговый фильтр
        self.__analog = analog
        # Частота дискретизации цифровой системы.
        self.__samplingFrequency = samplingFrequency

    def butter_bandpass(self):
        nyq = 0.5 * self.__samplingFrequency
        low = self.__lowcut / nyq
        high = self.__highcut / nyq
        sos = signal.butter(self.__orderFiltr,
                            [low, high],
                            btype=self.__typeFiltr,
                            analog=self.__analog,
                            output="sos")

        return sos

    def butter_bandpass_filter(self, signal, lowcut=500.0, highcut=1250.0):
        sos = self.butter_bandpass()
        y = signal.sosfilt(sos, signal)

        return y


    def AFRfilter(self):
        sos = self.butter_bandpass()
        w, h = signal.sosfreqz(sos, worN=2000)
        
        return w, h