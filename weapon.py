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
                 damage = 20,
                 clas = "Archer")
Bow = Weapon(name = "Bow",
                 damage = 35,
                 clas = "Archer")
crossbow = Weapon(name = "Crossbow",
                 damage = 50,
                 clas = "Archer")
celestial_bow = Weapon(name = "Celestial Bow",
                 damage = 65,
                 clas = "Archer")
tempest_bow = Weapon(name = "Tempest Bow",
                 damage = 75,
                 clas = "Archer")
uzi = Weapon(name = "Uci",
                 damage = 90,
                 clas = "Archer")
glock = Weapon(name = "Gock-17",
                 damage = 105,
                 clas = "Archer")
m14 = Weapon(name = "N-14",
                 damage = 115,
                 clas = "Archer")
smg = Weapon(name = "Sub submachine sun",
                 damage = 135,
                 clas = "Archer")
mg = Weapon(name = "Machine gum",
                 damage = 150,
                 clas = "Archer")
ar = Weapon(name = "AR-16",
                 damage = 175,
                 clas = "Archer")
ak = Weapon(name = "BK-47",
                 damage = 225,
                 clas = "Archer")


base_dagger = Weapon(name = "Basic Dagger",
                     damage = 15.5,
                     clas = "Assassin")
dagger = Weapon(name = "Basic Dagger",
                     damage = 27,
                     clas = "Assassin")
shuriken = Weapon(name = "Shuriken",
                     damage = 39,
                     clas = "Assassin")
kunai = Weapon(name = "Kunai",
                     damage = 51,
                     clas = "Assassin")
brass = Weapon(name = "Brass Knuckles",
                     damage = 58,
                     clas = "Assassin")
claws = Weapon(name = "Claws",
                     damage = 70,
                     clas = "Assassin")
bigdagger = Weapon(name = "Dagger but Big",
                     damage = 82,
                     clas = "Assassin")
knife = Weapon(name = "Knife",
                     damage = 90,
                     clas = "Assassin")
siletto = Weapon(name = "Siletto",
                     damage = 105,
                     clas = "Assassin")
katana = Weapon(name = "Katana",
                     damage = 117,
                     clas = "Assassin")
karambit = Weapon(name = "Karambit",
                     damage = 136,
                     clas = "Assassin")
butterfly = Weapon(name = "Butterfly Knife",
                     damage = 175,
                     clas = "Assassin")

snowball = Weapon(name = "Snowball",
                     damage = 12.5,
                     clas = "snowman")
carrotgun = Weapon(name = "Carrot Gun",
                     damage = 25,
                     clas = "snowman")
coalcannon = Weapon(name = "Coal Cannon",
                     damage = 50,
                     clas = "snowman")
yellowsnow = Weapon(name = "Yellow Snow",
                     damage = 75,
                     clas = "snowman")
icefist = Weapon(name = "Ice Fist",
                     damage = 100,
                     clas = "snowman")
brownsnow = Weapon(name = "Brown Snow",
                     damage = 125,
                     clas = "snowman")
carrotsword = Weapon(name = "Carrot Sword",
                     damage = 150,
                     clas = "snowman")

dirtsword = Weapon(name = "Dirt Sword",
                     damage = 500,
                     clas = "noob")
toyhammer = Weapon(name = "Toy Hammer",
                     damage = 750,
                     clas = "noob")
slap = Weapon(name = "Slap",
                     damage = 1000,
                     clas = "noob")
balloonpop = Weapon(name = "Balloon Pop",
                     damage = 1500,
                     clas = "noob")
scream = Weapon(name = "Scream",
                     damage = 2500,
                     clas = "noob")


none = Weapon(name = "Unequiped",
              damage = 0,
              clas = "Every")


warriorloot =  ["Base Sword", "sword", "Spear", "Sledge Hammer", "claymore", "Javelin", "Rapier", "Saber", "Cutlass", "Scimitar"]

archerloot = ["Short Bow", "Bow", "Crossbow", "Celestial Bow", "Tempest Bow", "Uci", "Gock-17", "N-14", "Sub Submachine sun", "Machine gum", "AR-16", "BK-47"]

assassinloot = ["Basic Dagger", "Dagger", "Shuriken", "Kunai", "Brass Knuckles", "Claws", "Dagger but big", "Knife", "Siletto"]

snowmanloot = ["Snowballs", "Carrot Gun", "Coal Cannon", "Yellow Snow", "Ice Fist", "Brown Snow", "Carrot Sword"]

noobloot = ["Dirt Sword", "Toy Hammer", "Slap", "Balloon Pop", "Scream"]

godloot = ["Lightniing Bolt", "Earthquake", "Fireball", "Tsunami", "Enlightenment"]
