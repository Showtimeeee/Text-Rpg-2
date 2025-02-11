class Armor:
    def __init__(self, name, defense, type):
        self.name = name
        self.defense = defense
        self.type = type

    def __str__(self):
        return f"{self.name} (+{self.defense} брони, тип: {self.type})"
