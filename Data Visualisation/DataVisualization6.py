import matplotlib.pyplot as plt

v=[1,2,8,9,2,0,3,10]
plt.annotate(xy=[1,1],text='First Entry')
plt.plot(range(1,9),v)
plt.legend(['First'],loc=0)
plt.show()