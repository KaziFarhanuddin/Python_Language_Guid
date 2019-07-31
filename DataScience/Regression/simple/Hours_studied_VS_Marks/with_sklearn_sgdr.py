import numpy as np
from sklearn import linear_model

points = np.genfromtxt('data.csv', delimiter=',')
x, y = zip(*points)
y = np.array(y)
x = np.array(x).reshape(-1, 1)

clf = linear_model.SGDRegressor(max_iter=1000, tol=1e-3)
clf.fit(x, y)
print(np.mean((clf.predict(x) - y) ** 2))
