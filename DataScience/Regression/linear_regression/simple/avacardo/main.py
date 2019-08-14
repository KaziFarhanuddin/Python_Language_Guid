import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

file = pd.read_csv('avocado.csv')[:800]
file

data = pd.DataFrame({'bags':file['Total Bags']/10000, 'volume':file['Total Volume']/1000000, 'price':file['AveragePrice']})
data

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression() 
model = regressor.fit(np.array(np.array(data['volume']).reshape(-1, 1), np.array(data['bags']).reshape(-1, 1)), np.array(data['price'], datatype=float64)) 
