# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:32:19 2020

@author: Leclair Romain
"""

import pandas as pd


#Ici on utilise la base du tutorial / Complication de récupérer les données 
df = pd.read_csv('https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/glassdoor_jobs.csv')


#Company name text only
#State field
#Age of company 
#Parsing of job description 

#############################################################################

# Cleaning Salary

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1'] # Drop Missing data represented by ' -1'
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

#Make Averae salary 
df['min_salary'] = min_hr.apply(lambda x: int((x.split('-')[0]).replace(':','')))
df['max_salary'] = min_hr.apply(lambda x: int((x.split('-')[1]).replace(':','')))
df['avg_salary'] = (df.min_salary + df.max_salary) /2

#############################################################################
#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1) # Selectioner où on a les données


#############################################################################
#State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0 , axis=1)


#############################################################################
#Age of company
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020-x)


#############################################################################
#Job description

df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#############################################################################
df = df.drop(['Unnamed: 0'], axis=1)
df.to_csv('salary_data_cleaned.csv', index=False)





