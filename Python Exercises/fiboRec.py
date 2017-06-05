# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:40:04 2016

@author: marcowong
"""

def fiboRec(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fiboRec(n-1)+fiboRec(n-2)