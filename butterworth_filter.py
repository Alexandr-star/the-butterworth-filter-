import numpy
from scipy import signal

#from scipy import signal

class ButterworthFilter:
    
    def __init__(self, orderFiltr,
                    criticalFrequency,
                    samplingFrequency,
                    typeFiltr="lowpass",
                    analog=True):
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

    def buttFilter(self, sample):
        sos = signal.butter(self.__orderFiltr,
                            self.__criticalFrequency,
                            btype=self.__typeFiltr,
                            analog=self.__analog,
                            output="sos",
                            fs=self.__samplingFrequency)
        filteredSample = signal.sosfilt(sos, sample)
        
        return filteredSample

    def AFRfilter(self):
        b, a = signal.butter(self.__orderFiltr,
                             self.__criticalFrequency,
                             btype=self.__typeFiltr, 
                             analog=self.__analog, 
                             output="ba")
        w, h = signal.freqs(b, a)
        
        return w, h