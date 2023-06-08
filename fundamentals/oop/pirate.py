class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.bullets = 3
        self.bottles = 4

    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nBullets: {self.bullets}\nBottles of Rum: {self.bottles}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"\n{self.name} attacked {ninja.name} for {self.strength} damage!\n")
        return self

    def pistol (self, ninja):
        if self.bullets == 0:
            print("Out of ammo!")
            return self
        else:
            pistol_damage = self.strength*2
            ninja.health -= pistol_damage
            self.bullets -= 1
            print(f"\n{self.name} shot {ninja.name} for {int(pistol_damage)} damage! {self.name} has {self.bullets} bullets left!\n")
            return self

    def rum (self):
        if self.bottles == 0:
            print("Out of booze!")
            return self
        else:
            heal_amount = 15
            self.health += heal_amount
            self.bottles -= 1
            print(f'\n{self.name} healed for {heal_amount}!')
            return self