from pandas.plotting import parallel_coordinates
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('auto-mpg.csv')

# pl=parallel_coordinates(df,"cylinders",cols=['cylinders','mpg','origin'],color=['red','blue','yellow','orange'])
# plt.show()

print(pd.crosstab(df['cylinders'],df['model year'],rownames=['cylinders'],colnames=['model year']))