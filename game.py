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
play = True
alive = 0
##Mobs

#Dungeon 1
Goblins = Enemy(name="Goblin", health=25, health_max=25, damage=5, classes="mob", level=1, exp=50, statpoints=0, exp_next=0)
Goblin_Leader = Boss(name="Goblins Leader", health=120, health_max=120, damage=15, classes="boss", level=5, exp=250,statpoints=0, exp_next=0)

#Tutorial
Tutorial_Dummy = Enemy(name = "Dummy", health = 50, health_max = 50, damage = 5, classes = "Tutorial", level = 1, exp = 100, statpoints = 0, exp_next = 0)

#Dungeon 2
Wolves = Enemy(name="Wolf", health=225, health_max=225, damage=25, classes="mob", level=5, exp=125, statpoints=0,exp_next=0)
Eilte_Wolf = Boss(name="Elite Wolf", health=500, health_max=500, damage = 50, classes = "boss", level = 10, exp=625, statpoints=0, exp_next=0)

#Dungeon 3
Zombie = Enemy(name="Zombie", health = 375, health_max=375, damage=40, classes="mob", level = 15, exp = 500, statpoints=0, exp_next=0)
Giant_Zombie = Boss(name="Giant_Zombie", health=750, health_max=750, damage=75, classes="boss", level = 20, exp = 2500, statpoints=0, exp_next=0)


#Dungeon 4 
Spider = Enemy(name="Spider", health = 500, health_max=500, damage=50, classes="mob", level = 15, exp = 1250, statpoints=0, exp_next=0)
Tarantula = Boss(name="Tarantula", health=1000, health_max=1000, damage= 100, classes="boss", level = 20, exp = 7500, statpoints=0, exp_next=0)

#Dungeon 5
Lizard = Enemy(name="Lizard", health = 750, health_max=750, damage=75, classes="mob", level = 15, exp = 3000, statpoints=0, exp_next=0)
Dragon = Boss(name="Dragon", health=1500, health_max=1500, damage= 150, classes="boss", level = 99, exp = 20000, statpoints=0, exp_next=0)

#Dungeon 6
Professor_Whalen = Enemy(name="Professor Whalen", health=1500, health_max=1500, damage= 100, classes="boss", level = 99, exp = 6969, statpoints=0, exp_next=0)
Mega_Whalen = Boss(name="Mega Whalen", health=99999, health_max=99999, damage= 999, classes="boss", level = 99, exp = 99999, statpoints=0, exp_next=0)

#Impossible
Impossible = Enemy(name="Impossible Whalen Jr", health=5000, health_max=5000, damage= 500, classes="boss", level = 999, exp = 33333, statpoints=0, exp_next=0)
Impossible_boss = Boss(name="Impossible Whalen", health=500000, health_max=500000, damage= 9999, classes="boss", level = 9999, exp = 999999, statpoints=0, exp_next=0)

def battle():
        number_mobs = 10
        for i in range(1,number_mobs):
            Enemy.health = Enemy.health_max
            while Enemy.health > 0:
                os.system("cls")
                hero.attack(Enemy)
                Enemy.attack(hero) 
                print(f"Total number of mobs: {number_mobs}")
                print(f"Health of {Enemy.name} [Level:{Enemy.level}]:{Enemy.health}")   
                print(f"Health of {hero.name} [Level:[{hero.level}]:{hero.health}")
                print("Enter to continue")
                input()
                

                if Enemy.health == 0:
                    hero.gain_experience(Enemy.exp)
                    print(" ")
                    print(f"{hero.name} has gained {Enemy.exp} exp")
                    input()
                    number_mobs = number_mobs - 1

                if hero.health <= 0:
                    hero.die()
                    
        print("You are now moving onto the boss room...")
        print(" ")
        input()
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

    Class_Chooser = input("Enter class [Warrior,Archer,Assassin,Snowman,Noob,???]: ").lower()

    if Class_Chooser == "warrior":
        Class = "Warrior"
        hero = Hero(name = Creation, health = 200, health_max = 200, damage = 15, classes = "Warrior", level = 1, exp = 0, statpoints = 0, exp_next = 100)
        warriorloot =  ["Base Sword", "sword", "Spear", "Sledge Hammer", "claymore", "Javelin", "Rapier", "Saber", "Cutlass", "Scimitar", "Zweihander"]

    if Class_Chooser == "archer":
        Class = "Archer"
        hero = Hero(name = Creation, health = 80, health_max = 80, damage = 45, classes = "Archer", level = 1, exp = 0, statpoints = 0, exp_next = 90)
        archerloot = ["Short Bow", "Bow", "Crossbow", "Celestial Bow", "Tempest Bow", "Phantasm", "Storm bow", "Regular Arrow", "Steel Arrow", "Celestial Arrow", "Flaming Arrow", "Unholy Arrow", "Venom Arrow", "Holy Arrow", "Spectral Arrow", "Uci", "Gock-71", "BK - 48", "BR-16", "N-14", "Sub Submachine sun", "Machine gum", "Regular Bullet", "Nano Bullet", "Bouncy Bullet", "Homing Bullet", "Fast Bullet", "Buck Shot", "Slug Shot", ".50 Cal"]

    if Class_Chooser == "assassin":
        Class = "Assassin"
        hero = Hero(name = Creation, health = 100, health_max = 100, damage = 35, classes = "Assassin", level = 1, exp = 0, statpoints = 0, exp_next = 100)
        assassinloot = ["Dagger", "Shuriken", "Kunai", "Brass Knuckles", "Claws", "Choke", "Dagger but big", "Knife", "Siletto"]

    if Class_Chooser == "snowman":
        Class = "Snowman"
        hero = Hero(name = Creation, health = 150, health_max = 150, damage = 30, classes = "Snowman", level = 1, exp = 0, statpoints = 0, exp_next = 100)
        snowmanloot = ["Snowballs", "Carrot Gun", "Coal Cannon", "Yellow Snow", "Ice Fist", "Brown Snow", "Carrot Sword"]
        
    if Class_Chooser == "noob":
        Class = "Noob"
        hero = Hero(name = Creation, health = 50, health_max = 50, damage = 500, classes = "Noob", level = 1, exp = 0, statpoints = 0, exp_next = 50)
        noobloot = ["Dirt Sword", "Toy Hammer", "Slap", "Baloon Pop", "Scream"]

    if Class_Chooser == "god":
        Class = "God"
        hero = Hero(name = Creation, health = 150, health_max = 150, damage = 35, classes = "God", level = 1, exp = 0, statpoints = 0, exp_next = 10)
        godloot = ["Lightniing Bolt", "Earthquake", "Fireball", "Tsunami", "Enlightenment"]

    



