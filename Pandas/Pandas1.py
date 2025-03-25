import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('auto-mpg.csv')
# print(df.to_string())
# print(df.shape)
# print("No. of rows",df.shape[0])
# print(df.describe(exclude=["float"]))

# df['horsepower']=df['horsepower'].replace('?',0.0)
# print(df.to_string())
# print(df.corr())

# pd.plotting.scatter_matrix(df,figsize=[15,15],marker='.',alpha=0.7)
# plt.show()