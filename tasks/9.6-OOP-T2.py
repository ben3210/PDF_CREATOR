from abc import ABC, abstractmethod 
#implementing abstraction - the derived classes must have a method to calculate area
#that overrides the initial area method in the parent class(Shape), otherwise Error occurs

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __int__(self):
        return int(self.area())
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def __str__(self):
        return f"Rectangle: lenght {self.length}, width {self.width}"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def __str__(self):
        return f"Circle: raduis {self.radius}"
    
class Right_Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) / 2
    def __str__(self):
        return f"Right Triangle: base {self.base}, height: {self.height}"
    
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
    def area(self):
        return (self.base1 + self.base2) * self.height / 2
    def __str__(self):
        return f"Trapezoid: base1 {self.base1}, base2: {self.base2}, height: {self.height}"
    
        
rectangle = Rectangle(5, 2)
print(int(rectangle))

circle = Circle(3)
print(int(circle))

right_triangle = Right_Triangle(6, 4)
print(int(right_triangle))

trapezoid = Trapezoid(11, 7, 6)
print(int(trapezoid))

print(str(rectangle))
print(str(circle))
print(str(right_triangle))
print(str(trapezoid))