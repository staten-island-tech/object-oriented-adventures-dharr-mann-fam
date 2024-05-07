from weapon import none
import weapon

class Character():
    def __init__(self, name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int):
        self.name = name
        self.health = health
        self.health_max = health_max
        self.damage = damage
        self.classes = classes
        self.level = level
        self.exp = exp
        self.statpoints = statpoints
        self.exp_next = exp_next
  
 


    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.damage} to [{target.name}]")






class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 health_max: int,
                 damage: int,
                 classes: str,
                 level: int,
                 exp: int,
                 statpoints: int,
                 exp_next: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next)


    def gain_experience(self, experience):
        self.exp += experience
        if self.exp >= self.exp_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_next
        self.exp_next = self.exp_next * 1.5
        self.statpoints += 3
        self.health_max = self.health_max * 1.05
        self.damage = self.damage * 1.05
        self.health = self.health_max



class Enemy(Character):
    def __init__(self, 
                 name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next)



class Boss(Character):
    def __init__(self, 
                 name: str, health: int, health_max: int, damage: int, classes: str, level: int, exp: int, statpoints: int, exp_next: int):
        super().__init__(name = name, health = health, health_max = health_max, damage = damage, classes = classes, level = level, exp = exp, statpoints = statpoints, exp_next = exp_next)