rule all:
    input:
        "data/cleaned_data/cleaned_college.csv",
        "data/cleaned_data/cleaned_highschool.csv",
        "data/integrated_data/students.csv",
        "figures/heatmap_female.png",
        "figures/heatmap_male.png"

rule college_data_import:
    output:
        "data/cleaned_data/cleaned_college.csv"
    shell:
        "python scripts/college_data_import.py"

rule highschool_data_import:
    output:
        "data/cleaned_data/cleaned_highschool.csv"
    shell:
        "python scripts/highschool_data_import.py"

rule data_integration:
    input:
        college="data/cleaned_data/cleaned_college.csv",
        highschool="data/cleaned_data/cleaned_highschool.csv"
    output:
        "data/integrated_data/students.csv"
    shell:
        "python scripts/data_integration.py"

rule data_acquisition:
    input:
        college="data/cleaned_data/cleaned_college.csv",
        highschool="data/cleaned_data/cleaned_highschool.csv",
        integrated="data/integrated_data/students.csv"
    shell:
        "python scripts/data_acquisition.py"

rule data_analysis:
    input:
        "data/integrated_data/students.csv"
    output:
        "figures/heatmap_female.png",
        "figures/heatmap_male.png"
    shell:
        "python scripts/data_analysis.py"
