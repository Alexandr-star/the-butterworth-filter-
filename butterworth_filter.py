import numpy
from scipy import signal

from sample import SampleSignal

class ButterworthFiltringSignal(SampleSignal):
    
    def __init__(self, samplingFrequency, typeFiltr="low", analog=True):

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
                            btype=self.__typeFiltr,
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

    # def butter_bandpass2(self):
    #     b, a = signal.butter(self.__orderFiltr,
    #                         self.__criticalFrequency,
    #                         btype=self.__typeFiltr,
    #                         analog=self.__analog,
    #                         output="ba")
    #
    #     w, h = signal.freqs(b, a)
    #     return w, h


    def AFRfilter(self):
        sos = self.butter_bandpass()
        w, h = signal.sosfreqz(sos)
        
        return w, h