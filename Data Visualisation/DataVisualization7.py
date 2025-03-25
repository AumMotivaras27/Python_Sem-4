import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x1= 5*np.random.rand(50)
x2= 5*np.random.rand(50)+25
x3= 30*np.random.rand(25)
x=np.concatenate((x1,x2,x3))

y1= 5*np.random.rand(50)
y2= 5*np.random.rand(50)+25
y3= 30*np.random.rand(25)
y=np.concatenate((y1,y2,y3))

c_array=['b']*50+['g']*50+['m']*25

plt.scatter(x,y,s=[50],marker='D',c=c_array)

plt.show()