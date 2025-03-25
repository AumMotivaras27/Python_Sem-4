import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('diabetes_unclean - Copy.csv')

# Display the statics analysis that are relevant for object type column.
print(df.describe(include='object'))

# Display the specific statics that are relevant for numeric type column.
print(df.describe())

# How many rows and columns are given in dataset.
print("No. of Rows =",df.shape[0])
print("No. of Columns =",df.shape[1])

# Check the missing value of dataset.
print(df.isna().sum())

# Replace the missing value in the column 'HbA1c' with their mean value.
df['HbA1c']=df['HbA1c'].fillna(df['HbA1c'].mean())
print(df.isna().sum())

# Drop the missing value of other columns.
df=df.dropna()
print(df.isna().sum())

# Check the information of your dataset.
print(df.info())

# In class column 'N ' and 'y ' replace with 'N' and 'y'.
df['CLASS']=df['CLASS'].replace('N ','N')
df['CLASS']=df['CLASS'].replace('Y ','Y')
print(df.CLASS.unique())

# Show the corelation between variables.
print(df.corr(numeric_only=True))
# print(df.corr())

# Draw the box plot for colmns AGE,Urea,HbA1c,Chol,TG,HDL,LDL,VLDL,BMI
c=['AGE','Urea','HbA1c','Chol','TG','HDL','LDL','VLDL','BMI']
plt.boxplot(df[c])
# plt.show()

# Visualize the columns Urea,HbA1c,TG,BMI for different age using parallel cordinates
pd.plotting.parallel_coordinates(df,'AGE',['Urea','HbA1c','TG','BMI'])
# plt.show()

# Remove the rows whose gender column has "f" and give frequency of "F" and 'M' in different class.
df.drop(df[df['Gender']=='f'].index)
print(df.shape)
print(pd.crosstab(df['Gender'],df['CLASS']))

# Rmove the outliers from 'HbA1c' and give shape of df.
quart1=df['HbA1c'].quantile(0.25)
quart2=df['HbA1c'].quantile(0.75)
IQR=quart2-quart1
low_val=quart1-1.5*IQR
high_val=quart2+1.5*IQR
df=df.loc[(df['HbA1c']>low_val) & (df['HbA1c']<high_val)]

print(df.shape)