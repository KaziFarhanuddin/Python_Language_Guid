import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def show_points_and_line(points, m, b):
    min_x, max_x = points[0, 0], points[0, 0]
    for point in points:
        # print(point[0], point[1])
        plt.plot(point[0], point[1], 'o', color='green')
        if min_x>point[0]:
            min_x=point[0]
        elif max_x<point[0]:
            max_x=point[0]
    plt.plot([min_x, max_x], [(m*min_x+b), (m*max_x+b)], color='red')
    plt.gca().set(xlabel="Hours Studyed", ylabel="Marks", title='Hours Studyed VS Marks')
    plt.legend(['Student'])
    plt.show()


points = np.genfromtxt('data.csv', delimiter=',')
# split the values into two series instead a list of tuples
x, y = zip(*points)
x = np.array(x).reshape(-1, 1)
y = np.array(y)

regr = linear_model.LinearRegression()
regr.fit(x, y)

# check that the coeffients are the expected ones.
m = regr.coef_[0]
b = regr.intercept_
print(f' y = {m} * x + {b}')
print('error :',np.mean((regr.predict(x) - y) ** 2))

show_points_and_line(points, m, b)