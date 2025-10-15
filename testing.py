class Animal:
    def __init__(self, height, weight, color, species, predator):
        self.height = height
        self.weight = weight
        self.color = color
        self.species = species
        self.predator = predator
    
    def calBMI(self):
        return self.weight / self.height
    
    def printInfo(self):
        print(f"{self.height} {self.weight} {self.color} {self.species} {self.predator}")

class Cat(Animal):
    def __init__(self, height, weight, color, species, predator, furLength):
        super().__init__(self, height, weight, color, species, predator)
        self.furLength = furLength

class Tabby(Cat):
    def __init__(self, height, weight, color, species, predator, furLength, stray):
        super().__init_subclass__


jaguar = Animal(2, 6, "Orange", "Jaguar", True)
cat = Animal(3, 9, "Black", "Cat", True, 15.0)
jaguar.printInfo()
print(f"{jaguar.species} bmi is: {jaguar.calBMI()}")
cat.printInfo()
print(f"{cat.species} bmi is: {jaguar.calBMI()}")


        
