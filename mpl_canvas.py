import matplotlib
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):

        fig = Figure()

        self.axes = fig.add_subplot(111)
        self.axes.axis("off")
        super(MplCanvas, self).__init__(fig)