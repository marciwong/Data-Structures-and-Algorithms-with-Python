# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:48:32 2016

@author: marcowong
"""

def fiboIter(n):
    fibNumbers = [0,1]
    for i in range (2,n+1):
        if n==0:
            return n
        elif n==1:
            return n
        else:
            fibNumbers.append(-n)
    return fibNumbers[n]
    