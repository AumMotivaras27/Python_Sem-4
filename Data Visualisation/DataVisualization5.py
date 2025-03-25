import matplotlib.pyplot as plt

v=[0,5,8,9,2,0,3,10]
ax=plt.axes()
ax.set_xticks([1,2,3,4,5,6,7,8])
ax.set_yticks([0,1,2,3,4,5,6,7])
plt.plot(range(1,9),v,'-.')
plt.show()