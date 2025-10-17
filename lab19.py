class Vehicle():
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def start_engine(self):
        print("Car engine started.")
        return
    
class Motorcycle(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def start_engine(self):
        print("Motorcycle engine started.")
        return
    
c1 = Car("Toyota")
c1.start_engine()

m1 = Motorcycle("Harley-Davidson")
m1.start_engine()
