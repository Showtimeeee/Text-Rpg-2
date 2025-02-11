import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = None  
        self.weapon = "Кулаки" 

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.finisher()  #  фаталити при смерти
            print(f"{self.name} повержен!")

    def finisher(self):
        finishers = [
        f"У {self.name} оторвало голову! Она покатилась по арене, словно тыква.",
        f"{self.name}у пронзили сердце! Из раны фонтаном брызнула кровь, окрасив песок в багровый цвет.",
        f"{self.name} вспомнил лица сыновей и упал замертво. Его последние мысли были о семье, которую он больше никогда не увидит.",
        f"Внезапно у {self.name} хлынула струя крови из шеи, это конец. Он замер, словно кукла, с широко раскрытыми глазами.",
        f"{self.name} рухнул на колени, хватаясь за живот, где зияла рана. Кровь залила его тело, превращая его в кровавое месиво.",
        f"У {self.name} отделилась рука, летя в воздух, словно кусок мяса. Он смотрел на нее с ужасом, не веря своим глазам.",
        f"{self.name} попытался подняться, но его ноги не слушались. Он упал, сжимая грудь, где билось его сердце. Вскоре оно затихло.",
        f"{self.name} закричал от боли, его лицо исказилось гримасой ужаса.  Он попытался  схватиться  за  рану,  но  упал  и  умер."]
        print(random.choice(finishers))

    def equip_weapon(self, weapon):
        if weapon.type == self.type:
            self.weapon = weapon
            self.damage += weapon.damage
            print(f"{self.name} взял {weapon.name}!")
        else:
            print(f"{self.name} не может использовать {weapon.name}!")

    def equip_armor(self, armor):
        if armor.type == self.type:
            self.armor = armor
            self.health += armor.defense
            print(f"{self.name} взял {armor.name}!")
        else:
            print(f"{self.name} не может использовать {armor.name}!")

        

    def attack(self, target):
        attack_verbs = [
        "с яростью обрушил на противника град сокрушительных ударов, сотрясая тело у",
        "с оглушительным ревом нанес серию мощных ударов, обливая арену брызгами крови",
        "стремительно ринулся вперед, обрушив на врага серию жестоких ударов",
        "взмахнул оружмем, рассекая плоть противника и вызывая фонтан алой крови у",
        "с силой опустил оружие, глубоко вонзая его в плечо врага, заставив вскрикнуть от боли",
        "мощным ударом ноги в живот отбросил противника назад, выбивая дух из",
        "обрушил на голову врага град жестоких ударов, сотрясая сознание у"]
        
        if target.armor:  # проверяем, надета ли броня
            final_damage = self.damage - target.armor.defense
        else:
            final_damage = self.damage
        if final_damage > 0:
            
            attack_verb = random.choice(attack_verbs)
            print(f"{self.name} {attack_verb} {target.name}, нанеся {final_damage} урона!")
            target.take_damage(final_damage)
            print()

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health}, Урон: {self.damage}, Броня: {self.armor}, Оружие: {self.weapon})"
