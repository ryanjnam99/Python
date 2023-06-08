class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.sound = sound
    def sleep(self):
        self.energy += 25
        print(f"{self.name} energy is at {self.energy}")
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} energy is at {self.energy} and health is at {self.health}")
        return self
    def play(self):
        self.health += 5
        print(f"{self.name} is at a health of {self.health}")
        return self
    def noise(self):
        print(f"{self.name} starts to {self.sound}")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_foods, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_foods = pet_foods
        self.pet = pet
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} takes the {self.pet.name} out for a walk.")
        return self
    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} feeds the {self.pet.name} {self.treats}.")
        return self
    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} bathes the {self.pet.name}.")
        return self




toto = Pet("Toto", "afghan hound", "sit", "bark")
ryan = Ninja("Ryan", "Nam", "biscuits", "nibbles", toto)
print(ryan.last_name)
ryan.walk().feed().walk()
print(toto.name)