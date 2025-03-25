import matplotlib.pyplot as plt
import pandas as pd

x=range(1,6)
y=[1,4,6,8,4]
plt.fill_between(x,y,color='skyblue',alpha=0.2)
plt.plot(x,y,color='red',alpha=0.6)
plt.show()