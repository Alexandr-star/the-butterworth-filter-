from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

class filtrSignalWidget(FigureCanvas):
    def __init__(self, sample, *filtr, parent=None, width=372, height=529, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.drawFiltredSignal(sample, filtr)

    def drawFiltredSignal(self, sample, filtr):
        arr = filtr[0]
        T = 0.5
        filtred_signal = arr[0]
        w = arr[1]
        h = arr[2]
        fs = arr[3]
        #t = np.linspace(0, T, T * fs, endpoint=False)
        print("w", len(w))
        print("h", len(h))
        print("fs", fs)
        print("filt", len(filtred_signal), filtred_signal)

        canvasSignal = self.figure.add_subplot(111)
        canvasSignal.semilogx(w, 20 * np.log10(abs(h)))
        canvasSignal.set_title('AFR')
        canvasSignal.set_ylabel("x")

