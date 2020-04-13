import numpy
from scipy import signal

from sample import SampleSignal

class ButterworthFiltringSignal(SampleSignal):
    
    def __init__(self,
                    lowcut=500.0,
                    highcut = 1250.0,
                    orderFiltr=50,
                    criticalFrequency=5,
                    samplingFrequency=100,
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
        sos = signal.butter(self.__orderFiltr,
                            self.__criticalFrequency,
                            btype=self.__typeFiltr,
                            analog=self.__analog,
                            output="sos")

        print(sos)
        return sos

    def butter_bandpass_filter(self, sample):
        sos = self.butter_bandpass()
        y = signal.sosfilt(sos, sample)

        return y


    def butter_bandpass2(self):
        b, a = signal.butter(self.__orderFiltr,
                            self.__criticalFrequency,
                            btype=self.__typeFiltr,
                            analog=self.__analog,
                            output="ba")

        w, h = signal.freqs(b, a)
        return w, h


    def AFRfilter(self):
        sos = self.butter_bandpass()
        w, h = signal.sosfreqz(sos, worN=2000)
        
        return w, h