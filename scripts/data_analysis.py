import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
student_path = "data/integrated_data/students.csv"  # relative path
df = pd.read_csv(student_path)

# Calculate correlation matrix without two columns that have objects
df2 = df.loc[:, ~df.columns.isin(['Pstatus', 'school'])]
df2_fem = df2[df2['sex'] == 1]
df2_mal = df2[df2['sex'] == 2]

corr_matrix_fem = df2_fem.corr()
corr_matrix_mal = df2_mal.corr()

# Define the parent directory for image/figures
#base_directory = 'is477-fa24-jojo' 
parent_directory = os.path.join('figures')
os.makedirs(parent_directory, exist_ok=True)  # Create the directory if it doesn't exist

file_name1 = 'heatmap_female.png'
file_name2 = 'heatmap_male.png'
file_path1 = os.path.join(parent_directory, file_name1)
file_path2 = os.path.join(parent_directory, file_name2)

# Create heatmap for females
fig_1 = plt.figure(figsize=(12, 10))
ax_1 = sns.heatmap(corr_matrix_fem, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
ax_1.set_title('Correlation Heatmap of Variables (female)')
fig_1.savefig(file_path1)  # Save the figure

# Create heatmap for males
fig_2 = plt.figure(figsize=(12, 10))
ax_2 = sns.heatmap(corr_matrix_mal, annot=True, cmap='crest', vmin=-1, vmax=1, center=0)
ax_2.set_title('Correlation Heatmap of Variables (male)')
fig_2.savefig(file_path2)  # Save the figure

# Display the heatmaps
plt.show()

print(f"Association figure is saved to {file_path1}")
print(f"Association figure is saved to {file_path2}")
