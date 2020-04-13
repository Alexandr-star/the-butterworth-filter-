#from ui_app import Ui_MainWindow
from PyQt5.QtWidgets import QSizePolicy

import ui_app
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

class signalWidget(FigureCanvas):
    def __init__(self, sample,  *filtr, parent=None, width=372, height=529, dpi=100, drawFunc=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.drawSignal(sample, filtr)


    def drawSignal(self, sample, filtr):

        canvasSignal = self.figure.add_subplot(2, 1, 1)
        canvasSignal.plot(sample, 'g', linewidth=0.5)
        canvasSignal.set_title('Signal')
        canvasSignal.set_ylabel("x")
        if (len(filtr[0]) != 0):
            filtr_sample = filtr[0]
            filtr_sample = filtr_sample[0]
            canvasAFR = self.figure.add_subplot(2, 1, 2)
            canvasSignal.set_title('Filter signal')
            canvasAFR.set_ylabel('x')
            canvasAFR.set_xlabel('y')
            canvasAFR.plot(filtr_sample, 'r', linewidth=0.5)

