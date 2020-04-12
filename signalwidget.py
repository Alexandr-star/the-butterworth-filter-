#from ui_app import Ui_MainWindow
from PyQt5.QtWidgets import QSizePolicy

import ui_app
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

class signalWidget(FigureCanvas):
    def __init__(self, sample, parent=None, width=372, height=529, dpi=100, drawFunc=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.drawSignal(sample)

    def drawSignal(self, sample):
        data = [random.random() for i in range(250)]
        canvasSignal = self.figure.add_subplot(2, 1, 1)
        canvasSignal.set_title('Signal')
        canvasSignal.set_ylabel("x")
        canvasSignal.plot(sample, 'r-', linewidth = 0.5)

        canvasAFR = self.figure.add_subplot(2, 1, 2)
        canvasAFR.set_ylabel('x')
        canvasAFR.set_xlabel('y')
        canvasAFR.plot(sample, 'r-', linewidth = 0.5)


