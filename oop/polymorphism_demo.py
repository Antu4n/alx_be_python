import math#
class Shape: 
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length
    def area(self): 
        return self.width * self.length
class Circle(Shape):    
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()