def search():
    Dungeons = ["[1] Goblins",
                "[2] Wolves",
                "[3] Zombies",
                "[4] Arachnids",
                "[5] Lizards",
                "[6] Mega Boss"
    ]
    list(map(print, Dungeons))

if Choice == "1":
    while play == True:
        Search = input("Enter username to start search: ")
        play == False
        for i in up:
            if Search in i["name"]:
                hero = Hero(name = i["name"], health = i["health"], health_max = i["health_max"], damage = i["damage"], classes = i["classes"], level = i["level"], exp = i["exp"], statpoints = i["statpoints"], exp_next = i["exp_next"])
                print (f"Welcome back {hero.name}! ") 
                search()
                """ up.remove(hero.remove(hero.name)) """
                Narration = input("Now pick a dungeon to complete (Type the number corresponding to the Dungeon): ")
                
            
        ##Dungeon 1
        if Narration == "1":
            Enemy = Goblins
            Boss = Goblin_Leader
            number_mobs = 10
            battle()

        ##Dungeon 2
        if Narration == "2":
            Enemy = Wolves
            Boss = Eilte_Wolf
            number_mobs = 10
            battle()

        ##Dungeon 3
        if Narration == "3":
            Enemy = Zombie
            Boss = Giant_Zombie
            number_mobs = 12
            battle()

        ##Dungeon 4
        if Narration == "4":
            Enemy = Spider
            Boss = Tarantula
            number_mobs = 15
            battle()

        ##Dungeon 5
        if Narration == "5":
            Enemy = Lizard
            Boss = Dragon
            number_mobs = 20
            battle()    
        ##Dungeon 6
        if Narration == "6":
            Enemy = Professor_Whalen
            Boss = Mega_Whalen
            number_mobs = 2
            battle()

        ##Dungeon 7
        if Narration == "7":
            Enemy = Impossible
            Boss = Impossible_boss
            number_mobs = 2
            battle()



if Choice == "2":
    for i in  up:
        if Creation in i["name"]:
            print("Username is taken. Please choose another. ")
            quit()
    Tutorial = input("Would you like a tutorial?[Y/Y] (You are forced): ")
    if Tutorial == "Y" or "y":
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
    Search = input("Enter username to start search: ")
    for j in up:
        hero = Hero(name = j["name"], health = j["health"], health_max = j["health_max"], damage = j["damage"], classes = j["classes"], level = j["level"], exp = j["exp"], statpoints = j["statpoints"], exp_next=["exp_next"])
        print(f"[name: {hero.name}, level: {hero.level}, hp: {hero.health_max}, damage: {hero.damage}, class: {hero.classes}, exp: {hero.exp}, statpoints: {hero.statpoints}, Exp Req: {hero.exp_next}]")
        ask = input("What would you like to do?: [1] Edit Statpoints [2] Exit: ")

        if ask == "2":
            exit()
        if ask == "1":
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


if add_data.__dict__ in data:
    add_data.__dict__.update(name = hero.name, health = hero.health, health_max = hero.health_max, damage = hero.damage, classes = hero.classes, level = hero.level, exp = hero.exp, statpoints = hero.statpoints, exp_next = hero.exp_next)
else:
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
