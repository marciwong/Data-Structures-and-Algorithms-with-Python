# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:57:13 2016

@author: marcowong
"""

def squareRootBisection(x,eps=0.01):
    low = 0.0
    high = max(1.0,x)
    guess = (low + high)/2
    while abs(guess**2-x)>=eps:
        if guess**2<x:
            low=guess
        else:
            high=guess
        guess = (guess+x/guess)/2
    return guess