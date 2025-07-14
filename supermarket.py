import pandas as pd
import json
import requests

url = "https://raw.githubusercontent.com/chef-boneyard/supermarket/master/data_bags/apps/supermarket.json"
response = requests.get(url)
data = json.loads(response.text)


df = pd.json_normalize(data)

print(" First 5 rows:")
print(df.head())

print("\n DataFrame Info:")
print(df.info())

print("\n Columns:")
print(df.columns)

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Summary Statistics (if numeric):")
print(df.describe(include='all'))

print("\n Data Types:")
print(df.dtypes)
