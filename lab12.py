class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Minivan(Car):
   def __init__(self, brand, model, year, hasASD):
       super().__init__(brand, model, year)
       self.hasASD = hasASD

c = Minivan("Honda", "Odyssey", 2018, True)
print(c.brand, c.model, c.year, c.hasASD)

    
