import os
import pandas as pd

# Define file paths for datasets
datasets = {
    "college": "data/cleaned_data/cleaned_college.csv",
    "highschool": "data/cleaned_data/cleaned_highschool.csv",
    "students_integrated": "data/integrated_data/students.csv"
}

# Ensure the datasets exist in the correct location
for name, file_path in datasets.items():
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Required dataset not found: {file_path}")
    else:
        print(f"Dataset verified: {file_path}")

# Verify and load datasets
def load_dataset(file_path):
    print(f"Loading dataset: {file_path}")
    data = pd.read_csv(file_path)
    print(data.shape)
    return data

# Load the datasets for further processing
college = load_dataset(datasets["college"])
highschool = load_dataset(datasets["highschool"])
students_integrated = load_dataset(datasets["students_integrated"])

# this data acquisition dataset shows that we have integrated two datasets correctly and they're all located in correct directories
# rows from shape 145 (college) + 649(highschool) = 794 (students)