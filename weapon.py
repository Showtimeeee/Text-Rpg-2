class Weapon:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type

    def __str__(self):
        return f"{self.name} ({self.damage} урона, тип: {self.type})"
