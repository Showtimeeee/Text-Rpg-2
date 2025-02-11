from character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self.type = "Warrior"
