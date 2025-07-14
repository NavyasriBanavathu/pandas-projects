import pandas as pd


def categorize_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"

print("Direct Outputs:")
print(categorize_age(5))    
print(categorize_age(17))    
print(categorize_age(28))   
print(categorize_age(45))    
print(categorize_age(70))    
print(categorize_age(-5))    


data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Elder'],
    'age': [5, 17, 28, 45, 70]
}
df = pd.DataFrame(data)


df['age_group'] = df['age'].apply(categorize_age)

print("\nDataFrame Output:")
print(df)

    

