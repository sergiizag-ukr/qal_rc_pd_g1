from abc import ABC, abstractmethod

# Завдання 1: Клас `MagicCreature`

class MagicCreature(ABC):

    def __init__(self, name: str, magic_level: int, health: int):

        if magic_level < 1 or magic_level > 10:
            raise ValueError("Рівень магії має бути від 1 до 10!")

        if health < 0 or health > 100:
            raise ValueError("Здоров'я має бути від 0 до 100!")
        
        self.name = name
        self._magic_level = magic_level
        self.__health = health
        self.__alive = True

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):

        if value > 100:
            raise ValueError("Здоров'я має бути від 0 до 100!")
        
        if value <= 0 :
            self.__alive = False
            self.__health = 0
        else:
            self.__health = value

        return self.__health

    @property
    def magic_level(self):
        return self._magic_level

    @magic_level.setter
    def magic_level(self, value: int):
        if value < 1 or value > 10:
            raise ValueError("Рівень магії має бути від 1 до 10!")
        else:
            self._magic_level = value

    @property
    def is_alive(self):
        return self.__alive

    @abstractmethod
    def use_ability(self):
        """кожна підістота **зобов'язана** реалізувати цей метод"""
        pass

    @abstractmethod
    def describe(self):
        """ повертає опис істоти у довільному форматі — кожен підклас описує себе по-своєму"""
        pass

    def take_damage(self, amount):
        if not self.__alive:
            return f"{self.name} вже переміг смерть... або ні."

        self.health -= amount

        

    def __str__(self):
        return f" {self.name} | Магія: {self._magic_level} | HP: {self.__health} | Живий: {self.__alive}"

class Molfar(MagicCreature):

    def __init__(self, name: str, magic_level: int, health: int, element: str, spells: int):
        super().__init__(name, magic_level, health)
        self.element = element
        self.spells = spells

    def use_ability(self):
        if self.__spells > 0:
            self.__spells -= 1
            return f"Мольфар {self.name} закликає {self.element}! Залишилось заклинань: {self.__spells}"
        else:
            return f"Мольфар {self.name} виснажений — сила стихій покинула його!"

    def describe(self):
        return f"Мольфар {self.name}, повелитель стихії {self.element}. Рівень магії: {self._magic_level}"

    @property
    def spells(self):
        return self.__spells

    @spells.setter
    def spells(self, spells: int):
        if spells < 0:
            raise ValueError("заклинань повинно бути більше нуля")
        self.__spells = spells
        
        
class Rusalka(MagicCreature):

    def __init__(self, name: str, magic_level: int, health: int, river, charm_power: int):
        super().__init__(name, magic_level, health)
        self.river = river
        self.__charm_power = charm_power

    def use_ability(self):
        result = f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.__charm_power}"

        if self.__charm_power == 5:
            result += " Ніхто не встоїть!"

        return result

    @property
    def charm_power(self):
        return self.__charm_power

    @charm_power.setter
    def charm_power(self, value):
        if value < 0 or value > 5:
            raise ValueError("діапазон повинен бути від 1 до 5")
        self.__charm_power = value

    def describe(self):
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.__charm_power}/5"

class Perelesnyk(MagicCreature):

    def __init__(self, name: str, magic_level: int, health: int, speed: int, form = "вогняна куля"):
        super().__init__(name, magic_level, health)
        self.speed = speed
        self.form = form

    def use_ability(self):
        if self.form == "людська":
            return f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.speed}! Форма: {self.form}. Ніхто не здогадається..."
        else:
            return f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.speed}! Форма: {self.form}."

    def describe(self):
        return f"Перелесник {self.name}. Швидкість: {self.speed}. Зараз у формі: {self.form}"

    def change_form(self):
        if self.form == "вогняна куля":
            self.form = "людська"
        else:
            self.form = "вогняна куля"

        return f"Перелесник перетворився на {self.form}!"

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        if speed < 1 or speed > 100:
            raise ValueError("Швидкість має бути від 1 до 100")
        self.__speed = speed


class EnchantedForest():

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.__creatures = []
        self.capacity = capacity

    def add_creature(self, creature: MagicCreature):
        if len(self.__creatures) >= self.capacity:
            return f"Зачарований ліс {self.name} переповнений!"
        if not creature.is_alive:
            return "Мертві істоти не можуть оселитись у лісі!"
        for exist_creature in self.__creatures:
            if exist_creature.name == creature.name:
                return f"{creature.name} вже мешкає у цьому лісі!"

        self.__creatures.append(creature)

    def remove_creature(self, name):
        for exist_creature in self.__creatures:
            if exist_creature.name == name:
                self.__creatures.remove(exist_creature)
                return
            
        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self):

        level = 0
        powerfull = ""

        if len(self.__creatures) == 0:
            return "Ліс порожній — нема кому чаклувати!"
        for c in self.__creatures:
            if c.magic_level > level :
                level = c.magic_level
                powerfull = c.name
        return f"{powerfull} is the most powerful creature in the forrest"

    def attack_intruder(self, intruder_name):
        abilities =[]

        if len(self.__creatures) == 0:
            return f" Ліс беззахисний перед {intruder_name}!"
        for c in self.__creatures:
            if c.is_alive:
                abilities.append(c.use_ability())
        return abilities

    def census(self):

        descriptions = []
        if len(self.__creatures) == 0:
            return " Ліс порожній"
         
        for c in self.__creatures:
            descriptions.append(c.describe())

        return descriptions

    @property
    def creatures_count(self):
        amount = 0
        for c in self.__creatures:
            if c.is_alive:
                amount += 1
        return amount

forest = EnchantedForest("Чорний Ліс", capacity=5)

molfar = Molfar("Юрій", magic_level=8, health=90, element="вогонь", spells=3)
rusalka = Rusalka("Калина", magic_level=6, health=100, river="Дніпро", charm_power=5)
perelesnyk = Perelesnyk("Іскра", magic_level=7, health=85, speed=95, form="вогняна куля")

forest.add_creature(molfar)
forest.add_creature(rusalka)
forest.add_creature(perelesnyk)
    
print(forest.most_powerful())
print(forest.attack_intruder("мисливець"))

molfar.take_damage(90)
print(molfar.is_alive)

print(forest.census())




