import pandas as pd
import os

# Paths to the datasets using relative paths 
college_path = "data/cleaned_data/cleaned_college.csv"
highschool_path = "data/cleaned_data/cleaned_highschool.csv"

# check if the files are located in correct path
for path in [college_path, highschool_path]:
    if not os.path.exists(path):
        print(f"Error: File not found: {path}")

# load datasets 
df_college = pd.read_csv(college_path)
df_highschool = pd.read_csv(highschool_path)

# combine two datasets 
students = pd.concat([df_college, df_highschool])
print(students.head())
print(students.shape)

# define base_directory to correctly locate new directory
# base_directory = 'final_project/is477-fa24-jojo'

# Define the parent directory for data
parent_directory = os.path.join('data') # add base_directory inside the parenthesis if you have an error with repository
if not os.path.exists(parent_directory):
    os.makedirs(parent_directory, exist_ok=True)
# Define the new directory for cleaned data
new_directory = os.path.join(parent_directory, 'integrated_data')
file_name = 'students.csv'
file_path = os.path.join(new_directory, file_name)

# Create the directory structure if it doesn't exist
os.makedirs(new_directory, exist_ok=True)

# Save the cleaned DataFrame to the new directory
students.to_csv(file_path, index=False)

print(f"Cleaned DataFrame saved to {file_path}")

