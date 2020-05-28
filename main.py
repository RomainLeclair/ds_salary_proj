# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:47:04 2020

@author: Leclair Romain
"""

import glassdorScrapping as gs
import pandas as pd

path = r'C:\Users\Leclair Romain\Desktop\ds_salary_project\chromedriver'
df = gs.get_jobs('data scientist', 100, False, path, 15)