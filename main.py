from character import Hero, Enemy
Y = 0
N = 1

Creation = input("Enter your Username: ")
Class_Chooser = input("Enter class [Warrior,Archer,Assassin]: ")
if Class_Chooser == "Warrior":
    Class = "Warrior"
    hero = Hero(name = Creation, health = 200, damage = 15, classes = "Warrior", level = 1, exp = 0 )

if Class_Chooser == "Archer":
    Class = "Archer"
    hero = Hero(name = Creation, health = 100, damage = 25, classes = "Archer", level = 1, exp = 0 )

if Class_Chooser == "Assassin":
    Class = "Assassin"
    hero = Hero(name = Creation, health = 100, damage = 40, classes = "Assassin", level = 1, exp = 0 )



Tutorial_Dummy = Enemy(name = "Dummy", health = 50, damage = 5, classes = "Tutorial", level = 1, exp = 100)

Tutorial = input("Would you like a tutorial?[Y/N]: ")
if Tutorial == "Y":
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
            hero.exp = hero.exp + Tutorial_Dummy.exp
            print("Congrats yours getting pretty good at this. Time for another challenge")
            print(__name__)