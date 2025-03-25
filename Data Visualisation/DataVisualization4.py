import matplotlib.pyplot as plt

v1=[1,5,8,9]
v2=[3,8,9,2]
plt.plot(range(1,5),v1)
plt.plot(range(1,5),v2)
plt.savefig('fig1.png',format='png')
plt.show()