
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

    
#heart health graph
class HeartRateGraph(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #self.setWindowTitle('Real-Time Graph')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Create a matplotlib figure and a canvas for PyQt integration
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        # Button to update the graph with new data
        self.update_button = QPushButton('Update Graph', self)
        self.update_button.clicked.connect(self.update_graph)
        self.layout.addWidget(self.update_button)

        # Initial data
        self.x_data = np.arange(0, 10, 0.1)
        self.y_data = np.sin(self.x_data)

        # Plot the initial data
        self.line, = self.ax.plot(self.x_data, self.y_data)
        self.ax.set_title('Real-Time Graph')

    def update_graph(self):
        # Generate new real-time data
        new_data = np.random.rand(100)

        # Update the x_data with new values
        self.x_data = np.append(self.x_data[1:], self.x_data[-1] + 0.1)

        # Update the y_data with new real-time data
        self.y_data = np.append(self.y_data[1:], new_data)

        # Update the plot with the new data
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)

        # Adjust the x-axis limits for scrolling effect
        self.ax.set_xlim(self.x_data.min(), self.x_data.max())

        # Redraw the canvas
        self.canvas.draw()
