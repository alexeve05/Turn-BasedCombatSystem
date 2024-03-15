# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:30:15 2024

@author: axeve
"""

import random

class Character(object):
    def __init__(self, name = "", hitPoints = 20, hitChance = 50, maxDamage = 5, armor = 1):
        super().__init__()
        
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__hitPoints = value
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__hitChance = value
        
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__maxDamage = value
        
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        value = self.testInt(value, 0, 1000, 0)
        self.__armor = value
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value
            checks to see if it is an int between
            min and max. If it is not a legal value 
            set it to default """
            
        out = default
        
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
            
        return out
    
    def printStats(self):
        print(f"""
{self.name}
    Hit Points: {self.hitPoints}
    Hit Chance: {self.hitChance}
    Max Damage: {self.maxDamage}
    Armor: {self.armor}
    
    """)
    
    def hit(self, enemy):
        if random.randint(1,100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}")
            damage = random.randint(1, self.maxDamage)
            print(f" for {damage} points of damage")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print("The Enemy takes no damage.")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses {enemy.name}")
            
def basicFight(character1, character2):
    keepGoing = True
    while keepGoing:
        character1.hit(character2)
        character2.hit(character1)
        
        print(f"{character1.name} HP: {character1.hitPoints}")
        print(f"{character2.name} HP: {character2.hitPoints}")
        print()
        
        if character1.hitPoints <= 0:
            print(f"{character1.name} loses")
            keepGoing = False
        elif character2.hitPoints <= 0:
            print(f"{character2.name} loses")
            keepGoing = False
        start = input("Press enter if you want to do another round of combat.")
        
def main():
    c = Character()
    c.printStats()
    basicFight(c, c)
    
if __name__ == "__main__":
    main()
    