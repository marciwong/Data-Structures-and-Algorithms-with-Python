# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:57:13 2016

@author: marcowong
"""

gradeLevels = [80,50]

def printGrade (score, gradeLevels):
    if score>= gradeLevels[0]:
        print('distiction')
    elif score >= gradeLevels[1]:
        print('pass')
    else: print('fail')
    