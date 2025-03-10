class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.weight}kg, {self.height}cm"
