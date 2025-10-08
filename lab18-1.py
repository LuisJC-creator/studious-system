class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def area(self):
        return self.width * self.height
    
rec1 = Rectangle(3, 4)
rec2 = Rectangle(7, 4)
rec3 = rec1 + rec2
print(rec3.area())
