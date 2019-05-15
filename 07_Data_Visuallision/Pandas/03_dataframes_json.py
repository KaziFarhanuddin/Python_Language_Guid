import pandas as pd

df = pd.read_json('json.json')

print(df)

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger
