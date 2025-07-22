
# Lesson 43: Solution

import pandas as pd

df = pd.read_csv('sample_data.csv')

print("First 3 rows:")
print(df.head(3))

print("\nNames:")
print(df['Name'])

print("\nPeople older than 30:")
print(df[df['Age'] > 30])
