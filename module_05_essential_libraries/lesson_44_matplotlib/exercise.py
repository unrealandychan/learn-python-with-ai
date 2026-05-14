# Lesson 44: `matplotlib` - Data Visualization

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

    print("\n--- Task 1: Create a bar chart of Names vs. Ages ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    plt.bar(df['Name'], df['Age'], color='skyblue')
    plt.xlabel("Name")
    plt.ylabel("Age")
    plt.title("Ages of Individuals")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    print("\n--- Task 2: Create a scatter plot of Age vs. Score ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Age'], df['Score'], color='red', marker='o')
    plt.xlabel("Age")
    plt.ylabel("Score")
    plt.title("Age vs. Score Scatter Plot")
    plt.grid(True)
    plt.show()

    print("\n--- Task 3: Create a line plot of Scores ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    plt.plot(df['Name'], df['Score'], color='green', linestyle='-', marker='x')
    plt.xlabel("Name")
    plt.ylabel("Score")
    plt.title("Scores Over Individuals")
    plt.grid(True)
    plt.show()

    print("\n--- Task 4: Create a histogram of Ages ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    plt.hist(df['Age'], bins=5, edgecolor='black', alpha=0.7)
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.title("Distribution of Ages")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    print("\n--- Task 5: Create subplots for Age vs. Score and Names vs. Score ---")
    # Your code here
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    # Subplot 1: Age vs. Score
    axes[0].scatter(df['Age'], df['Score'], color='purple')
    axes[0].set_xlabel("Age")
    axes[0].set_ylabel("Score")
    axes[0].set_title("Age vs. Score")
    axes[0].grid(True)

    # Subplot 2: Names vs. Score
    axes[1].bar(df['Name'], df['Score'], color='orange')
    axes[1].set_xlabel("Name")
    axes[1].set_ylabel("Score")
    axes[1].set_title("Names vs. Score")
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout() # Adjusts subplot params for a tight layout
    plt.show()

    print("\n--- Task 6: Save one of the plots to a file (e.g., 'age_bar_chart.png') ---")
    # Your code here
    plt.figure(figsize=(8, 6))
    plt.bar(df['Name'], df['Age'], color='blue')
    plt.xlabel("Name")
    plt.ylabel("Age")
    plt.title("Ages of Individuals (Saved Plot)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    save_path = os.path.join(current_dir, 'age_bar_chart.png')
    plt.savefig(save_path)
    print(f"Plot saved to {save_path}")
    # plt.show() # Uncomment to display the saved plot as well

if __name__ == "__main__":
    main()