import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from datetime import datetime
from PyQt5.QtGui import *
from main import *


#graph for Blood Oxygen
class boGraph():
    class PlotCanvas(FigureCanvas):
        def __init__(self, parent=None, width=5, height=4, dpi=100):
            fig = Figure(figsize=(width, height), dpi=dpi)
            self.axes = fig.add_subplot(111)
            super(boGraph.PlotCanvas, self).__init__(fig)
            self.setParent(parent)

            FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)

            self.logged_in_user = UserData(name="John", age=25)  # Create a user instance for testing
            self.animation = FuncAnimation(fig, self.update_plot, interval=300)

        def simulate_blood_oxygen(self):
            dynamic_blood_oxygen = random.randint(self.logged_in_user.heart_health.get_bo()-2, logged_in_user.heart_health.get_bo()+2)
            if (dynamic_blood_oxygen <= 90):
                dynamic_blood_oxygen = 90
            if (dynamic_blood_oxygen >=100):
                dynamic_blood_oxygen = 100
            logged_in_user.heart_health.set_bo(dynamic_blood_oxygen)
            current_blood_oxygen = logged_in_user.heart_health.get_bo()
        
            self.DISPLAY_BLOOD_OXYGEN.setText("Blood Oxygen: " + str(current_blood_oxygen))


        def update_plot(self, frame):
            bo = self.simulate_blood_oxygen()
            x = np.linspace(bo, 150, 10, endpoint=True)
            y = np.sin(x)

            # Set new x-axis ticks and labels
            new_xticks = np.linspace(bo, 150, 5, endpoint=True)
            self.axes.set_xticks(new_xticks)
            self.axes.set_xticklabels([f'{tick:.1f}' for tick in new_xticks])

            # Set new y-axis ticks and labels
            new_yticks = np.linspace(-1, 1, 5, endpoint=True)
            self.axes.set_yticks(new_yticks)
            self.axes.set_yticklabels([f'{tick:.1f}' for tick in new_yticks])

            self.axes.clear()
            self.axes.plot(x, y)

            self.draw()


    class MainWindow(QMainWindow):
        def __init__(self):
            super(boGraph.MainWindow, self).__init__()

            central_widget = QWidget(self)
            self.setCentralWidget(central_widget)

            layout = QVBoxLayout(central_widget)
            self.plot_canvas = boGraph.PlotCanvas(self, width=5, height=4, dpi=100)
            layout.addWidget(self.plot_canvas)

            self.show()


    def run_bo_graph():
        app = QApplication(sys.argv)
        window = boGraph.MainWindow()
        sys.exit(app.exec_())

    if __name__ == '__main__':
       run_bo_graph()
