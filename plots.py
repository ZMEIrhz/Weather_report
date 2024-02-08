import pandas as pd
#import hvplot.pandas
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class WeatherPlot():
    def __init__(self, parameter = 'Относительная влажность воздуха', dbase = "data_base22101.csv", AX = None):
        self.Plot, self.Axis = plt.subplots()

        df = pd.read_csv(dbase, encoding = 'windows-1251')
        df[parameter].interpolate(method='linear').plot(ax=AX)
        self.axis_position = plt.axes([0.2, 0.01, 0.6, 0.05], facecolor='White')
        self.slider_position = Slider(self.axis_position, 'Pos', 1.0, 150000.0)
        self.slider_position.on_changed(self.update)

        super(WeatherPlot, self).__init__()
        if __name__ == '__main__':
            plt.show()




    def update(self, val):
        pos = self.slider_position.val
        self.Axis.axis([pos, pos + 10, 0, 110])
        self.Plot.canvas.draw_idle()

if __name__ == '__main__':
    WeatherPlot()