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
dialouge_greet = ["Hello!", "I have been waiting for you", "The prophecies have fortold of your arrival!", "", "RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "Dang it! Another one, really? Oh well."]
dialouge_fight = ["You truly are a mighty opponent!", "Owww", "This is going to be easy", "", "RARRRRR"]
##Mobs


#Dungeon 1
Goblins = Enemy(name="Goblin", health=25, health_max=25, damage=5, classes="mob", level=1, exp=25, statpoints=0, exp_next=0)
Goblin_Leader = Boss(name="Goblins Leader", health=120, health_max=120, damage=15, classes="boss", level=5, exp=75,statpoints=0, exp_next=0)

#Tutorial
Tutorial_Dummy = Enemy(name = "Dummy", health = 50, health_max = 50, damage = 5, classes = "Tutorial", level = 1, exp = 100, statpoints = 0, exp_next = 0)

#Dungeon 2
Wolves = Enemy(name="Wolf", health=50, health_max=65, damage=10, classes="mob", level=5, exp=40, statpoints=0,exp_next=0)
Eilte_Wolf = Boss(name="Elite Wolf", health=250, health_max=250, damage = 40, classes = "boss", level = 10, exp=150, statpoints=0, exp_next=0)

#Dungeon 3
Zombie = Enemy(name="Zombie", health = 250, health_max=250, damage=45, classes="mob", level = 15, exp = 750, statpoints=0, exp_next=0)
Giant_Zombie = Boss(name="Giant_Zombie", health=500, health_max=500, damage=60, classes="boss", level = 20, exp = 300, statpoints=0, exp_next=0)

#Dungeon 4 
Spider = Enemy(name="Spider", health = 150, health_max=150, damage=25, classes="mob", level = 15, exp = 50, statpoints=0, exp_next=0)
Tarantula = Boss(name="Tarantula", health=750, health_max=750, damage= 75, classes="boss", level = 20, exp = 300, statpoints=0, exp_next=0)

#Dungeon 5
Little_Whalen = Enemy(name="Mini. Whalen", health = 200, health_max=200, damage=50, classes="mob", level = 15, exp = 50, statpoints=0, exp_next=0)
Boss_Whalen = Boss(name="Mr. Whalen", health=1500, health_max=1500, damage= 100, classes="boss", level = 99, exp = 1000, statpoints=0, exp_next=0)



def battle():
    while Enemy.health > 0 and hero.health > 0:
        for i in range(1,number_mobs):
            os.system("cls")
            Enemy.health = Enemy.health_max
            print(f"Total number of mobs: {number_mobs}")
            print(f"Health of {Enemy.name} [Level:{hero.level}]:{Enemy.health_max}")   
            print(f"Health of {hero.name} [Level:[{Enemy.level}]:{hero.health}")
            print("Enter to continue")
            input()

            hero.attack(Enemy)
            Enemy.attack(hero)          

            print(f"Health of {hero.name} [Level:{hero.level}]:{hero.health} ")    
            print(f"Health of {Enemy.name} [Level:{Enemy.level}]:{Enemy.health} ")

            input()
            print("Press Enter to continue battle")
            if Enemy.health == 0:
                hero.gain_experience(Enemy.exp)
                print(" ")
                print(f"{hero.name} has gained {Enemy.exp} exp")

            if hero.health == 0:
                print("You Lost! Restart to pick another dungeon!")
                hero.health = hero.health_max
                play = input("Do you want to play again [True/False]")
                break

    print("You are now moving onto the boss room...")
    print(" ")
    input()

    while Boss.health > 0 and hero.health > 0:
        if Boss.health == Boss.health_max:
            choice_greet = random.randint(1,5)
            if choice_greet == 1:
                print(dialouge_greet[0])
            elif choice_greet == 2:
                print(dialouge_greet[1])
            elif choice_greet == 3:
                print(dialouge_greet[2])
            elif choice_greet == 4:
                print(dialouge_greet[3])
            else:
                print(dialouge_greet[4])
 
        os.system("cls")
        print(f"Health of {hero.name} [Level:{hero.level}]:{hero.health}")    
        print(f"Health of {Boss.name} [Level:{Boss.level}]:{Boss.health}") 
        choice_fight = random.randint(1,10)
        if choice_fight == 1:
            print(dialouge_fight[0])
        elif choice_fight == 2:
            print(dialouge_fight[1])
        elif choice_fight == 3:
            print(dialouge_fight[2])
        elif choice_fight == 4:
            print(dialouge_fight[3])
        elif choice_fight:
            print(dialouge_fight[4])
        else:
            print("")
        print("Enter to continue")   
        input()

        hero.attack(Boss)
        Boss.attack(hero)          

        print(f"Health of {hero.name} [Level:{hero.level}]:{hero.health}")    
        print(f"Health of {Boss.name} [Level:{Boss.level}]:{Boss.health}")

        input()
        print("Press Enter to continue battle")
        if Boss.health == 0:
            hero.gain_experience(Boss.exp)
            print(" ")
            print(f"{hero.name} has gained {Boss.exp} exp")
            hero.health = hero.health_max
            print("You have beaten the dungeon!")

        if hero.health == 0:
            print("You Lost! Restart to pick another dungeon!")
            hero.health = hero.health_max
            break                
                
  






Choice = input("What Would you like to do? [1]Load Existing Character, [2]Create New Character, [3]Inventory: ")
if Choice == "2":
    Creation = input("Enter your Username: ")
    Class_Chooser = input("Enter class [Warrior,Archer,Assassin,Snowman,Noob]: ").lower()

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
        hero = Hero(name = Creation, health = 10, health_max = 10, damage = 5000, classes = "Noob", level = 1, exp = 0, statpoints = 0, exp_next = 50)



def search():
    Dungeons = ["[1] Goblins",
                "[2] Wolves",
                "[3] Zombies",
                "[4] Spiders",
                "[5] FINAL BOSS",
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
            Enemy = Little_Whalen
            Boss = Boss_Whalen
            number_mobs = 20
            battle()

if Choice == "2":
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


if Choice == "3":
    for j in up:
        hero = Hero(name = j["name"], health = j["health"], health_max = j["health_max"], damage = j["damage"], classes = j["classes"], level = j["level"], exp = j["exp"], statpoints = j["statpoints"], exp_next=["exp_next"])
        print(f"[name: {hero.name}, level: {hero.level}, hp: {hero.health_max}, damage: {hero.damage}, class: {hero.classes}, exp: {hero.exp}, statpoints: {hero.statpoints}, Exp Req: {hero.exp_next}]")
        exit()



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


