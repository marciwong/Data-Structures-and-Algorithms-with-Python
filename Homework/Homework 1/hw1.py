# -*- coding: utf-8 -*-
"""

String conversion: slash-date format to dash-date format


"""
def dateConversion(dateString):
    """
    input: dateString: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/17 (assume valid dates)
    Assume European date ordering (day-month-year). 
    Assume also that two-digit years are in the past century (1917-2016 is "past century", 2017- is not...).
    output: returnString: string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1917
    """
    
    dateAsList = dateString.split('/') # split slash format string into a list - this may be useful...
        
    dayString = dateAsList[0]
    monthString = dateAsList[1]
    yearString = dateAsList[2]
        
    return convertDay(dayString)+'-'+convertMonth(monthString)+'-'+convertYear(yearString)    

def convertDay(dayString):
    """ 
    input: string containing day number in slash-date format
    output: string containing day number in dash-date format
    """ 
    if len(dayString)<2:
        dayString='0'+dayString

    return dayString

def convertMonth(monthString):
    """ 
    input: string containing month number in slash-date format
    output: string containing month number in dash-date format
    """   
    if len(monthString)<2:
        monthString='0'+monthString

    return monthString

def convertYear(yearString):
    """ 
    input: string containing year number in slash-date format
    output: string containing year number in dash-date format
    """
    if len(yearString)!=4:
        if 17<=int(yearString)<=99:
            yearString = '19' + yearString
        else:
            yearString = '20'+ yearString
    
    return yearString
    

def testDateConversion():
    """ function to test your date conversion function
    """
    for dateString in ['19/8/16','1/12/1898','1/1/17']:
        # should return '19-08-2016','01-12-1898','01-01-1917' 
        print(dateString)
        print(dateConversion(dateString))


#testDateConversion()


##### 
# Complete robust version below

def dateConversionRobust(dateString):
    """
    input: dateString: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/17 (DO NOT assume valid date inputs)
    Use European date ordering (day-month-year). 
    Assume that two-digit years are in the past century (1917-2016 is "past century", 2017- is not...).
    output: returnString: string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1917
    if not a valid date, return None
    """    

    try:
        std_date = dateConversion(dateString)
        checkdate(std_date)
    except:
        print('Not a valid date')
        return None
    return std_date


def checkdate(dateString):
          
    dateAsList = dateString.split('-')  
    day = int(dateAsList[0])
    month = int(dateAsList[1])
    year = int(dateAsList[2])

    if month in (1, 3, 5, 7, 8, 10, 12):
        if day >= 32:
            raise Exception('Not a valid day')

    if month in (4, 6, 9, 11):
        if day >= 31:
            raise Exception('Not a valid day')
            
    if leapyear(year) == True:
        if day >= 30:
            raise Exception('Not a valid day')     
    else:       
        if day >= 29:
            raise Exception('Not a valid day')
        
def leapyear(year): 
    if year % 4 == 0:
      return True
    elif year % 100 == 0:
      return False
    elif year % 400 == 0:
      return True
    else:
      return False

def testDateConversionRobust():
    """ function to test your date conversion function
    """
    for dateString in ['19/8/16','1/12/1898','1/1/17','32/12/2016', 'not a date string']:
        # should return '19-08-2016','01-12-1898','01-01-1917', None, None
        print(dateString)
        print(dateConversionRobust(dateString))

testDateConversionRobust()