# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:57:13 2016

@author: marcowong
"""

def toChars(s):
    s=s.lower()
    alphabet = 'abcdefghijklmnopqrxtuvwxyz'
    ans = ' '
    for c in s:
        for a in alphabet:
            if c==a:
               ans = ans+c            
    return ans
    
exampleStr = 'Never (1) odd or (2) even ...'
testStr = toChars(exampleStr)