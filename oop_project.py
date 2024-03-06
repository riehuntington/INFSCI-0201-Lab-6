class Character:

    def __init__(self, name, health, weapon = ""):
        self.name = name
        self.health = health
        self.weapon = weapon

    def equip(self, weapon):
        self.weapon = weapon

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)

class Hero(Character):
    pass

class Enemy(Character):
    pass

class Weapon:

    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

empty_handed = Weapon(name = "Empty handed", weapon_type = "dummy", damage = 0, value = 0)
healing_staff = Weapon(name = "Healing Staff", weapon_type = "magic", damage = -3, value = 0)

protagonist = Hero(name = "Hero", health = 100)
protagonist.health = 10
protagonist.equip(empty_handed)

ally = Enemy(name = "Friendly Enemy", health = 100, weapon = healing_staff)

# Did not build out actual gameplay as that was not required in the Tasks section