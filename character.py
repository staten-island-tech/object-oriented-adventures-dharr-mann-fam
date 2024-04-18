from weapon import Weapon
import random

class Character():
    def __init__(self, name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, exp_next: int, crit_chance: int):
        self.name = name
        self.health = health
        self.health_max = health_max
        self.damage = damage
        self.classes = classes
        self.level = level
        self.exp = exp
        self.exp_next = exp_next
        self.crit_chance = crit_chance



    def attack(self, target):
        target.health -= self.damage
        generate = random.randint(1,100)
        if generate <= self.crit_chance:
            target.health -= self.damage * 1.5
            print("Player got a critical hit!")

        target.health = max(target.health, 0)




class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 health_max: int,
                 damage: int,
                 classes: str,
                 level: int,
                 exp: int,
                 exp_next: int,
                 crit_chance: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, exp_next = exp_next, crit_chance = crit_chance)

    def gain_experience(self, experience):
        self.exp += experience
        if self.exp >= self.exp_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_next
        self.exp_next = self.exp_next * 1.5







class Enemy(Character):
    def __init__(self, 
                 name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, exp_next: int, crit_chance: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, exp_next = exp_next, crit_chance = crit_chance)