
class Food:
    def __init__(self):
        self.protein = 0


class Grain(Food):
    def __init__(self):
        super().__init__()
        self.protein = 1
        self.fructose = 3


rice = Grain()
print(rice.protein, rice.fructose)