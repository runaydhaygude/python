# Pie chart
import matplotlib.pyplot as pyplot

data = [3, 4, 5]

pyplot.pie(data)
pyplot.show() # this blocks the thread


# Bubble plotting

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [3000, 6000, 5000, 8000, 11000, 9000, 10000]
weight = [100, 150, 2000, 200, 400, 300, 250]

pyplot.scatter(x_values, y_values, weight)
pyplot.show()