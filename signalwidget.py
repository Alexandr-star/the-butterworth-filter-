#from ui_app import Ui_MainWindow
from PyQt5.QtWidgets import QSizePolicy

import ui_app
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

class signalWidget(FigureCanvas):
    def __init__(self, parent=None, width=372, height=529, dpi=100, drawFunc=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.drawSignal()

    def drawSignal(self):
        data = [random.random() for i in range(250)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-', linewidth = 0.5)
        ax.set_title('Not Filtr')
