from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def dummy(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


shape1 = Rectangle(4, 5)
shape2 = Circle(3)

print(type(shape1).__name__)
print('Area:', shape1.area())
print('Perimeter:', shape1.perimeter())

print(type(shape2).__name__)
print('Area:', shape2.area())
print('Perimeter:', shape2.perimeter())
