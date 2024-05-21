class Weapon():
    def __init__(self,
                name: str,
                damage: int,
                clas: str): 
        
        self.name = name
        self.damage = damage
        self.clas = clas

basesword = Weapon(name = "Greatsword",
                    damage = 10,
                    clas = "Warrior")
sword = Weapon(name = "Sword",
                    damage = 12,
                    clas = "Warrior")
spear = Weapon(name = "Spear",
                    damage = 15,
                    clas = "Warrior")
claymore = Weapon(name = "Claymore",
                    damage = 20,
                    clas = "Warrior")
sledge_hammer = Weapon(name = "Sledge Hammer",
                    damage = 30,
                    clas = "Warrior")
javelin = Weapon(name = "Javelin",
                    damage = 35,
                    clas = "Warrior")
rapier = Weapon(name = "Rapier",
                    damage = 40,
                    clas = "Warrior")
saber = Weapon(name = "Saber",
                    damage = 45,
                    clas = "Warrior")
cutlass = Weapon(name = "Cutlass",
                    damage = 50,
                    clas = "Warrior")
Scimitar = Weapon(name = "Scimitar",
                    damage = 75,
                    clas = "Warrior")



shortbow = Weapon(name = "Shortbow",
                 damage = 15,
                 clas = "Archer")
Bow = Weapon(name = "Bow",
                 damage = 17.5,
                 clas = "Archer")
crossbow = Weapon(name = "Crossbow",
                 damage = 20,
                 clas = "Archer")
celestial_bow = Weapon(name = "Celestial Bow",
                 damage = 22.5,
                 clas = "Archer")
tempest_bow = Weapon(name = "Tempest Bow",
                 damage = 25,
                 clas = "Archer")
uzi = Weapon(name = "Uci",
                 damage = 30,
                 clas = "Archer")
glock = Weapon(name = "Gock-17",
                 damage = 35,
                 clas = "Archer")
m14 = Weapon(name = "N-14",
                 damage = 40,
                 clas = "Archer")
smg = Weapon(name = "Sub submachine sun",
                 damage = 45,
                 clas = "Archer")
mg = Weapon(name = "Machine gum",
                 damage = 50,
                 clas = "Archer")
ar = Weapon(name = "AR-16",
                 damage = 75,
                 clas = "Archer")
ak = Weapon(name = "BK-47",
                 damage = 90,
                 clas = "Archer")


base_dagger = Weapon(name = "Basic Dagger",
                     damage = 12.5,
                     clas = "Assassin")
dagger = Weapon(name = "Basic Dagger",
                     damage = 15,
                     clas = "Assassin")
shuriken = Weapon(name = "Shuriken",
                     damage = 20,
                     clas = "Assassin")
kunai = Weapon(name = "Kunai",
                     damage = 22.5,
                     clas = "Assassin")
brass = Weapon(name = "Brass Knuckles",
                     damage = 27.5,
                     clas = "Assassin")
claws = Weapon(name = "Claws",
                     damage = 30,
                     clas = "Assassin")
bigdagger = Weapon(name = "Dagger but Big",
                     damage = 32.5,
                     clas = "Assassin")
knife = Weapon(name = "Knife",
                     damage = 40,
                     clas = "Assassin")
siletto = Weapon(name = "Siletto",
                     damage = 80,
                     clas = "Assassin")

none = Weapon(name = "Unequiped",
              damage = 0,
              clas = "Every")


warriorloot =  ["Base Sword", "sword", "Spear", "Sledge Hammer", "claymore", "Javelin", "Rapier", "Saber", "Cutlass", "Scimitar"]

archerloot = ["Short Bow", "Bow", "Crossbow", "Celestial Bow", "Tempest Bow", "Uci", "Gock-17", "N-14", "Sub Submachine sun", "Machine gum", "AR-16", "BK-47"]

assassinloot = ["Basic Dagger", "Dagger", "Shuriken", "Kunai", "Brass Knuckles", "Claws", "Choke", "Dagger but big", "Knife", "Siletto"]

snowmanloot = ["Snowballs", "Carrot Gun", "Coal Cannon", "Yellow Snow", "Ice Fist", "Brown Snow", "Carrot Sword"]

noobloot = ["Dirt Sword", "Toy Hammer", "Slap", "Baloon Pop", "Scream"]

godloot = ["Lightniing Bolt", "Earthquake", "Fireball", "Tsunami", "Enlightenment"]
