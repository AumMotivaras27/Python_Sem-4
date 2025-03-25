import pandas as pd

df=pd.read_csv('auto-mpg.csv')
# print(df[df['horsepower']=='?'])

df['horsepower']=pd.to_numeric(df['horsepower'].replace('?',0.0))

quart1=df['acceleration'].quantile(0.25)
quart2=df['acceleration'].quantile(0.75)
IQR=quart2-quart1
low_val=quart1-1.5*IQR
high_val=quart2+1.5*IQR

# df=df.loc[(df['acceleration']<low_val) | (df['acceleration']>high_val)]

df=df.loc[(df['acceleration']>low_val) & (df['acceleration']<high_val)]

print(df)