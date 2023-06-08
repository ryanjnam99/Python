class Ninja:

    def __init__( self , name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.shurikens = 5
    
    def show_stats( self ):
        print(f"\nName: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nShurikens: {self.shurikens}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"\n{self.name} attacked {pirate.name} for {self.strength} damage!\n")
        return self
    
    def shuriken(self, pirate):
        if self.shurikens == 0:
            print("No shurikens left!")
            return self
        else:
            shuriken_damage = self.strength*1.5
            pirate.health -= shuriken_damage
            self.shurikens -= 1
            print(f"\n{self.name} threw a shuriken at {pirate.name} for {int(shuriken_damage)} damage! {self.name} has {self.shurikens} left!\n")
            return self
    
    # def backstab(self, pirate):