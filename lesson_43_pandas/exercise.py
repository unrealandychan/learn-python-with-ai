# Lesson 43: `pandas` - Data Analysis

import pandas as pd
import os

def main():
    # Construct the absolute path to sample_data.csv
    current_dir = os.path.dirname(__file__)
    csv_filepath = os.path.join(current_dir, 'sample_data.csv')

    print("\n--- Task 1: Load the `sample_data.csv` file into a DataFrame ---")
    # Your code here
    try:
        df = pd.read_csv(csv_filepath)
        print("DataFrame loaded successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at {csv_filepath}")
        return
    except Exception as e:
        print(f"An error occurred while loading the CSV: {e}")
        return

    print("\n--- Task 2: Print the first 5 rows of the DataFrame ---")
    # Your code here
    print(df.head())

    print("\n--- Task 3: Select and print the 'Name' column ---")
    # Your code here
    print("\nNames:")
    print(df['Name'])

    print("\n--- Task 4: Filter the DataFrame to show only people older than 30 ---")
    # Your code here
    older_than_30 = df[df['Age'] > 30]
    print("\nPeople older than 30:")
    print(older_than_30)

    print("\n--- Task 5: Calculate and print the average age ---")
    # Your code here
    average_age = df['Age'].mean()
    print(f"\nAverage Age: {average_age:.2f}")

    print("\n--- Task 6: Add a new column 'Is_Adult' (True if Age >= 18, False otherwise) ---")
    # Your code here
    df['Is_Adult'] = df['Age'] >= 18
    print("\nDataFrame with 'Is_Adult' column:")
    print(df.head())

    print("\n--- Task 7: Group the DataFrame by 'City' and calculate the average 'Age' for each city ---")
    # Your code here
    avg_age_by_city = df.groupby('City')['Age'].mean()
    print("\nAverage Age by City:")
    print(avg_age_by_city)

if __name__ == "__main__":
    main()