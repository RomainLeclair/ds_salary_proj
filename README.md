# Data Science Salary Estimator : Project Overview
* I try to create a tool that estimates data Science salaries for learn
* Scraped over 1000 job description in USA from glassdor using python and selenium
* Data Cleaning and Engineered features
* Searching best Model to estimare average Salary
* Buil a client API with Flask


# Code ans Ressource Used
**Python Version**: 3.7

**Packages**: pandas, numpy, sklearn, matplotlib, seabonr, selenium, flask, json, pickle

**For Web Framework Requierments**: `pip install -r requierements.txt`

**Scrapper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium/blob/master/glassdoor%20scraping.ipynb

**Flask Porduction**: https://flask.palletsprojects.com/en/1.1.x/



# Web Scraping

We use glassdor for scrap each description of job. With each job, we got the following:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company headquarters
* Company size
* Company Founded Date
* Type of Ownership
* Industry 
* Sector
* Revenue
* Competitors


# Data Cleaning

After we scraping all the data i want . I need to clean this database.  Clean some features or delete features whose information dit not seem to me or not very important. I make this different steps:
 * Parsed numeric data out of salary
 * Made columns for employer provided salary and hourly wages
 * Removed rows without salary
 * Parsed rating out of company text
 * Made a new column for company state
 * Added a column for if the job was at the company's headquarters
 * Transformed founded date into age of company
 * Made columns for if different skills were listed in the job descriprion:
      * Python
      * R
      * Excel
      * AWS
      * Spark
 * Column for simplified job title and Seniority
 * Colum for description length
 
 
 # EDA
 
 I try to check the distributions of the data and the value counts for each categorical variable. Below are a few higlights from the pivot tables. Wich from my point of view are the most interesting.
 
 ![alt text](https://github.com/RomainLeclair/ds_salary_project/blob/master/heatmap.png)



