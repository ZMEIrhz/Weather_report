import sys
import matplotlib as plt
from matplotlib.widgets import Slider
plt.use('Qt5Agg')
from plots import WeatherPlot
from data_base_sql import login
from weather_ui import Ui_MainWindow
from login_ui import Ui_LoginWindow
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas as pd


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.log_in_button.clicked.connect(self.log_in)

    def log_in(self):
        username = self.ui.login_line.text()
        password = self.ui.password_line.text()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        if login(username, password):
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.canvas = MplCanvas()
            self.ui.verticalLayout_6.addWidget(self.canvas)
            WeatherPlot()
            self.canvas.draw()
            self.ui.comboBox_visual.currentTextChanged.connect(self.change_plot)

    def change_plot(self):
        parameter = 'Относительная влажность воздуха'
        dbase = "data_base22101.csv"
        if self.ui.comboBox_visual.currentText() == 'влажность':
            parameter = 'Относительная влажность воздуха'
            dbase = "data_base22101.csv"
        self.Plot, self.Axis = plt.subplots()
        df = pd.read_csv(dbase, encoding='windows-1251')
        df[parameter].interpolate(method='linear').plot()
        self.axis_position = plt.axes([0.2, 0.01, 0.6, 0.05], facecolor='White')
        self.slider_position = Slider(self.axis_position, 'Pos', 1.0, 150000.0)
        self.slider_position.on_changed(self.uupdate)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())