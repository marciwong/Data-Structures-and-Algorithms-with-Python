# -*- coding: utf-8 -*-
"""

DSAP W3 solution

"""

class Attack():
    def __init__(self,name,attackType,damage):
        self.name = name
        self.attackType = attackType
        self.damage = damage
    
    def getAttackType(self):
        return self.attackType

    def getDamage(self):
        return self.damage
    
    def __str__(self):
        return self.name

class Monster():
    def __init__(self,name,monsterType,combatPoints,hitPoints,attacks):
        self.name = name
        self.monsterType = monsterType
        self.combatPoints = combatPoints
        self.hitPoints = hitPoints
        self.health = hitPoints
        self.attacks = attacks
        
    def getMonsterType(self):
        return self.monsterType

    def getCombatPoints(self):
        return self.combatPoints
    
    def getHealth(self):
        return self.health
    
    def gethitPoints(self):
        return self.hitPoints        
    
    def getAttacks(self):
        return self.attack         
    
    def __str__(self):
        return self.name

    def hurt(self,damage):
        self.health = self.health - damage
        if self.health <= 0:
            print(self.name + ' is dead!')
        else: print(self.name + ' has ' + str(self.health) + ' health left')

    def heal(self,healing):
        self.health = min(self.hitPoints,self.health + healing)
        if self.health == self.hitPoints:
            print(self.name + ' is in full strength!')
        else: print(self.name + ' has ' + str(self.health) + ' health left')
    
    def useAttack(self,attack,targetMonster):
        # attack should use combatPoints somehow, also types
        if attack not in self.attacks:
            print(self.name + ' does not have this attack!')
        else:
            damage = attack.getDamage()
            #print(targetMonster)
            damage = round(damage * self.combatPoints / targetMonster.getCombatPoints())
            print(self.name + ' hits ' + str(targetMonster) + ' for ' + str(damage) + '!')
            targetMonster.hurt(damage)
            



lightning = Attack('LightningBolt', 'electric', 20)    
spray = Attack('WaterSpray','water',10)
betterlightning = Attack('Better LightningBolt', 'electric', 100)  


pika = Monster('Pikachu','electric',100,80,[lightning, betterlightning])
pika.hurt(10)
pika.heal(20)

squirt = Monster('Squirtle','water',200,50,[spray])



pika.useAttack(lightning,squirt)
squirt.useAttack(spray,pika)
pika.useAttack(betterlightning,squirt)


#####

class Node:
    """ Node class: contains unspecified data in stuff and link to next Node
        """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next  = next

    def __str__(self):
        return str(self.stuff)    
 
class Queue:
    """ Queue using linked Nodes
        Supports inserting and deleting nodes
        """
    def __init__(self):
        """ Keep track of both first and last node for fast operations"""
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, stuff):
        # Insert a Node into queue
        node = Node(stuff)
        #print(node)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

   
    def dequeue(self):
        # Returns first node of the queue
        removedNode = self.first.stuff
        #print(removedNode)
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return removedNode

    def isEmpty(self):
        return self.length == 0
    
    def __str__(self):
        s = ''
        item = self.first
        while item is not None:
            s += str(item.stuff) + ' '
            item = item.next
        return s
        
    def __len__(self):
        return self.length


class ListQueue:
    """ Queue using list
        Supports inserting and deleting nodes
        """
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item) #insert item into position of 0 in list self.items
        #print(self.items[0])

    def dequeue(self):
        return self.items.pop() 

Q = Queue()

QL = ListQueue()

import random
A=[random.randint(0,1000) for r in range(10)]




