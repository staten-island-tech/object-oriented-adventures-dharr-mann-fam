from character import Hero, Enemy, Character, Boss
import json
import os
import random
f = open("data.json", encoding="utf8")
up = json.load(f)
Y = 0
N = 1
os.system("cls")
number_mobs = 1
play = input("Do you want to play again [True/False]")
if play == "True".lower:
    play = True

if play == "False".lower:
    play = False

Goblins = Enemy(name="Goblin", health=25, health_max=25, damage=5, classes="mob", level=1, exp=25, statpoints=0, exp_next=0)
Goblin_Leader = Boss(name="Goblins Leader", health=120, health_max=120, damage=15, classes="boss", level=5, exp=75,statpoints=0, exp_next=0)

    #Tutorial
Tutorial_Dummy = Enemy(name = "Dummy", health = 50, health_max = 50, damage = 5, classes = "Tutorial", level = 1, exp = 100, statpoints = 0, exp_next = 0)

    #Dungeon 2
Wolves = Enemy(name="Wolf", health=50, health_max=65, damage=10, classes="mob", level=5, exp=40, statpoints=0,exp_next=0)
Eilte_Wolf = Boss(name="Elite Wolf", health=250, health_max=250, damage = 40, classes = "boss", level = 10, exp=150, statpoints=0, exp_next=0)

    #Dungeon 3
Placeholder = Enemy(name="PlaceHolder", health = 150, health_max=150, damage=25, classes="mob", level = 10, exp = 100, statpoints=0, exp_next=0)
PlaceholderBoss = Boss(name="PlaceHolder Boss", health=500, health_max=500, damage=60, classes="boss", level = 20, exp = 300, statpoints=0, exp_next=0 )