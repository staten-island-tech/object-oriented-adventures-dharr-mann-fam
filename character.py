from weapon import none
import math
import weapon
import os
import random

class Character():
    def __init__(self, name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int, extra_damage: int):
        self.name = name
        self.health = health
        self.health_max = health_max
        self.damage = damage
        self.classes = classes
        self.level = level
        self.exp = exp
        self.statpoints = statpoints
        self.exp_next = exp_next
        self.extra_damage = extra_damage
  
 


    def attack(self, target):
        target.health -= self.damage
        math.ceil(self.health)
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {round(self.damage)} and {self.extra_damage} to [{target.name}]")





class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 health_max: int,
                 damage: int,
                 extra_damage: int,
                 classes: str,
                 level: int,
                 exp: int,
                 statpoints: int,
                 exp_next: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next, extra_damage=extra_damage)


    def gain_experience(self, experience):
        self.exp += experience
        while self.exp >= self.exp_next:
            self.level_up()
            
    def roll_weapon(self, cls):
        rng = random.randint(1,2)
        rng2 = random.randint(1,len(weapon.what_class[cls.lower()])-1)
        if rng == 1:
            self.extra_damage = weapon.what_class[cls.lower()][rng2].damage
            print(f"You have dropped {weapon.what_class[cls.lower()][rng2].name} damage")
            print(f"You have gained {self.extra_damage} damage")
            item = weapon.what_class[cls.lower()][rng2].name
            return item
            """ self.store(weapon.what_class[cls.lower()][rng2].name) """


    def level_up(self):
        self.level += 1
        self.exp -= self.exp_next
        self.exp_next = self.exp_next * 1.15
        self.exp_next = math.ceil(self.exp_next)
        self.statpoints += 5
        self.health_max = self.health_max * 1.05
        self.health_max = math.ceil(self.health_max)
        self.damage = self.damage * 1.05
        self.damage = math.ceil(self.damage)
        self.health = self.health_max


    def die(self):
        if self.health <= 0:
            self.health = self.health_max    
            print("You died! No exp for you")
            quit()

    def statpoint_atk(self, amount):
        print(f"Available Points: {self.statpoints}")
        amount = int(input("enter amount: "))
        if amount > self.statpoints:
            print("Error! Amount is too high, exit and retry")
        else:
            for i in range(amount):
                self.statpoints -= 1
                self.damage = (self.damage * 1.01)

            print(f"You have put {amount} points into Damage!")


    def statpoint_HP(self, amount):
        print(f"Available Points: {self.statpoints}")
        amount = int(input("enter amount: "))
        if amount > self.statpoints:
            print("Error! Amount is too high, exit and retry")
        else:
            for i in range(amount):
                self.statpoints -= 1
                self.health = (self.health * 1.01)
                self.health_max = (self.health_max * 1.01)
            print(f"You have put {amount} points into Health!")


    def store(self, inventory):
        inventory = []
        item = self.roll_weapon()
        inventory.append(item)
        print(inventory)









class Enemy(Character):
    def __init__(self, 
                 name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int, extra_damage: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next, extra_damage=extra_damage)



class Boss(Character):
    def __init__(self, 
                 name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int, extra_damage: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next, extra_damage=extra_damage)


