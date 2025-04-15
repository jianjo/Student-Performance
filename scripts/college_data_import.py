from ucimlrepo import fetch_ucirepo 
import pandas as pd
import os

  
# fetch dataset 
higher_education_students_performance_evaluation = fetch_ucirepo(id=856) 

# data (as pandas dataframes) 
X_c = higher_education_students_performance_evaluation.data.features 
y_c = higher_education_students_performance_evaluation.data.targets 

# data preprocessing
# columns  
# select which columns to use/merge 
col_selection_c = [
    'Student Age', 'Sex', 'Regular artistic or sports activity',
    'Do you have a partner', "Mother's education", "Father's education",
    'Parental status', 'Weekly study hours'
]
X_c = X_c[col_selection_c]
dict_c = {'Student Age': 'age',
        'Sex': 'sex',
        'Regular artistic or sports activity': 'activities',
        'Do you have a partner': 'romantic',
        "Mother's education": 'Medu',
        "Father's education": 'Fedu',
        'Parental status': 'Pstatus',
        'Weekly study hours': 'studytime'}
 
# call rename () method to prepare integration 
X_c = X_c.rename(columns=dict_c)

# add "school" column to identify the data entries from this dataset 
X_c["school"] = "college"

# rows 
# change Medu & Fedu variables
X_c['Medu'] = X_c['Medu'].replace({5:4, 6:4})
X_c['Medu'].value_counts()
X_c['Fedu'] = X_c['Fedu'].replace({5:4, 6:4})
X_c['Fedu'].value_counts()
## 1: primary school, 2: secondary school, 3: high school, 4: higher education

# change Pstatus to binary (T-living together/A-apart)
X_c['Pstatus'] = X_c['Pstatus'].replace({1:'T', 2:'A', 3:'A'})
X_c['Pstatus'].value_counts()

# change studytimes values 
## numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours
## current 1: None, 2: <5 hours, 3: 6-10 hours, 4: 11-20 hours, 5: more than 20 hours)
# i decided to keep 1 since the 1 from the high school dataset is <2 which almost doesn't mean anything as none study hours 

X_c['studytime'] = X_c['studytime'].replace({5:4})


# target dataframe 
y_c = y_c.rename(columns={'OUTPUT Grade':'final_grade'})

df_college = pd.concat([X_c, y_c], axis=1)
print(df_college.head())
print(df_college.shape)
print(df_college.info())

# define the base directory to avoid new directory being located outside the designated directory 
# base_directory = 'final_project/is477-fa24-jojo'

# Define the parent directory for data
parent_directory = os.path.join('data') # add base_directory inside the parenthesis if you have an error with repository
if not os.path.exists(parent_directory):
    os.makedirs(parent_directory, exist_ok=True)
# Define the new directory for cleaned data
new_directory = os.path.join(parent_directory, 'cleaned_data')
file_name = 'cleaned_college.csv'
file_path = os.path.join(new_directory, file_name)

# Create the directory structure if it doesn't exist
os.makedirs(new_directory, exist_ok=True)

# Save the cleaned DataFrame to the new directory
df_college.to_csv(file_path, index=False)

print(f"Cleaned DataFrame saved to {file_path}")

# metadata - original dataset
#print(higher_education_students_performance_evaluation.metadata) 
  
# variable information - original dataset 
#print(higher_education_students_performance_evaluation.variables) 