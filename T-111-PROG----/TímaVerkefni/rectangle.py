from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width = 0):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2