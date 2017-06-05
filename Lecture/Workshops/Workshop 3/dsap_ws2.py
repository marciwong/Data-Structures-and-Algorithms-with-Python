# -*- coding: utf-8 -*-
"""

DSAP Workshop 2

"""

##########################################

#####
# Linear seach

def linearSearch(A,x):
    for elem in A:          
        if elem == x:
            return True
    return False           
    
y = 6
A = [3,8,11,9,4]
found = linearSearch(A,y)

#%%
# Binary search

def binarySearch(A,x,low,high):
    """Assumes A is a list with elements in ascending order.
    	   x is the element we're searching for.
	   low and high are indices of the list in between which we search.
        Returns True if x is in A and False otherwise"""

    if low >= high: # nothing left to search
        if A[low] == x: 
            return True
        else:
            return False
    
    midpoint = (low + high) // 2 # integer division // to divide roughly in half
    # print(midpoint)
    if A[midpoint] == x:
        return True # found it!
    elif A[midpoint] > x:
        return binarySearch(A,x,low,midpoint-1) # why midpoint-1?
    else:
        return binarySearch(A,x,?,?)

      
      
# Test
y = 24
A = [9,24,32,56,57,59,61,99]
found = binarySearch(A,y,0,len(A)-1)      
  
#%%
# Generate random sorted lists and time performance
import random
y = 20
size = 1000000
# We use a "list comprehension" to generate the list
A = sorted([random.randint(0,1000) for r in range(size)]) 

%timeit binarySearch(A,y,0,len(A)-1)      
%timeit linearSearch(A,y) 

#%%
##########################################
# Sorting

#####
# Selection sort

def selectionSort(A):
    """Assumes A is a list (whose elements can be compared).
        Returns sorted list"""
    for prefixSize in range(len(A)): # each iteration moves one element to prefix from suffix
        iMin = prefixSize # initialize index of minimum value to the beginning of the suffix
        for i in range(prefixSize,len(A)): # find the minimum element in the suffix
            # store index of minimum value in iMin, go through each element, update to find smallest
            if A[i] < A[iMin]:
                iMin = i
        # you can swap elements by a single operation x,y = y,x
        A[prefixSize], A[iMin] = ?, ?     
    return A   


A = [3,8,11,9,4,9,3,2,1]
print(selectionSort(A))


#%%
#####
# Built-in methods

# In Python, searching a list is easy using built-in methods:

A = [3,8,11,9,4]
4 in A
A.sort()
B = sorted(A,reverse=True)



#%%
#####
# Extra: Fortune 500

# You can read the data into lists

def readF500ToList():
    """ read fortune 500 data into a list where each element is a list of a row of csv data """
    import csv
    s = []
    with open('fortune500.csv', 'r') as csvfile:
        f500reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in f500reader:
            s.append(row)
    return s
    
F500list = readF500ToList() # a list of lists
print(F500list[11000:11500])


# Alternatively, you can read the data using the pandas library

import pandas as pd

def readF500ToPandas():
    """ read fortune 500 data into pandas dataframe """
    df = pd.read_csv('fortune500.csv')
    return df
    

F500df = readF500ToPandas() # This is a pandas "dataframe" used to organise data


# Some useful pandas commands

df[:3] # Get the first three lines of data
df.columns # Get the columns in your data
df.describe() # Get summary statistics

# Get the specified two columns of data for only year 2005
s = df.loc[df.Year == 2005,['Company','Revenue (in millions)']] 

# Get the specified two columns of data for only the first year using indices
s = df.loc[0:499,['Company','Revenue (in millions)']] 


#%%
#####
# Extra: Merge sort


def merge(left, right):
    """Assumes left and right are sorted lists and
         compare defines an ordering on the elements.
       Returns a single sorted list."""
    
    # Give loop structure to begin with
   
    result = []
    i = 0
    j = 0
    
    while (i < len(left) and j < len(right)):
        # Loop through both lists comparing their items: 
        # In each iteration append the smallest item to result
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        # If there are elements left in left, append them
        result.append(left[i])
        i += 1
    while (j < len(right)):
        # If there are elements left in right, append them
        result.append(right[j])
        j += 1
    return result

def mergeSort(L):
    """Assumes L is a list. Sorts recursively and uses merge to combine results.
    Returns a new sorted list."""
    if len(L) < 2: # Base case
        return L[:]
    else: # General case
        middle = # split st middle index to divide into left and right sides
        left = # recursively sort left side
        right =  # recursively sort right side
    return merge(left, right) # combine two sides using merge


A=[random.randint(0,1000) for r in range(10)]   
print(mergeSort(A))





