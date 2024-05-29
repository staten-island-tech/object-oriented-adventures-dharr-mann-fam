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
alive = 0
##Mobs

#Dungeon 1
Goblins = Enemy(name="Goblin", health=25, health_max=25, damage=5, classes="mob", level=1, exp=50, statpoints=0, exp_next=0)
Goblin_Leader = Boss(name="Goblins Leader", health=120, health_max=120, damage=15, classes="boss", level=5, exp=250,statpoints=0, exp_next=0)

#Tutorial
Tutorial_Dummy = Enemy(name = "Dummy", health = 50, health_max = 50, damage = 5, classes = "Tutorial", level = 1, exp = 100, statpoints = 0, exp_next = 0)

#Dungeon 2
Wolves = Enemy(name="Wolf", health=75, health_max=75, damage=15, classes="mob", level=5, exp=125, statpoints=0,exp_next=0)
Eilte_Wolf = Boss(name="Elite Wolf", health=300, health_max=300, damage = 50, classes = "boss", level = 10, exp=625, statpoints=0, exp_next=0)

#Dungeon 3
Zombie = Enemy(name="Zombie", health = 225, health_max=225, damage=20, classes="mob", level = 25, exp = 500, statpoints=0, exp_next=0)
Giant_Zombie = Boss(name="Giant_Zombie", health=550, health_max=550, damage=125, classes="boss", level = 30, exp = 2500, statpoints=0, exp_next=0)

#Dungeon 4 
Spider = Enemy(name="Spider", health = 550, health_max=550, damage=50, classes="mob", level = 35, exp = 1250, statpoints=0, exp_next=0)
Tarantula = Boss(name="Tarantula", health=1350, health_max=1350, damage= 300, classes="boss", level = 60, exp = 7500, statpoints=0, exp_next=0)

#Dungeon 5
Lizard = Enemy(name="Lizard", health = 750, health_max=750, damage=60, classes="mob", level = 55, exp = 3000, statpoints=0, exp_next=0)
Dragon = Boss(name="Dragon", health=2100, health_max=2100, damage= 500, classes="boss", level = 99, exp = 20000, statpoints=0, exp_next=0)

#Dungeon 6
Professor_Whalen = Enemy(name="Professor Whalen", health=1500, health_max=1500, damage= 100, classes="boss", level = 99, exp = 6969, statpoints=0, exp_next=0)
Mega_Whalen = Boss(name="Mega Whalen", health=99999, health_max=99999, damage= 999, classes="boss", level = 999, exp = 99999, statpoints=0, exp_next=0)

#Impossible
Impossible = Enemy(name="Impossible Whalen Jr", health=5000, health_max=5000, damage= 500, classes="boss", level = 999, exp = 33333, statpoints=0, exp_next=0)
Impossible_boss = Boss(name="Impossible Whalen", health=500000, health_max=500000, damage= 9999, classes="boss", level = 9999, exp = 999999, statpoints=0, exp_next=0)

def battle():
        number_mobs = 21
        counter = 20
        for i in range(1,number_mobs):
            Enemy.health = Enemy.health_max
            while Enemy.health > 0:
                os.system("cls")
                hero.attack(Enemy)
                Enemy.attack(hero) 
                print(f"Total number of mobs: {counter}")
                print(f"Health of {Enemy.name} [Level:{Enemy.level}]:{Enemy.health}")   
                print(f"Health of {hero.name} [Level:[{hero.level}]:{hero.health}")
                print("Enter to continue")
                input()
                

                if Enemy.health == 0:
                    hero.gain_experience(Enemy.exp)
                    print(" ")
                    print(f"{hero.name} has gained {Enemy.exp} exp")
                    input()
                    counter = counter - 1
                
                elif hero.health <= 0:
                    hero.die()

                if counter == 0:     
                    print("You are now moving onto the boss room...")
                    print(" ")
                    input()
                    boss()

def boss():    
        while Boss.health > 0:
            os.system("cls")
            hero.attack(Boss)
            Boss.attack(hero)          
            print(f"Health of {hero.name} [Level:{hero.level}]:{hero.health}")    
            print(f"Health of {Boss.name} [Level:{Boss.level}]:{Boss.health}") 
            print("Press Enter to continue battle")  
            input()


            if Boss.health == 0:
                hero.gain_experience(Boss.exp)
                print(" ")
                print(f"{hero.name} has gained {Boss.exp} exp")
                hero.health = hero.health_max
                print("You have beaten the dungeon! Run the code again and choose another dungeon. ")

            if hero.health <= 0:
                hero.die()




