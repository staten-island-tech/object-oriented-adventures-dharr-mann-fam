from character import Hero, Enemy
import json
import os
f = open("data.json", encoding="utf8")
up = json.load(f)
Y = 0
N = 1

Creation = input("Enter your Username: ")
Class_Chooser = input("Enter class [Warrior,Archer,Assassin]: ")
Class_Chooser.lower()
if Class_Chooser == "warrior":
    Class = "Warrior"
    hero = Hero(name = Creation, health = 200, health_max=200, damage = 15, classes = "Warrior", level = 1, exp = 0, exp_next = 100)

if Class_Chooser == "archer":
    Class = "Archer"
    hero = Hero(name = Creation, health = 100, health_max=100, damage = 25, classes = "Archer", level = 1, exp = 0, exp_next = 100)

if Class_Chooser == "assassin":
    Class = "Assassin"
    hero = Hero(name = Creation, health = 100, health_max=100, damage = 40, classes = "Assassin", level = 1, exp = 0, exp_next = 100)



Tutorial_Dummy = Enemy(name = "Dummy", health = 50, health_max=50, damage = 5, classes = "Tutorial", level = 1, exp = 100, exp_next = 100)

Tutorial = input("Would you like a tutorial?[Y/N]: ")
Tutorial.lower()
if Tutorial == "y":
        while Tutorial_Dummy.health > 0:
            print(f"Health of {hero.name}:{hero.health_max}")
            print(f"Health of {Tutorial_Dummy.name}: {Tutorial_Dummy.health_max}")

            hero.attack(Tutorial_Dummy)
            Tutorial_Dummy.attack(hero)

            if hero.classes == "Archer":
                hero.attack(Tutorial_Dummy)
                hero.attack(Tutorial_Dummy)
                Tutorial_Dummy.attack(hero)

            print(f"Health of {hero.name}:{hero.health}")
            print(f"Health of {Tutorial_Dummy.name}: {Tutorial_Dummy.health}")

            input()

        if Tutorial_Dummy.health == 0:
            hero.gain_experience(Tutorial_Dummy.exp)
            hero.health = hero.health_max
            print("Congrats yours getting pretty good at this. Time for another challenge")









add_data = Hero(name = hero.name, health = hero.health, health_max = hero.health_max, damage = hero.damage, classes = hero.classes, level = hero.level, exp = hero.exp, exp_next = hero.exp * 1.5 ) 


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

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