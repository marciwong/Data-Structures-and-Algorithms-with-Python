# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:58:39 2016

@author: hpeura
"""

import pandas as pd


data = pd.read_csv('southKenHygiene.csv')

data.describe()


data.head(5)

d = data.dropna()


