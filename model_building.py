# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:51:55 2020

@author: Leclair Romain
"""
#LIBRAIRIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Data
df = pd.read_csv('data_eda.csv')
df.columns

#Selesction of Feature
df_model = df[['avg_salary','Rating','Size','Type of ownership','Sector','Industry','Revenue','num_comp','hourly',
             'employer_provided','job_state','same_state','age','company_txt', 'job_state', 'same_state',
             'age', 'python_yn', 'R_yn','spark', 'aws', 'excel', 'jomb_simp', 'seniority','desc_len']]

#Dummy_data
df_dum = pd.get_dummies(df_model)


#Prepare Data
X=df_dum.drop('avg_salary',axis=1)
y = df_dum['avg_salary'].values

#Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Multiple linear regresion
import statsmodels.api as sm
X_sm = X = sm.add_constant(X) # On ajotue une constante au modele
model =sm.OLS(y, X_sm)
model.fit().summary()

#With Sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error', cv = 3))


#Lasso regression
from sklearn.linear_model import Lasso
lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train, scoring='neg_mean_absolute_error', cv = 3))
#Chose the better alpha
alpha = []
error= []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring='neg_mean_absolute_error', cv = 3)))

plt.plot(alpha,error)

err = tuple(zip(alpha,error)) # combinaison des erreur et des alpha
df_err = pd.DataFrame(err, columns=['alpha','error'])
pd.DataFrame(err, columns=['alpha','error'])


#Random Forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring='neg_mean_absolute_error', cv = 3))

#Rf is better
#Let's tune him with GridSearchCV

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
paramters = {'n_estimators' : range(10,300,10),
             'criterion' : ['mse' , 'mae'],
             'max_features' : ['auto','sqrt','log2']}


gs = GridSearchCV(rf, paramters, scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train, y_train)

gs.best_score_
gs.best_estimator_


#Recheck lml
lm_l = Lasso(alpha= 0.13)
lm_l.fit(X_train, y_train)

#Test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

#Evaluate
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)

