import pandas as pd


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)


print(" First 5 rows:\n", df.head())


print("\n Dataset Info:\n")
print(df.info())

print("\n Summary Statistics:\n", df.describe(include='all'))


print("\n Missing Values:\n", df.isnull().sum())


print("\n Value Counts for 'Sex':\n", df['Sex'].value_counts())
print("\n Value Counts for 'Embarked':\n", df['Embarked'].value_counts())


df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


df['Age'].fillna(df['Age'].median(), inplace=True)


df.drop(columns=['Cabin'], inplace=True)


df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

print("\n Average Survival Rate by Pclass:\n", df.groupby('Pclass')['Survived'].mean())


df.to_csv("cleaned_titanic.csv", index=False)


print("\n Final 5 Rows:\n", df.tail())
