import pandas as pd
#import hvplot.pandas
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class WeatherPlot():
    def __init__(self):
        self.Plot, self.Axis = plt.subplots()
#iloc[:150000]
        #plt.figure(figsize=(8, 4))
        df = pd.read_csv("data_base22101.csv", encoding = 'windows-1251')
        df2 = pd.read_csv("Предсказание_Терпяй-Тумса.csv", encoding='windows-1251')
        df['Температура воздуха по сухому термометру'].interpolate(method='linear').plot()  # первый график
        df2['Прогноз температуры'].interpolate(method='linear').plot()  # второй график нужно что-то придумать с числом среза
        plt.legend()
        plt.title('Погода Терпяй-Тумса')
        plt.ylabel('Температура (°C)')
        plt.xlabel('Дата')
        self.axis_position = plt.axes([0.2, 0.1, 0.6, 0.05], facecolor='White')
        self.slider_position = Slider(self.axis_position, 'Pos', 1.0, 170000.0)
        self.slider_position.on_changed(self.update)

        plt.show()

    def update(self, val):

        pos = self.slider_position.val
        self.Axis.axis([pos, pos + 200, -70, 60])
        self.Plot.canvas.draw_idle()




if __name__ == '__main__':
    WeatherPlot()