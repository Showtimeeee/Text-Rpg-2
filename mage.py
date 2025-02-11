from character import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 20)
        self.type = "Mage"
