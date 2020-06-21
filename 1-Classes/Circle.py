import math #importing Math 
# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


Circle1 = Circle(5)
print(Circle1.radius) # output : 5
print(Circle1.area()) # output : 78.53981633974483

