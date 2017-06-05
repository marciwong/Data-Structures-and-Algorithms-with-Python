# -*- coding: utf-8 -*-
"""

DSAP Workshop 3

"""

##########################################

#####
# Monsters and attacks

class Monster():
    def __init__(self,name,monsterType,combatPoints,hitPoints):
        self.name = name
        self.monsterType = monsterType # type
        self.combatPoints = combatPoints
        self.health = hitPoints # current health
        
    def getMonsterType(self):
        return self.monsterType

    def getCombatPoints(self):
        return self.combatPoints
    
    def getHealth(self):
        return self.health
    
    def gethitPoints(self):
        return self.hitPoints        
         
    def __str__(self):
        return self.name

    def hurt(self,damage):
        self.health = self.health - damage
        if self.health <= 0:
            print(self.name + ' is dead!')
        else: print(self.name + ' has ' + str(self.health) + ' health left')

# Add the functions heal and useAttack as described in the instructions

    def heal(self,healing):
      self.health = self.health + healing
      if self.health >= max(self.health):
        print(self.name + 'has full health!')
      else:
        print(self.name + 'has', str(self.health) + 'health now!')

    def useAttack(self,name,attack,targetMonster):
      if attack not in self.attacks:
        print(self.name + ' does not have this attack!')
      else: 
        print(self.name + 'used' + self.attackType)
      
   
       
       
pika = Monster('Pikachu','electric',100,80)
  
print(pika.getMonsterType())
           
pika.hurt(10)
pika.heal(20) 


class Attack():
    def __init__(self,name,attackType,damage):
       self.name = name
       self.attackType = attackType
       self.damage = damage
       name = str
       attackType = str
       damage = int
    def getAttackType(self):
        return self.attackType
    def getDamage(self):
        return self.damage
    def __str__(self):
        return self.name
    
def useAttack(self,attack,otherMonster):
        otherMonster.health = otherMonster.health - self.Adamage
        print (self.name + 'used' + self.attackName + 'on' + otherMonster )
        pika.useAttack(lightning,squirt)
        squirt.useAttack(spray,pika)



lightning = Attack('LightningBolt', 'electric', 20)    
spray = Attack('WaterSpray','water',10)

squirt = Monster('Squirtle','water',200,50,[spray])
pika = Monster('Pikachu','electric',100,80,[lightning])
pika.useAttack(lightning,squirt)
squirt.useAttack(spray,pika)


squirt = Monster('Squirtle','water',200,50,[spray])
pika = Monster('Pikachu','electric',100,80,[lightning])
#########
# Queues

class ListQueue:
    """ Queue using list
        Supports inserting and deleting nodes
        """
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item): # Other way around: append and remove first?
        self.items.insert(0,item)
        #print(self.items[0])

    def dequeue(self):
        return self.items.pop() 


lq = ListQueue()
lq.enqueue(23)
x=lq.dequeue()


#####

class Node:
    """ 
    Node class: contains unspecified data in stuff and link to next Node
    """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next  = next

    def __str__(self):
        return str(self.stuff) 

#####


class Queue:
    """ 
    Queue using linked Nodes
    Supports inserting and deleting nodes
    """
    
    def __init__(self):
        """ Keep track of both first and last node for fast operations"""
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, stuff):
        # Insert a Node into queue
        n=1
        node = Node(stuff)
        if self.length == 0: # empty queue: add first node
            self.first = node
            self.last = node
        else: # add node to be the last item in queue
            last = self.last
            last.next = node
            self.last = node
        self.length = n+1 # increase queue length
  
    def dequeue(self):
        # Returns first node of the queue
        removedNode = self.first.stuff
        self.first = n # update the first node
        self.length = n-1 # decrease queue length
        if self.length == 0:
            self.last = None
        return removedNode

    def isEmpty(self):
        return self.length == 0
    
    def __str__(self):
        # return the queue elements as a string
        
    
      def __len__(self):
        return self.length

# Run the queue:

import random
Q = Queue()

QL = ListQueue()

A=[random.randint(0,1000) for r in range(1000)]

%timeit for i in A: Q.enqueue(i)

%timeit for i in A: QL.enqueue(i)




