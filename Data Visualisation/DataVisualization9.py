import matplotlib.pyplot as plt
import numpy as np 

time=np.arange(12)
income=np.array([5,9,6,6,10,7,6,4,4,5,6,4])
exp=np.array([6,6,8,3,6,9,7,8,6,6,4,8])
fig,ax=plt.subplots(figsize=(8,8))
ax.plot(time,income,color='green')
ax.plot(time,exp,color='red')
ax.fill_between(time,income,exp,where=(income>exp),color='green',alpha=0.25,label='Positive',interpolate=True)
ax.fill_between(time,income,exp,where=(income<exp),color='red',alpha=0.3,label='Negative',interpolate=True)
plt.xlabel('time')
plt.ylabel('in/exp comparision')
ax.legend()
plt.show()