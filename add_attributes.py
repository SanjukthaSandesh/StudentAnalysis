import pandas as pd
import numpy as np

# Load the existing CSV file
df = pd.read_csv(r'C:\Users\sanju\Downloads\Predicting-Student-Performance-Using-Machine-Learning-main (1)\Predicting-Student-Performance-Using-Machine-Learning-main\updated_stud.csv')  # Assuming stud.csv is the file in the current directory

# Add new attributes:

# Health (categorical: Excellent, Good, Average, Poor)
df['health'] = np.random.choice(['Excellent', 'Good', 'Average', 'Poor'], size=len(df))

# Going out with friends (categorical: Often, Sometimes, Rarely, Never)
df['going_out_with_friends'] = np.random.choice(['Often', 'Sometimes', 'Rarely', 'Never'], size=len(df))

# Absences (random number of absences, range from 0 to 20)
df['absences'] = np.random.randint(0, 21, size=len(df))

# Failure (random boolean values, 1 for failed, 0 for passed)
df['failure'] = np.random.choice([0, 1], size=len(df))

# Science Score (random values, range from 0 to 100)
df['science_score'] = np.random.randint(0, 101, size=len(df))

# Activities (categorical: Participates, Doesn't Participate)
df['activities'] = np.random.choice(['Participates', "Doesn't Participate"], size=len(df))

# Romantic Relationship (categorical: Yes, No)
df['romantic'] = np.random.choice(['Yes', 'No'], size=len(df))

# Travel Time (categorical: <15 min, 15-30 min, 30-60 min, >60 min)
df['travel_time'] = np.random.choice(['<15 min', '15-30 min', '30-60 min', '>60 min'], size=len(df))

#overall performance
df['overall_performance'] = df[['math_score', 'reading_score', 'writing_score', 'science_score']].mean(axis=1)

# Rename the columns
df = df.rename(columns={
    'overall_performance': 'math_score',  # Rename current 'overall_performance' to 'math_score'
    'math_score': 'overall'              # Rename original 'math_score' to 'overall'
})

# Verify the changes
print(df.head())




# Save the updated dataframe to a new CSV file
df.to_csv('stud_updated.csv', index=False)

print("New attributes with additional details have been added successfully.")
