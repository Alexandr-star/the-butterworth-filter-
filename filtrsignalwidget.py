from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

class filtrSignalWidget(FigureCanvas):
    def __init__(self, *filtr, parent=None, width=400, height=600, dpi=70):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.drawFiltredSignal(filtr)

    def drawFiltredSignal(self, filtr):
        arr = filtr[0]
        w = arr[0]
        h = arr[1]
        canvasSignal = self.figure.add_subplot(111)
        canvasSignal.semilogx(w, h)
        canvasSignal.set_title('AFR')
        canvasSignal.set_xlabel("Frequency [radians / second]")
        canvasSignal.set_ylabel("Amplitude [dB]")
        canvasSignal.grid(which='both', axis='both')
        #20 * np.log10(abs(h))

