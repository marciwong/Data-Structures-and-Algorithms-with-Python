# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 10:15:55 2016

@author: marcowong
"""

import pandas as pd
import csv
import numpy
import math

df = pd.read_csv('/Users/marcowong/Documents/Imperial College/Term 1/Data Structures and Algorithms with Python/Homework/Group Project/SP_500_close_2015.csv')

def readNamesIntoDict():
    dN = dict()
    input_file = csv.DictReader(open("/Users/marcowong/Documents/Imperial College/Term 1/Data Structures and Algorithms with Python/Homework/Group Project/SP_500_firms.csv"))
    for row in input_file:
        #print(row)
        dN[row['Symbol']] = [row['Name'],row['Sector']]
    return dN

def readPricesIntoDict():
    input_file = csv.DictReader(open('/Users/marcowong/Documents/Imperial College/Term 1/Data Structures and Algorithms with Python/Homework/Group Project/SP_500_close_2015.csv', 'r')) 
    d = dict()
    for row in input_file:
        for column, value in row.items():
            d.setdefault(column, []).append(value)
    return d

def calculateCompanyDetails():
    companyToPricesDict = readPricesIntoDict()

    companyDetailsDict = dict()

    # Min / max sum of daily return
    maxSumOfDailyReturns = 0
    maxSumOfDailyReturnsCompany = ''
    minSumOfDailyReturns = math.inf
    minSumOfDailyReturnsCompany = ''

    # Min / max mean of daily return
    maxMeanOfDailyReturns = 0
    maxMeanOfDailyReturnsCompany = ''
    minMeanOfDailyReturns = math.inf
    minMeanOfDailyReturnsCompany = ''

    # Min / max standard deviation
    maxStddev = 0
    maxStddevCompany = ''
    minStddev = math.inf
    minStddevCompany = ''

    companyNames = list(companyToPricesDict.keys())
    companyNames.remove('Date')

    for companyName in companyNames:
        prices = list(map(float, companyToPricesDict[companyName]))
        
        # Calculate standard deviation and daily returns in a single for loop

        # Can use numpy.std() here instead
        # pricesInFloat = map(numpy.float, prices)
        # stddev = numpy.std(pricesInFloat)
        sumOfPricesSq = 0
        dailyReturns = []
        pricesSqList = []
        for i in range(len(prices)):
            
            # Calculate daily returns
            if i != 0:
                dailyReturn = (prices[i] - prices[i-1]) / prices[i-1]
                dailyReturns.append(dailyReturn)
        
        sumOfDailyReturns = sum(dailyReturns)
        meanOfDailyReturns = (sumOfDailyReturns / float(len(dailyReturns)))
                  
        for j in range(len(dailyReturns)): 

            # Calculate std
            pricesSq = math.pow(( dailyReturns[j] - meanOfDailyReturns), 2)
            pricesSqList.append(pricesSq)
        sumOfPricesSq = sum(pricesSqList)
        stddev = math.sqrt((1 / ((len(dailyReturns) - 1))) * (sumOfPricesSq))
        
        for x in range(len(dailyReturns)):
            if daiLyReturns[x] > maxDailyReturns:
                maxDailyReturns = dailyReturns[x]
                maxDailyReutrnsCompany = companyName
            if dailyReturns[x] < minDailyReutnrs:
                minDailyReturns = dailyReturns[x]
                minDailyReutrnsCompany = companyName

        # Find the max / min DailyReturn
        if DailyReturns > maxDailyReturns:
            maxSumOfDailyReturns = sumOfDailyReturns
            maxSumOfDailyReturnsCompany = companyName
        
        if sumOfDailyReturns < minSumOfDailyReturns:
            minSumOfDailyReturns = sumOfDailyReturns
            minSumOfDailyReturnsCompany = companyName

        # Find the max / min  mean of DailyReturn
        if meanOfDailyReturns > maxMeanOfDailyReturns:
            maxMeanOfDailyReturns = meanOfDailyReturns
            maxMeanOfDailyReturnsCompany = companyName
        
        if meanOfDailyReturns < minMeanOfDailyReturns:
            minMeanOfDailyReturns = meanOfDailyReturns
            minMeanOfDailyReturnsCompany = companyName    
           
        # Find the max / min standard deviation
        if stddev > maxStddev:
            maxStddev = stddev
            maxStddevCompany = companyName
            
        if stddev < minStddev:
            minStddev = stddev
            minStddevCompany = companyName
                     
        companyDetailsDict[companyName] = {'sumOfDailyReturns' : sumOfDailyReturns, 'meanOfDailyReturns' : meanOfDailyReturns, 'stddev' : stddev}
              
    print('Max sum of daily return company: ', maxSumOfDailyReturnsCompany)
    print(maxSumOfDailyReturns)
    print('Min sum of daily return company: ', minSumOfDailyReturnsCompany)
    print(minSumOfDailyReturns)
    print('Overall the best performance company: ', maxMeanOfDailyReturnsCompany)
    print(maxMeanOfDailyReturns)
    print('Overall the worst performance company: ', minMeanOfDailyReturnsCompany)
    print(minMeanOfDailyReturns)
    print('Company has the most volatility: ', maxStddevCompany)
    print(maxStddev)
    print('Company has the least volatility: ', minStddevCompany)
    print(minStddev)

def varCovMat():
    companyToPricesDict = readPricesIntoDict()

    allCompanyNames = list(companyToPricesDict.keys())
    allCompanyNames.remove('Date')

    numberOfCompanies = len(allCompanyNames)

    covarianceMatrix = [[0] * numberOfCompanies] * numberOfCompanies
    
    for i in range(numberOfCompanies):
        for j in range(numberOfCompanies):
            companyA = allCompanyNames[i]
            companyB = allCompanyNames[j]
            
            pricesOfCompanyA = list(map(float, companyToPricesDict[companyA]))
            pricesOfCompanyB = list(map(float, companyToPricesDict[companyB]))

            sumOfProducts = 0
            sumOfCompanyASquare = 0
            sumOfCompanyBSquare = 0
            for k in range(len(pricesOfCompanyA)):
                sumOfProducts += pricesOfCompanyA[k] * pricesOfCompanyB[k]
                sumOfCompanyASquare += math.pow(pricesOfCompanyA[k], 2)
                sumOfCompanyBSquare += math.pow(pricesOfCompanyB[k], 2)

            covariance = ((numberOfCompanies * sumOfProducts) - (sum(pricesOfCompanyA) * sum(pricesOfCompanyB))) / ((math.sqrt((numberOfCompanies * sumOfCompanyASquare) - math.pow(sum(pricesOfCompanyA), 2))) * (math.sqrt((numberOfCompanies * sumOfCompanyBSquare) - math.pow(sum(pricesOfCompanyB), 2))))

            covarianceMatrix[i][j] = covariance

calculateCompanyDetails()



