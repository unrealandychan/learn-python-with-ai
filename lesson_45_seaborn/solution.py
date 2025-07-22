
# Lesson 45: Solution

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../lesson_43/sample_data.csv')

# Boxplot
plt.figure(1)
sns.boxplot(x=df['Age'])
plt.title('Boxplot of Age')

# Violin plot
plt.figure(2)
sns.violinplot(x=df['Age'])
plt.title('Violin Plot of Age')

# Pair plot
sns.pairplot(df)

plt.show()
