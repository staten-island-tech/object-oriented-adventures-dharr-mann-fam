from weapon import Weapon

class Character():
    def __init__(self, name: str, health: int, damage: int, classes: str, level: int, exp: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage
        self.classes = classes
        self.level = level
        self.exp = exp


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
                 exp: int):
        super().__init__(name = name, health = health, damage = damage, classes = classes, level = level, exp = exp)



class Enemy(Character):
    def __init__(self, 
                 name: str, health: int, damage: int, classes: str, level: int, exp: int):
        super().__init__(name = name, health = health, damage = damage, classes = classes, level = level, exp = exp)