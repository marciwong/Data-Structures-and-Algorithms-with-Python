# -*- coding: utf-8 -*-
"""

HW2: technical analysis

"""

def movingAverage(prices, n):
    """ 
    #Input: prices is a list of prices (ordered in time), n is an integer
    #Calculates n-day moving average for prices
    Output: returns a list movingAverage with None for the first n-1 values in prices 
    and the appropriate moving average for the rest
    """
    timeLength = len(prices)
    movingAverage = [None]*timeLength
    for i in range(timeLength):
        if i < n-1:
            continue
        movingAverage[i] = float(sum(prices[i+1-n:i+1])) / float(n)
    return movingAverage


def testMovingAverage():
    """
    test your implementation of movingAverage
    """    
    prices = [2,3,4,5,8,5,4,3,2,1]
    n = 3
    ma3 = movingAverage(prices,n)
    print(ma3)
    print([None, None, 3.0, 4.0, 5.666666666666667, 6.0, 5.666666666666667, 4.0, 3.0, 2.0])
    n = 2
    ma2 = movingAverage(prices,n)
    print(ma2)
    print([None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5])


def crossOvers(prices1,prices2):
    """ 
    Identify cross-over indices for two equal-length lists of prices (here: moving averages)
    
    Input: two lists of prices (ordered by time)
    Output: returns list of crossover points: "crossovers"

    Each item in "crossovers" is a list [timeIndex,higherIndex], where:
    
    -timeIndex is the crossover time index
    
    -higherIndex indicates which price becomes higher at timeIndex: either 1 for first list or 2 for second list
    """
    crossovers = []    
    NoNone2 = prices2.count(None)
    length = len(prices2)
    
    for i in range(length):
        if i < NoNone2+1:
            continue
        if prices1[i] > prices2[i] and prices1[i-1] < prices2[i-1]:
           crossovers.append([i,1])
        elif prices1[i] <= prices2[i] and prices1[i-1] > prices2[i-1]:
           crossovers.append([i,2])
        elif prices2[i] > prices1[i] and prices2[i-1] < prices1[i-1]:
           crossovers.append([i,2])
        elif prices2[i] <= prices1[i] and prices2[i-1] > prices1[i-1]:
           crossovers.append([i,1])           
    return crossovers


def testCrossOvers():
    """
    test your implementation of crossOvers
    """
    #prices = [2,3,4,5,4,3,2,1,6,1]
    #list1 = movingAverage(prices,2)
    #list2 = movingAverage(prices,3)
    list1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    list2 = [None, None, 3.0, 4.0, 4.333333333333333, 4.0, 3.0, 2.0, 3.0, 2.6666666666666665]
    print(crossOvers(list1,list2))
    print([[5, 2], [8, 1]]) # correct result
    

testCrossOvers()

def makeTrades(money, prices, crossovers):
    """
    Given an initial cash position, use a list of crossovers to make trades
    
    Input: money - initial cash position; prices - list of prices (ordered by time); crossovers - list of crossovers     
    Output: currentValue - list of value of position (either in stock value or cash) at each time index    
    
    Assume each item crossovers[i] is a list [timeIndex,buyIndex]    
    
    Assume that buyIndex = 1 means that short-term MA becomes higher than long term at this timeIndex
    buyIndex = 2 means that long-term MA becomes higher than short term.    

    You would like to buy at any timeIndex where crossover's buyIndex indicates 1, sell at 2. 
    
    That is, you want to buy whenever SHORT-TERM MA becomes higher than LONG-term (AND you have a cash position),
    and sell when the opposite cross-over occurs (AND you have a stock position).
    
    Use all money/stock available to buy/sell at the current price: you will always hold either stocks or cash, but never both.

    Assume fractional stock quantities, no transaction fees.      
    """
    currentValue = []
    cashPosition = True
    noOfStock = 0.0
    for x in range(len(prices)):
        if x == crossovers[0][0]:
            toBuy = (crossovers[0][1] == 1)
            if cashPosition:
                currentValue.append(money)
                if toBuy:    
                  noOfStock = money / float(prices[x])
                  cashPosition = not cashPosition                
            else:
                money = noOfStock * float(prices[x])
                currentValue.append(money)              
                cashPosition = not cashPosition
                
            crossovers.pop(0)    
            
        elif not cashPosition:
            money = noOfStock * float(prices[x])
            currentValue.append(money)
        else:
            currentValue.append(money)
            
    return currentValue

def testTrades():
    """
    test your implementation of makeTrades
    """
    prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    #list1 = movingAverage(prices,2) # this is how the crossovers were generated from the prices...
    #list2 = movingAverage(prices,3)
    #cos = crossOvers(list1,list2)
    cos = [[5, 2], [8, 1], [10, 2], [11, 1], [15, 2]]
    startingMoney = 1000
    print(makeTrades(startingMoney, prices, cos))
    print([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000.0, 166.66666666666666, 833.3333333333333, 833.3333333333333, 952.3809523809523, 1190.4761904761904, 833.3333333333333, 1071.4285714285713])


testTrades()




##### 
# Test with actual stock data using pandas datareader

import pandas_datareader.data as web
from datetime import datetime # Perhaps useful for HW1...


def getStock(symbol, start, end):
    """
    Downloads stock price data from Yahoo Finance
    Returns a pandas dataframe.
    """
    df =  web.DataReader(symbol, 'yahoo', start, end)
    return df

def getClose(df):
    """
    Returns stock price dataframe's adjusted closing price as a list
    """
    L = df['Adj Close'].values.tolist()
    return L
                

def MAvsBaH(n1,n2,stockCode,start,finish,startingMoney):
    """
    perform comparison between moving average crossover strategy and buy and hold
    Assume n1 < n2
    """
    
    # Get prices    
    stock = getStock(stockCode,start, finish)
    closingPrices = getClose(stock)
    
    # Moving averages
    ma1 = movingAverage(closingPrices,n1)
    ma2 = movingAverage(closingPrices,n2)  
    
    # Crossovers
    cos = crossOvers(ma1,ma2)
    
    # Make trades using crossover strategy, get list of values
    MAvalues = makeTrades(startingMoney,closingPrices,cos)    

    # Get buy and hold strategy values
    firstValue = closingPrices[n2-1] # start trading at same point in time
    BHvalues = [p/firstValue*startingMoney for p in closingPrices] # List comprehension for convenient looping
    
    print("Buy and hold: " + str(BHvalues[-1]))
    print("Crossover MA: " + str(MAvalues[-1]))
    
    return [BHvalues, MAvalues]



# Try with Nasdaq index
# Let's assume you can trade it like a stock at a price equal to the index (eg through an index fund)    
nasdaqCode = '^IXIC' 
n1 = 20
n2 = 50
start = datetime(1980,1,1)
finish = datetime(2015,12,31)
startingMoney = 1000
values = MAvsBaH(n1,n2,nasdaqCode,start,finish,startingMoney)

# Plotting
import matplotlib.pyplot as plt

plt.plot(values[0])
plt.plot(values[1])


