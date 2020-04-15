import numpy
from scipy import signal

from sample import SampleSignal

class ButterworthFiltringSignal(SampleSignal):
    
    def __init__(self, samplingFrequency, typeFiltr="low", analog=False):

        # Порядок фильтра
        self.__orderFiltr = 0
        # Критическая чачтота или частоты 
        self.__criticalFrequency = 0
        # тип фильтра
        self.__typeFiltr = typeFiltr 
        # Аналоговый фильтр
        self.__analog = analog
        # Частота дискретизации цифровой системы.
        self.__samplingFrequency = samplingFrequency

    def butter_bandpass(self):
        sos = signal.butter(self.__orderFiltr,
                            self.__criticalFrequency,
                            "low",
                            analog=self.__analog,
                            output="sos")

        print(sos)
        return sos

    def butter_bandpass_filter(self, sample):
        sos = self.butter_bandpass()
        y = signal.sosfilt(sos, sample)

        return y

    def setOrderAndCritFreq(self, wp, ws, maxBand, minBand):
        self.__orderFiltr, self.__criticalFrequency = signal.buttord(wp=wp, ws=ws, gpass=minBand, gstop=maxBand, analog=False, fs=self.__samplingFrequency)


    #[30, 80], [20, 90]  wp, ws, minBad, maxBand, analog=self.__analog, fs=self.__samplingFrequency

        # getter method
    def get_order(self):
        return self.__orderFiltr


    def AFRfilter(self):
        sos = self.butter_bandpass()
        w, h = signal.sosfreqz(sos)
        
        return w, h