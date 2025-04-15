# student performance in secondary education (high school)
from ucimlrepo import fetch_ucirepo 
import pandas as pd
import os

# fetch dataset 
student_performance = fetch_ucirepo(id=320) 
  
# data (as pandas dataframes) 
X_h = student_performance.data.features 
y_h = student_performance.data.targets 

# data preprocessing
# columns - x variables 
# select which columns to use/merge 
col_selection_h = [
    'age', 'sex', 'activities',
    'romantic', "Medu", "Fedu",
    'Pstatus', 'studytime'
]
X_h = X_h[col_selection_h]
# add "school" column to identify the data entries from this dataset 
X_h["school"] = "highschool"

# Student Age (1: 18-21, 2: 22-25, 3: above 26)
def convert_age(numeric_age):
    if numeric_age < 18:
        return 0
    elif 18 <= numeric_age < 22:
        return 1
    elif 22 <= numeric_age:
        return 2
X_h['age'] = X_h['age'].apply(convert_age)
print(X_h['age'].value_counts())

# encode sex to numerical (1: female, 2: male)
def convert_sex(categorical_sex):
    if categorical_sex == 'F':
        return 1
    elif categorical_sex == 'M':
        return 2
X_h['sex'] = X_h['sex'].apply(convert_sex)
print(X_h['sex'].value_counts())

# encode romantic to numerical (1: yes, 2: no)
def convert_romantic(binary_romantic):
    if binary_romantic == 'yes':
        return 1
    elif binary_romantic == 'no':
        return 2
X_h['romantic'] = X_h['romantic'].apply(convert_romantic)
print(X_h['romantic'].value_counts())

# change activities to integer values (1:yes, 2:no)
X_h['activities'] = X_h['activities'].replace({'yes':1, 'no':2})

# target dataset 
y_h = y_h.drop(columns=['G1','G2'])
# rename G3 to final grade 
y_h = y_h.rename(columns={'G3':'final_grade'})

# turn final grade to letter grade scale 
def convert_grade(numeric_grade):
    # Convert 0-20 scale to 0-100 scale
    percentage = (numeric_grade / 20) * 100
    
    # Map percentage to categorical grade
    if percentage < 65:
        return 0  # Fail
    elif 65 <= percentage < 67:
        return 1  # DD
    elif 67 <= percentage < 73:
        return 2  # DC
    elif 73 <= percentage < 77:
        return 3  # CC
    elif 77 <= percentage < 83:
        return 4  # CB
    elif 83 <= percentage < 87:
        return 5  # BB
    elif 87 <= percentage < 93:
        return 6  # BA
    elif 93 <= percentage <= 100:
        return 7  # AA

y_h['final_grade'] = y_h['final_grade'].apply(convert_grade)
print(y_h['final_grade'].value_counts())

# i decided to keep 1 since the 1 from the high school dataset is <2 which almost doesn't mean anything as none study hours 
df_highschool = pd.concat([X_h, y_h], axis=1)
print(df_highschool.head())
print(df_highschool.shape)
print(df_highschool.info())

# define base_directory to correctly locate new directory
# base_directory = 'final_project/is477-fa24-jojo' 

# Define the parent directory for data
parent_directory = os.path.join('data') # add base_directory inside the parenthesis if you have an error with repository
if not os.path.exists(parent_directory):
    os.makedirs(parent_directory, exist_ok=True)
# Define the new directory for cleaned data
new_directory = os.path.join(parent_directory, 'cleaned_data')
file_name = 'cleaned_highschool.csv'
file_path = os.path.join(new_directory, file_name)

# Create the directory structure if it doesn't exist
os.makedirs(new_directory, exist_ok=True)

# Save the cleaned DataFrame to the new directory
df_highschool.to_csv(file_path, index=False)

print(f"Cleaned DataFrame saved to {file_path}")

# # metadata - original data
# print(student_performance.metadata) 
  
# # variable information - original data
# print(student_performance.variables) 
