class Shape:
    def __str__(self):
        return f"{type(self).__name__} with area of {round(self.get_area(), 2)} and perimeter of {round(self.get_perimeter(), 2)}"