# QB 34

import pandas as pd
df=pd.read_csv('car data.csv')

# 1. How Many ritz car are there with kms driven more than 30000km.
df=df.loc[(df['Car_Name']=='ritz') & (df['Kms_Driven']>30000)]
print(len(df))

# 2. How many Petrol cars are of the year 2017 and whose selling price > 10 lakhs. 
df=df.loc[(df['Fuel_Type']=='Petrol') & (df['Year']==2017) & (df['Selling_Price']>10)]
print(len(df))

# 3. How many swift cars are there with selling price < 4 Lakhs.
df=df.loc[(df['Car_Name']=='swift') & (df['Selling_Price']<4)]
print(len(df))

# 4. How many Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs.
df=df.loc[(df['Transmission']=='Automatic') & (df['Fuel_Type']=='Petrol') & (df['Year']==2015) & (df['Selling_Price']>10)]
print(len(df))

# 5. List out Vehicles with Automatic Transmission and selling price < 1 Lakh.
df=df.loc[(df['Transmission']=='Automatic') & (df['Selling_Price']<1)]
print(df)

# 6. How Many Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included).
df=df.loc[(df['Fuel_Type']=='Petrol') & (df['Kms_Driven']>50000) & (df['Year']>=2010) & (df['Year']<=2015)]
print(len(df))

# 7.List out the cars whose price difference between present price and selling price is > 15 lakhs.
df=df.loc[((df['Present_Price'])-(df['Selling_Price']))>15]
print(df)

# 8.How many Petrol vehicles are there whose kms driven < 5000km and selling price < 50000.
df=df.loc[(df['Fuel_Type']=='Petrol') & (df['Kms_Driven']<5000) & (df['Selling_Price']<0.5)]
print(len(df))
