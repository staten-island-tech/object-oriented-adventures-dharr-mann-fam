from weapon import Weapon

class Character():
    def __init__(self, name: str, health: int, damage: int, classes: str, level: int, exp: int, exp_next: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
        self.classes = classes
        self.level = level
        self.exp = exp
        self.exp_next = exp_next



    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)


class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 damage: int,
                 classes: str,
                 level: int,
                 exp: int,
                 exp_next: int):
        super().__init__(name = name, health = health, damage = damage, classes = classes, level = level, exp = exp, exp_next = exp_next)

    
    def exp_gain(self, exp):
        if Enemy.health == 0:
            Hero.exp == exp + Enemy.exp

    def levelup(self, exp):
        if Hero.exp >= Hero.exp_next:
            Hero.exp - Hero.exp_next
            Hero.level = Hero.level + 1
            Hero.exp_next = Hero.exp_next * 1.5



class Enemy(Character):
    def __init__(self, 
                 name: str, health: int, damage: int, classes: str, level: int, exp: int, exp_next: int):
        super().__init__(name = name, health = health, damage = damage, classes = classes, level = level, exp = exp, exp_next = exp_next)