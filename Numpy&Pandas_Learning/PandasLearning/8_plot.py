import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  plot data
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()

data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
# print(data.head())

data.plot()

# plot method:bar,hist,box,kde,area,scatter,hexbin,pie
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)

plt.show()
