
# Lesson 44: Solution

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../lesson_43/sample_data.csv')

# Bar chart
plt.figure(1)
plt.bar(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Ages of Individuals')

# Scatter plot
df['Salary'] = [50000, 60000, 70000, 80000, 90000]
plt.figure(2)
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary')

plt.show()
