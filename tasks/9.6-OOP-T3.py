class Shape:
    def show(self):
        pass
    def save(self):
        with open("shape.txt", "w") as file:
            file.write(self.show())

    def load(self):
        with open("shape.txt", "r") as file:
            print(file.read())

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        return f"Square: coordinates of upper left corner ({self.x},{self.y}), side length {self.side}"

class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def show(self):
        return f"Rectangle: coordinates of upper left corner ({self.x},{self.y}), length {self.length}, width {self.width}"
    
class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        return f"Circle: coordinates of centre ({self.x},{self.y}), radius {self.radius}"
    
class Ellipse(Shape):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    
    def show(self):
        return f"Ellipse: coordinates of top corner of a circumscribed rectangle ({self.x},{self.y}) and its length {self.length}, width {self.width}"


square = Square(10, 5, 7)
square.save()
square.load()

rectangle = Rectangle(0, 0, 5, 10)
circle = Circle (3, 1, 14)
ellipse = Ellipse(4, 4, 22, 11)

shapes = []
shapes.append(square.show())
shapes.append(rectangle.show())
shapes.append(circle.show())
shapes.append(ellipse.show())

with open("all_shapes.txt", "w") as file:
    file.writelines(line + "\n" for line in shapes)

with open("all_shapes.txt", "r") as file:
    all_shapes = file.readlines()

all_shapes = [line.strip() for line in all_shapes]  #Removes "\n" at the end of each line
for line in all_shapes:
    print(line)