Choice = input("What Would you like to do? [1]Load Existing Character, [2]Create New Character, [3]Inventory: ")
if Choice == "2":
    Creation = input("Enter your Username: ")
    for i in  up:
        if Creation in i["name"]:
            print("Username is taken. Please choose another. ")
            quit()

    Class_Chooser = input("Enter class [Warrior,Archer,Assassin,Snowman,Noob,???]: ").lower()

    if Class_Chooser == "warrior":
        Class = "Warrior"
        hero = Hero(name = Creation, health = 200, health_max = 200, damage = 15, classes = "Warrior", level = 1, exp = 0, statpoints = 0, exp_next = 100)

    if Class_Chooser == "archer":
        Class = "Archer"
        hero = Hero(name = Creation, health = 80, health_max = 80, damage = 20, classes = "Archer", level = 1, exp = 0, statpoints = 0, exp_next = 90)

    if Class_Chooser == "assassin":
        Class = "Assassin"
        hero = Hero(name = Creation, health = 100, health_max = 100, damage = 40, classes = "Assassin", level = 1, exp = 0, statpoints = 0, exp_next = 100)

    if Class_Chooser == "snowman":
        Class = "Snowman"
        hero = Hero(name = Creation, health = 150, health_max = 150, damage = 30, classes = "Snowman", level = 1, exp = 0, statpoints = 0, exp_next = 100)
        
    if Class_Chooser == "noob":
        Class = "Noob"
        hero = Hero(name = Creation, health = 50, health_max = 50, damage = 50, classes = "Noob", level = 1, exp = 0, statpoints = 0, exp_next = 50)

    if Class_Chooser == "god":
        Class = "God"
        hero = Hero(name = Creation, health = 125, health_max = 125, damage = 25, classes = "God", level = 1, exp = 0, statpoints = 0, exp_next = 1)



def search():
    Dungeons = ["[1] Goblins",
                "[2] Wolves",
                "[3] Zombies",
                "[4] Arachnids",
                "[5] Lizards",
                "[6] Mega Boss",
                "[7] Impossible"
    ]
    list(map(print, Dungeons))

if Choice == "1":
        Search = input("Enter username to start search: ")
        for i in up:
            if Search in i["name"]:
                hero = Hero(name = i["name"], health = i["health"], health_max = i["health_max"], damage = i["damage"], classes = i["classes"], level = i["level"], exp = i["exp"], statpoints = i["statpoints"], exp_next = i["exp_next"])
                print (f"Welcome back {hero.name}! ") 
                search()
                Narration = input("Now pick a dungeon to complete (Type the number corresponding to the Dungeon): ")
                
            
        ##Dungeon 1
        if Narration == "1":
            Enemy = Goblins
            Boss = Goblin_Leader
            battle()

        ##Dungeon 2
        elif Narration == "2":
            Enemy = Wolves
            Boss = Eilte_Wolf
            battle()

        ##Dungeon 3
        elif Narration == "3":
            Enemy = Zombie
            Boss = Giant_Zombie
            battle()

        ##Dungeon 4
        elif Narration == "4":
            Enemy = Spider
            Boss = Tarantula
            battle()

        ##Dungeon 5
        elif Narration == "5":
            Enemy = Lizard
            Boss = Dragon
            battle()   

        ##Dungeon 6
        elif Narration == "6":
            Enemy = Professor_Whalen
            Boss = Mega_Whalen
            battle()
            
        ##Dungeon 7
        elif Narration == "7":
            Enemy = Impossible
            Boss = Impossible_boss
            battle()



if Choice == "2":
    Tutorial = input("Tutorial is starting... ")

    while Tutorial_Dummy.health > 0:
        os.system("cls")
        print(f"Health of {hero.name}:{hero.health_max}")
        print(f"Health of {Tutorial_Dummy.name}: {Tutorial_Dummy.health_max}")

        hero.attack(Tutorial_Dummy)
        Tutorial_Dummy.attack(hero)

        print(f"Health of {hero.name}:{hero.health}")
        print(f"Health of {Tutorial_Dummy.name}: {Tutorial_Dummy.health}")

        input()
        print("Press Enter to continue battle")
    if Tutorial_Dummy.health == 0:
        hero.gain_experience(Tutorial_Dummy.exp)
        hero.health = hero.health_max

        print("Congrats on your first win! Kill Terminal and go to inventory to see drops/use stat points.")

    if hero.health <= 0:
        hero.die()
        print("How you die to Tutorial")


if Choice == "3":
    os.system("cls")
    for j in up:
        hero = Hero(name = j["name"], health = j["health"], health_max = j["health_max"], damage = j["damage"], classes = j["classes"], level = j["level"], exp = j["exp"], statpoints = j["statpoints"], exp_next=j["exp_next"])
        print(f"Stats: [name: {hero.name}, level: {hero.level}, hp: {hero.health_max}, damage: {hero.damage}, class: {hero.classes}, exp: {hero.exp}, statpoints: {hero.statpoints}, Exp Req: {hero.exp_next}]")
        ask = input("What would you like to do?: [1] Edit Statpoints [2] Exit: ")

        if ask == "2":
            exit()
        if ask == "1":
            print(f"Available Points: {hero.statpoints}")
            edit = input("Which Statpoint woud you like to change? [1] Damage, [2] Max Health:")
            if edit == "1":
                hero.statpoint_atk(hero.statpoints)

            if edit == "2":
                hero.statpoint_HP(hero.statpoints)
            
            


add_data = Hero(name = hero.name, health = hero.health, health_max = hero.health_max, damage = hero.damage, classes = hero.classes, level = hero.level, exp = hero.exp, statpoints = hero.statpoints, exp_next = hero.exp_next) 




with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    
    ##Call classes in here
data  = [obj for obj in data if obj['name'] != hero.name]
json.dumps(data, indent = 4)

data.append(add_data.__dict__)


#No code needed below this line


# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")


#5,8,10,12,15,18
#5,10,15,18,20,23
