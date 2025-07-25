import pandas as pd
df= pd.read_csv('c:\\Users\\d\\Downloads\\Ecommerce Purchases.zip')
#display the first 10 rows
print(df.head(10))
#Display the last 10 rows
print(df.tail(10))
#display the  describle values
print(df.describe())

#data  cleaning 
print(df.isnull().sum())
print(df.drop_duplicates(inplace=True))
print(df.fillna('unknown'))
print(df.dropna())
#

# Top 5 most common email providers
df['Email Provider'] = df['Email'].apply(lambda x: x.split('@')[1])
print(df['Email Provider'].value_counts().head())

# Most popular browser
print(df['Browser Info'].value_counts().head())

#highest purchase price
print(df['Purchase Price'].value_counts().max())

#lowest purchase price
print(df['Purchase Price'].value_counts().min())

#filletring examples
amex_high = df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)]

# Total revenue by job
print(df.groupby('Job')['Purchase Price'].sum().sort_values(ascending=False))
print(df.groupby('Language')['Purchase Price'].sum().sort_values(ascending=True))




