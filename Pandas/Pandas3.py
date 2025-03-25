import pandas as pd

df=pd.read_csv('sales_data.csv')

# print(df.isna().sum())  # Gives Sum of Null Cell

# print(df.dropna())      # Drop Null Value Row

# print(df.dropna(thresh=2))      # Drop Row in which null value is more than 2 

# print(df.dropna(how="all"))      # Drop Row in which all the values are null

# print(df.dropna(axis=0))        # Drop Row where null value is present

# print(df.dropna(axis=1))        # Drop Column where null value is  present

# print(df.to_string())

# print(df.dropna(subset=['sales','expenses']))       # Removes row where null value occurs in sales and expenes column

# df.dropna(subset=['sales'],inplace=True)              # It will update original dataframe

# print(df['sales'].fillna(0))

# print(df['sales'].fillna(df['sales'].mean(),inplace=True))

# print(df['expenses'].fillna(df['expenses'].median(),inplace=True))

print(df.to_string())