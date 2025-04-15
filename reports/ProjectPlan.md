# Project Plan 
Final Project for IS 477 by team jojo — "jo"celyn and jian "jo."

## Overview 
**more details** 
We will be aiming to answer our research question to the best of our ability based on our datasets using tools that we have been taught in class. Specifically, we want to answer our question of if there are gender-specific predictors of academic success and dropouts as well as what factors (study time, parental influence, extracurricular activities, etc...) differ between genders in relation to academic outcomes. Some background information includes the fact that there are many "downstream" factors that can contribute to a person's upbringing and success. In this project, we want to look at some of those "downstream" factors that supposedly are not supposed to have an affect on someone's success such as their gender, parental influence, or neighborhoods, however, many times, these factors heavily contribute to a person's academic success, whether fairly or unfairly. The two datasets we will be using are from the UCI Machine Learning Respository, and will be on highschool education and college education as our second one. They will come cleaned, however, we will work on combining these two datasets. Overall, our goal of this project is to answer whether or not there are gender-specific predictors that can predict academic success and dropout rates of students, and how other factors like study time, parental influence, or extracurricular involvement differ between the two genders in relation to academic outcomes. 

## Research Question 
We will conduct an analysis on gender differences in success and retention predictors. Our research question is **"Are there gender-specific predictors of academic success and dropout? How do factors like study time, parental influence, and extracurricular involvement differ between genders in relation to academic outcomes?"**

We want to look at the two datasets (one looking at student performance and the other looking at student dropout and academic success) and we want to see if these two datasets can make any significant statistical result for the gender-specific predictors of academic success and dropouts. These datasets will come pre-cleaned, but we will work on combining them both.

Gender
Both datasets include a variable for gender (e.g., "sex" in Student Performance and "gender" in Predict Students' Dropout).
We want to see if there are similar factors influencing both datasets and if maybe one factor in one dataset seems to be heavily correlated with another factor in the other dataset. We also want to take a look and see if there are any significant or huge difference between the academic success of genders and if factors like study time, parental influence, and extracurricular activities differ between genders. It is intersting because although gender is not supposed to affect much outwardly, these factors will tell us if there is actually a pattern leading to a change in academic success whether you are a girl or a boy. We will also be creating visualizations for these patterns that we find, so that someone can properly see what influences what.

## Team 
We are planning to work on the project in person together, meaning that the workload will be fairly distributed among the two of us. 

- Jian Jo: focus on the data analysis part of the project more, however, will also be involved in writing up the reports and such.
- Jocelyn Yang: focus on writing down the findings on the report paper more, however, will also be involved when data cleaning and analysis.
  
## Datasets 
This project requires two datasets from APIs: one for the higher education and the other for the secondary education. 
- higher education: https://archive.ics.uci.edu/dataset/320/student+performance 
- secondary education: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success 

Both datasets include a variable for gender (e.g., "sex" in Student Performance and "gender" in Predict Students' Dropout). Therefore, we will perform integration and data preprocessing using OpenRefine and SQL.
## Timeline 

(Goals for the entirety of the project)
- Acquire datasets from at least two souces (Jian & Jocelyn)
- Automatic (programmatic) integration of datasets using Python/Pandas and/or SQL (Jian)
- Transparent data profiling, quality assessment, and cleaning (Jocelyn)
- Implement simple data analysis and/or visualization (Jian)
- Create a reproducible package (Jocelyn)
- Automated end-to-end workflow execution (Jocelyn)
- Accurate citation of data and software used (Jian)
- Create metadata describing your package (Jocelyn)
- Archive your project in a repository, obtaining a persistent identifier (Jian)

(A developed timeline)
1. Week 10: Oct 27 - Nov 2
- make a solid plan for this final project until the week 16 and decide two datasets and a research question for this project
- Set up a shared project environment to facilitate collaborative work.
- acquire the two datasets programmatically with integrity checks (checksums); if not, write down detailed steps to acquire data on ProjectPlan.md file under the datasets section, ensuring it's reproducible. (Jian)

2. Week 11: Nov 3 - Nov 9
- determine compatibility requirements for integration, noting column structures, data types, and schema.
- Create a reproducible package (Jocelyn), with clear instructions and dependencies. (Jian)
- Develop an automated end-to-end workflow to ensure smooth execution (Jocelyn).

  
3. Week 12: Nov 10 - Nov 16
- Perform comprehensive quality assessments (Jocelyn), documenting profiling outcomes in a transparent, reproducible format.
- Apply data cleaning techniques as needed (e.g., handling nulls, removing duplicates, etc.).
- Begin creating visualizations, ensuring reproducibility and clarity.
- Finalize and save visualizations in project files for future access.
- 2 page status report
- Write metadata describing your package (Jocelyn), covering data sources, analysis methods, and functionality.

  **status report submission on nov 15** 

4. Week 13: Nov 17 - Nov 23
- Create a reproducible package (Jocelyn), with clear instructions and dependencies.
- Review all analysis and visualizations, making any necessary adjustments.
- End goal: Finalize Package, Documentation, and Automation
- Ensure accurate citation of data and software used (Jian)

5. Week 13: Dec 2 - Dec 11 (Final Submission)
- GitHub release of your complete project
- Tie up any loose ends and final touches of the project
- Make sure everything is running smoothly and visualizations are clear
- Archive your project in a repository, obtaining a persistent identifier (Jian)
