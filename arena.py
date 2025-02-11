import random
from warrior import Warrior
from mage import Mage
from weapon import Weapon
from armor import Armor

class Arena:
    def __init__(self):
        self.weapons = [
            Weapon("Доска с ржавым гвоздем", 10, "Warrior"),
            Weapon("Топор", 15, "Warrior"),
            Weapon("Щит", 5, "Warrior"),
            Weapon("Посох", 12, "Mage"),
            Weapon("Книга заклинаний", 18, "Mage"),
            Weapon("Амулет огня", 8, "Mage")
        ]

        self.armors = [
            Armor("Железная броня", 12, "Warrior"),
            Armor("Кожаная броня", 6, "Warrior"),
            Armor("Пластинчатая броня", 18, "Warrior"),
            Armor("Шляпа", 5, "Mage"),
            Armor("Ботинки", 3, "Mage"),
            Armor("Плащ", 10, "Mage")
        ]

        self.characters = []

    def create_characters(self):
        warrior = Warrior("Воин")
        mage = Mage("Маг")
        self.characters.append(warrior)
        self.characters.append(mage)

    def start_battle(self):
        print("************************************************************ АРЕНА ************************************************************")
        print('_____________________________________________________________________________________________')
        print(f"Багровые лучи закатного солнца заливают арену зловещим кровавым светом. Воин, исполненный ярости, испускает пронзительный боевой клич, готовясь обрушить на врага шквал сокрушительных ударов. В то же время Маг, воздев руки к небесам, призывает всю мощь солнечной энергии, готовясь обрушить на противника сокрушительные магические потоки. Воздух сгущается от напряжения, предвещая грядущую схватку не на жизнь, а на смерть.")
        print('_____________________________________________________________________________________________')
        self.create_characters()
        first_turn = random.choice(self.characters)
        
        while True:
            random.shuffle(self.characters)
            for character in self.characters:
                if character.health > 0:
                    print(f"{character.name} начинает бой!\n")
                    print(f"\nХод {character.name}:\n{character}\n1. Нанести удар\n2. Подобрать оружие\n3. Подобрать броню\n4. Пропустить ход\n5. Завершить поединок")
                    action = input("Выберите действие: ")
                    print()

                    if action == "1":
                        target = self.get_opponent(character)
                        if target:
                            character.attack(target)
                            if target.health <= 0:
                                return character
                        else:
                            print("Нет противника!")
                    elif action == "2":
                        self.show_weapons(character)
                    elif action == "3":
                        self.show_armors(character)
                    elif action == "4":
                        print(f"{character.name} пропускает ход.")
                    elif action == "5":
                        print("Поединок завершен досрочно.")
                        return None
                    else:
                        print("неерный выбор действия")

    def get_opponent(self, character):
        for other_character in self.characters:
            if other_character != character:
                return other_character
        return None

    def show_weapons(self, character):
        available_weapons = [weapon for weapon in self.weapons if weapon not in [c.weapon for c in self.characters]]
        
        if available_weapons:
            print("На песке лежит оружие:")
            
            for i, weapon in enumerate(available_weapons):
                print(f"{i+1}. {weapon}")
                
            choice = int(input("Выберите оружие: "))
            
            if choice > 0 and choice <= len(available_weapons):
                weapon = available_weapons[choice-1]
                character.equip_weapon(weapon)
                self.weapons.remove(weapon)
            else:
                print("Неверный выбор оружия!")
        else:
            print("оружие украли гоблины")

    def show_armors(self, character):
        print("Доступная броня:")
        
        for i, armor in enumerate(self.armors):
            print(f"{i+1}. {armor}")
            
        choice = int(input("Выберите броню: "))
        
        if choice > 0 and choice <= len(self.armors):
            armor = self.armors[choice-1]
            character.equip_armor(armor)
            self.armors.remove(armor)
        else:
            print("неверный выбор брони!")

if __name__ == "__main__":
    arena = Arena()
    winner = arena.start_battle()
    if winner:
        print()
        print(f"Да здравствует: {winner.name}!")
