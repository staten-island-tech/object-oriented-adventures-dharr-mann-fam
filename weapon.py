class Weapon():
    def __init__(self,
                name: str,
                damage: int,
                rarity: str,
                clas: str): 
        
        self.name = name
        self.damage = damage
        self.rarity = rarity
        self.clas = clas

greatsword = Weapon(name = "Greatsword",
                    damage = 10,
                    rarity = "E",
                    clas = "Warrior")


base_dagger = Weapon(name = "Basic Dagger",
                     damage = 25,
                     rarity = "E",
                     clas = "Assassin")


shortbow = Weapon(name = "Shortbow",
                 damage = 15,
                 rarity = "E",
                 clas = "Assassin")