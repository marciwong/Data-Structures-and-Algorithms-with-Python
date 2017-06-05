# -*- coding: utf-8 -*-
"""

DSAP Workshop 5

"""

##########################################
# Building a knapsack of items
import random

class Item():
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result

# Helper functions

def buildItems(names,values,weights):
    # build list of items based on lists of names, values, and weights
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items


# These functions are used for sorting knapsack items according to max value, min cost, and bang-for-buck
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

# Let's create a bunch of random items
nItems = 10
values = []
weights = []
names = ['Item ' + str(i) for i in range(nItems)]
for i in range(nItems):
    values.append(random.randint(1,100))
    weights.append(random.randint(1,20))
    
it = buildItems(names,values,weights)


#%% Greegy algorithm for knapsack

def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, maxWeight >= 0,
         keyFunction maps elements of Items to floats"""
    
    # init: sort items    
    sortedItems = sorted(items, key=keyFunction, reverse = True)
    result = [] # list of items in knapsack 
    totalValue = 0.0 # knapsack value
    totalWeight = 0.0 # knapsack weight <= maxWeight
    
    # loop
    for i in range(len(sortedItems)):
        curItem = sortedItems[i]        
        if (totalWeight + curItem.getWeight()) <= maxWeight: # if can fit entire item into knapsack, do it, update its weight and value
            # code: add item to knapsack
            # code: increase knapsack weight and value 
    return result, totalValue   
    
# Run algorithm
it = buildItems(names,values,weights)
rs, v = greedy(it,20,density)

# Print results
print(v)
for item in rs:
    print(item)

#%%

##### 
# Brute force version

def powerSet(L):
    """
    Generator that returns all subsets of input L.
    """
    if len(L) <= 1:
        yield L # Google what this does!
        yield []
    else:
        for item in powerSet(L[1:]):
            yield [L[0]]+item
            yield item


s = powerSet([0,2,5])
 
for i in s:
    print(i)

def bruteForce(items, maxWeight):
    """ Brute-force knapsack solution
    """
    bestVal = 0.0
    bestSet = None
    pset = powerSet(items)
    for items in pset: # for each subset
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items: # add all items to knapsack
            itemsVal += item.getValue()
            itemsWeight += item.getWeight()
        if itemsWeight <= maxWeight and itemsVal > bestVal: # best solution and a feasible solution?
            bestVal = itemsVal
            bestSet = items
    return bestSet, bestVal

# Run --- compare with greedy solution
rs, v = bruteForce(it,20)

print(v)
for item in rs:
    print(item)


 



#%%

# Using Fantasy football data

from bs4 import BeautifulSoup
import codecs

def readPlayersHTML(html):
    """ Assumes html is a webpage formatted like https://fantasy.premierleague.com/player-list/
        These are ordered by position and wage
    """
    f=codecs.open(html, 'r','utf-8')
    data = f.read()
    soup = BeautifulSoup(data, 'lxml')
    s = []       
    for tr in soup.findAll('tr'):
        u = tr.findAll('td')
        u =  [x.text for x in u]
        s.append(u)
        
    s = list(filter(None, s))  # filter out empties  
    
    # create lists
    names = [i[0] for i in s]
    teams = [i[1] for i in s]
    wages = [i[3][1:] for i in s]
    values = [i[2] for i in s]
    
    return names,teams,wages,values

html = 'Player List - Fantasy Premier League.htm'
names,teams,wages,values = readPlayersHTML(html)

class Player(object):
    # Just like the Item class above
    def __init__(self, n, t, v, w, p):
        self.name = n
        self.team = t
        self.position = p
        self.value = int(v)
        self.weight = int(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getPosition(self):
        return self.position
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + self.position + ', ' + self.team + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result

# Create list of player objects

def buildPlayers(names,teams,values,wages): # change to take names, values, weights as input
    Players = []
    # assume ordered in order of position and wage - this is bad coding
    positions = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
    posIndex = 0
    for i in range(len(values)):
        if i>0:
            if float(wages[i]) > float(wages[i-1]):
                posIndex += 1
        # make sure wages are integer
        Players.append(Player(names[i], teams[i], values[i], int(float(wages[i])*10), positions[posIndex]))
    return Players

pl = buildPlayers(names,teams,values,wages)


# Solve problem with greedy algorithm


rs, v = greedy(pl,900,density)
print(v)
for item in rs:
    print(item)




#%%

# Greedy heuristic with team constraints

def greedyHeuristic(items, maxWeight, keyFunction, maxPlayers):
    """Assumes Items a list, maxWeight >= 0,
         keyFunction maps elements of Items to floats"""
    
    # max players for each position
    maxGoal = 1
    maxDef = 4
    maxMid = 4
    maxFW = 2
    
    # init: sort items    
    sortedItems = sorted(items, key=keyFunction, reverse = True)
    result = []
    totalValue = 0.0 # knapsack value
    totalWeight = 0.0 # knapsack weight <= maxWeight
    
    gl = 0
    df = 0
    md = 0
    fw = 0
    pl = 0
    
    # loop
    for i in range(len(sortedItems)):# give pseudocode
        curItem = sortedItems[i]        
        if (totalWeight + curItem.getWeight()) <= maxWeight and pl < maxPlayers: # if can fit item into knapsack, do it, update its weight and value
            plPos = curItem.getPosition()
            if plPos == 'Goalkeeper' and  gl < maxGoal:
                    gl += 1
                    result.append(curItem)
                    pl += 1
                    totalWeight += curItem.getWeight()
                    totalValue += curItem.getValue()
            elif plPos == 'Defender' and df < maxDef:
                    df += 1
                    result.append(curItem)
                    pl += 1
                    totalWeight += curItem.getWeight()
                    totalValue += curItem.getValue()
            elif plPos == 'Midfielder' and md < maxMid:
                    md += 1
                    result.append(curItem)
                    pl += 1
                    totalWeight += curItem.getWeight()
                    totalValue += curItem.getValue()
            elif plPos == 'Forward' and fw < maxFW:
                    fw += 1
                    result.append(curItem)
                    pl += 1
                    totalWeight += curItem.getWeight()
                    totalValue += curItem.getValue()
                
    return result, totalValue
    



maxPlayers = 11
budget = 900
rs, v = greedyHeuristic(pl,budget,density, maxPlayers)

for r in rs:
    print(r)

print(v)




