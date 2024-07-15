# Project Name

## Overview

➡️ This project focuses on [briefly describe the project's objectives and scope]. It involves [mention the key tasks or analyses involved, e.g., data collection, cleaning, analysis, etc.].



## Key Steps Followed

### Understanding Requirements
➡️ The initial step involved clearly defining the project's objectives and understanding what specific data was necessary to achieve those goals. Discussions with stakeholders ensured alignment and clarity on the scope of the analysis.

### Data Collection and Cleaning
➡️ ata was gathered from various sources such as APIs, databases, or datasets. Data cleaning was crucial to ensure accuracy, consistency, and freedom from errors or inconsistencies. Tasks included handling missing values, removing duplicates, and standardizing formats.

### Exploratory Data Analysis (EDA)
➡️ Python tools like Pandas, Matplotlib, and Seaborn were used to explore cleaned data. Visualization techniques helped understand data distributions, identify outliers, and explore relationships between variables. Statistical analysis provided insights into data characteristics and patterns.

### Tool Selection and Optimization
➡️ Tools like Jupyter Notebook and Excel were selected based on analysis needs. Optimization focused on efficient code writing, database indexing, and streamlining data processing workflows for large datasets.

### Communication and Documentation
➡️ Clear communication of findings and methodologies was maintained throughout. The entire process, from data sources to analysis techniques and conclusions, was documented. This ensured transparency, reproducibility, and facilitated knowledge sharing.



## Overview
➡️ This repository contains scripts and files used for scraping internship data from Internshala, performing data cleaning and analysis, and visualizing insights using Power BI.

## Files Overview

### `duration_sorter.py`
- This script extracts the duration time from internship data, which was not feasible in Excel due to the format inconsistency.

### `first_analysis.pbix`
- Power BI file containing all analysis and visualizations performed on the scraped internship data.

### `formula-to-paste.xlsx`
- Excel file containing formulas to extract stipend amounts from text, accommodating various formats like:
  - ₹ 10,000 /month
  - ₹ 10,000-12,000 /month
  - ₹ 2,000 /month + Incentives

### `internship_data_og.xlsx`
- Original dataset scraped from Internshala, containing internship details.

### `location_sorter.py`
- Python script to sort and categorize internships based on location.

### `main.py`
- Main Python script for web scraping, utilizing multiprocessing for enhanced speed.

### `main4.py`
- Python script to automate profile parsing and URL generation for internships, reducing manual input requirements.

### `skills_sorter.py`
- Python script to identify the top 10 skills most in demand by employers from the scraped data.

### `time_elapsed.py`
- Python script to display the time taken for web scraping and processing.


## Usage Instructions
1. Clone the repository: https://github.com/Calamivathan/Internshala-web-scraper-with-visualization-.git

2. Install dependencies (if any) and ensure Python environment is set up correctly.
3. 
4. Execute the scripts as needed:
- Use `main.py` for initial data scraping.
- Utilize other scripts like `duration_sorter.py`, `location_sorter.py`, `skills_sorter.py`, and `time_elapsed.py` for specific data processing tasks.

## License
This project is licensed under the [MIT License](link-to-license) - see the LICENSE file for details.
