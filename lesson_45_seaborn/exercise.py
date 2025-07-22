# Lesson 45: `seaborn` - Statistical Data Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

def main():
    # Construct the absolute path to sample_data.csv
    current_dir = os.path.dirname(__file__)
    csv_filepath = os.path.join(current_dir, 'sample_data.csv')

    # Load the data
    try:
        df = pd.read_csv(csv_filepath)
        print("DataFrame loaded successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at {csv_filepath}")
        return
    except Exception as e:
        print(f"An error occurred while loading the CSV: {e}")
        return

    print("\n--- Task 1: Create a boxplot of the 'Age' column ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df['Age'])
    plt.title("Boxplot of Age")
    plt.ylabel("Age")
    plt.show()

    print("\n--- Task 2: Create a violin plot of the 'Age' column ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    sns.violinplot(y=df['Age'])
    plt.title("Violin Plot of Age")
    plt.ylabel("Age")
    plt.show()

    print("\n--- Task 3: Create a scatter plot of 'Age' vs. 'Salary', with 'City' as hue ---")
    # Your code here
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x='Age', y='Salary', hue='City', data=df, s=100) # s for size of points
    plt.title("Age vs. Salary by City")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.grid(True)
    plt.show()

    print("\n--- Task 4: Create a histogram/KDE plot of the 'Score' column ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Score'], kde=True, bins=5, color='purple')
    plt.title("Distribution of Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

    print("\n--- Task 5: Create a pair plot of the numerical columns in the DataFrame ---")
    # Your code here
    # Select only numerical columns for pairplot
    numerical_df = df.select_dtypes(include=['number'])
    sns.pairplot(numerical_df)
    plt.suptitle("Pair Plot of Numerical Columns", y=1.02) # Adjust suptitle position
    plt.show()

    print("\n--- Task 6: Create a heatmap of the correlation matrix ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    correlation_matrix = numerical_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

if __name__ == "__main__":
    main()