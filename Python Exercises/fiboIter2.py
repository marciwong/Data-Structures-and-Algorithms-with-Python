# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:06:39 2016

@author: marcowong
"""

def fiboIter(n):
    fibNumbers = [0,1]
    for i in range(2,n+1):
        n = fiboIter(n-1)+fiboIter(n-2)
    