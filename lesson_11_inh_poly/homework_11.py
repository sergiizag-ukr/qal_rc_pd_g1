class Cossack:

    def __init__(self, name: str, kurin: str):
        self.name = name
        self.kurin = kurin
        self.weapons = []
        self.victories = 0
        self.rank = "козак"

    def arm(self, weapon):

        if weapon in self.weapons:
            return f"{self.name} вже має {weapon}!"
        else:
            self.weapons.append(weapon)

    def win_battle(self, enemy):
        self.victories +=1

        if self.victories >= 3 and self.victories < 7:
            self.rank = "осавул"
        elif self.victories >= 7:
            self.rank = "полковник"

        return f"{self.name} переміг {enemy}! Слава козаку!"
    
    

    def __str__(self):
        return f"Козак {self.name} | Курінь: {self.kurin} | Перемоги: {self.victories} | Зброя: {', '.join(self.weapons)}"
            


# Ivan = Cossack("Іван Сірко", "Кальміуський")
# Ivan.arm("шабля")
# Ivan.arm("мушкет")
# print(Ivan.win_battle("москалі"))
# print(Ivan)


class ZaporozhianSich:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.cossacks = []
        

    def enlist(self, cossack):

        for c in self.cossacks:
            if c.name == cossack.name:
                return f"{cossack.name} вже на Січі!"

        if len(self.cossacks) >= self.capacity:
            return "Січ переповнена!"
        
        self.cossacks.append(cossack)

    def dismiss(self, name):
        for c in self.cossacks:
            if c.name == name:
                self.cossacks.remove(c)
                return
            
        return f"Козака {name} не знайдено!"

    def call_to_battle(self, enemy):
        if len(self.cossacks) == 0:
            return "Нікому боронити Січ!"
        else:
            return f"Військо Запорозьке виступає проти {enemy}! У поході {len(self.cossacks)} козаків!"

    def best_warrior(self):

        if len(self.cossacks) == 0:
            return "Січ порожня!"

        best = self.cossacks[0]

        for c in self.cossacks:
            if c.victories > best.victories:
                best = c
        return best

    def roster(self):

        if len(self.cossacks) == 0:
                    return "На Січі нікого немає"

        name = []

        for c in self.cossacks:
            name.append(c.name)

        return name

    def promote_all(self):

        for c in self.cossacks:
            if c.victories >= 7:
                c.rank = "полковник"
            elif c.victories >= 3:
                c.rank = "осавул"
            else:
                c.rank = "козак"


sich = ZaporozhianSich("Чортомлицька Січ", capacity=3)

ivan = Cossack("Іван Сірко", "Кальміуський")
petro = Cossack("Петро Сагайдачний", "Канівський")

ivan.win_battle("яничари")
ivan.win_battle("татари")
petro.win_battle("поляки")

sich.enlist(ivan)
sich.enlist(petro)

print(sich.call_to_battle("москалі"))
print(sich.best_warrior())
print(sich.roster())

