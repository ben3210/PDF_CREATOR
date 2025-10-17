from abc import ABC, abstractmethod 
#implementing abstraction - the derived classes must have a method to calculate area
#that have details of how area is calculated based on the shape, otherwise Error occurs

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    
class Right_Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) / 2
    
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        return (self.base1 + self.base2) * self.height / 2
    
        
rectangle = Rectangle(5, 2)
print(rectangle.area())

circle = Circle(3)
print(circle.area())

right_triangle = Right_Triangle(6, 4)
print(right_triangle.area())

trapezoid = Trapezoid(11, 7, 6)
print(trapezoid.area())