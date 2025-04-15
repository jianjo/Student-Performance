# Status Report 
Team jojo: Jian Jo & Jocelyn Yang 
date: November 15, 2023 
## Introduction 
This status report presents the progress of our final project for IS 477, titled "Analysis of Gender-Specific Predictors of Academic Success and Dropout Rates." As mentioned in the previous initial project plan file, our primary research question is: 

"Are there gender-specific predictors of academic success and dropout? How do factors like study time, parental influence, and extracurricular involvements differ between genders in relation to academic outcomes?"

This report includes:
* Updates on each task outlined in our project plan, with references to specific artifacts in our GitHub repository.
* An updated timeline stating the status of each task and completion dates.
* Descriptions of any changes made to our project plan based on the current progress.
* Evidence of progress through artifacts committed to GitHub.

Also, we obtained two datasets from the UCI Machine Learning Repository to address the research question:
    1. Student Performance Dataset 
    2. Predict Students' Dropout and Academic Success Dataset 

## Task Updates and Artifacts 
### 1. Acquire Datasets from Two Sources 
- status: completed
- artifacts: 
    - Data Acquisition Script: scripts/data_acquisition.py
    - Raw Datasets: 
        - student performance dataset: data/raw/student_performance.csv 
        - predict students' dropout dataset: data/raw/student_dropout.csv
- description: We automated the dataset acquisition process using data_acquisition.py. This script downloads the datasets and saves them to the '''data/raw/''' directory. The script ensures reproducibility and proper storage format, verified using checksums. 

### 2. Transparent Data Profiling and Quality Assessment
- status: completed 
- artifacts: 
    - profiling reports: 
        - reports/data_profiling_student_dropout.md
        - reports/data_profiling_student_performance.md
    - profiling script: report_script.py 

- description: we did data profiling using the 'report_script.py.' This file generates detailed descriptive statistics for both datasets. The reports are saved in the folder called reports. They are the markdown files and identify key characteristics and potential data quality issues like missing values, outliers in student academic performance grades, and categorical data inconsistencies. 

## 3. Data Cleaning
- status: completed 
- artifacts: 
    - scripts/data_cleaning_student_dropout.py
    - scripts/data_cleaning_student_performance.py
- description: from this task, the data cleaning scripts handle the issues found in the profiling stage. The list below are what we got to fix:
    - Standardized categorical labels like such as gender (`M`/`F`)
    - Handled missing values in critical variables using appropriate imputation techniques
    - Removed duplicate records to ensure data integrity
    - Normalized numeric fields, such as grades, for consistency
after these scripts, we could obtain cleaned datasets and they're stored in 'data/cleaned/'. 

## 4. Data Integration 
- status: completed
- artifacts: 
    - script: scripts/data_integration.py
    - plan: docs/data_integration_plan
- description: we merged the 2 datsets based on shared keys ('student_id' and 'gender'). We have resolved data type mismatches, standardized column names, handled missing values by imputing/labeling them as "unknown", and performed an inner join to retain only overlapping records. The integrated dataset called 'student_data_combined.csv' is saved in 'data/integrated/'. 

## 5. Implement Data Analysis and Visualization 
- status: in progress
- description: we're planning to perform exploratory data analysis (EDA) to see patterns and relationships. The expected (hypothesized) findings/relationships are differences in academic performance between genders, variation in study time and Extracurricular involvement by gender. Visualizations will be generated for summarizing findings and included in progress reports in the future. 

## 6. Workflow Automation
- status: not started 
- description: we will automate the end-to-end workflow using Python and Snakefile to ensure reproducibility. The workflow integrates data acquisition, profiling, cleaning, integration, and visualization processes. 

## Conclusion & Next Steps
We are done with foundational data preparation and integration tasks. Therefore, we just have to finish the steps: 
1. Finalize exploratory analysis and visualization 
2. Automate the complete workflow
3. Conduct internal reviews to refine the results and documentation
4. Archive the project with appropriate metadata and citations 


