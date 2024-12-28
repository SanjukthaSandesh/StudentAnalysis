import pandas as pd
import numpy as np

# Load the existing CSV file
df = pd.read_csv(r'C:\Users\sanju\Downloads\Predicting-Student-Performance-Using-Machine-Learning-main (1)\Predicting-Student-Performance-Using-Machine-Learning-main\Notebook\data\stud.csv')  # File is in the same directory

# Add a new column 'study_time' with random values between 1 and 10 (simulating hours of study time per day)
df['study_time'] = np.random.randint(1, 11, size=len(df))  # Random study time between 1 and 10 hours per day

# Add a new column 'screen_time' with random values between 1 and 8 (simulating hours of screen time)
df['screen_time'] = np.random.randint(1, 9, size=len(df))  # Random screen time between 1 and 8 hours per day

# Check the updated dataframe with the new attributes
print(df.head())

# Save the updated DataFrame back to a new CSV file
df.to_csv('updated_stud.csv', index=False)

print("Attributes added and new CSV saved as 'updated_stud.csv'")
