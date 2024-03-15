# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:23:43 2024

@author: axeve
Alexis Evans
CS 120
Prof Harris
Mar. 15, 2024
"""

import tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    
    monster = tbc.Character("Monster", 20, 30, 5, 0)
    
    hero.printStats()
    monster.printStats()
    
    tbc.basicFight(hero, monster)
    
if __name__ == "__main__":
    main()
