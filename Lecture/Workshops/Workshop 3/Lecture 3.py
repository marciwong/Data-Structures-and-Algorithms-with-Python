# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:09:29 2016

@author: marcowong
"""

class Monster():
    def __init__(self,name, hitPoints, health, combatPoints):
        self.name = name
        self.combatPoints = combatPoints
        self.hitPoints = hitPoints
        self.health = hitPoints


    def hurt (self,damage):
        self.health = self.health - damage
        if self.health <=0:
            print(self.name + 'is dead!')

