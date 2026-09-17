from functools import reduce

### Завдання 1. Охоронці воріт

passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "valiD1pass",
]
def is_strong(password):
    
    return 8 <= len(password) <= 20 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and " " not in password



result1 = list(filter(lambda password: is_strong(password), passwords))
result2 = list(filter(lambda password: not is_strong(password), passwords))
print(result1)
print(result2)


### Завдання 2. Перепис козацького реєстру

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]

def registry(registr):

    list_dict = {}
    line = registr.split("|")
    list_dict = {
        "name": line[0].strip().title(),
        "rank":  line[1].strip().title(),
        "warriors": int(line[2].strip())
    }
    return list_dict
    


result3 = list(map(registry, raw_registry))

result4 = list(filter(lambda i: i["warriors"] > 0, result3))
#print(result4)


result5 = reduce(lambda count, i : count + i["warriors"], result4, 0)

result6 = sorted(result4, key= lambda i: i["warriors"], reverse=True)

print(f"Козацький реєстр ({len(result6)} записи):")
print("─" * 50)
print(f"{'№':<3} {'Імʼя':<25} {'Посада':<12} {'Воїни'}")
print("─" * 50)

for number, item in enumerate(result6, start=1):
    print(
        f"{number:<3} "
        f"{item['name']:<25} "
        f"{item['rank']:<12} "
        f"{item['warriors']}"
    )

print("─" * 50)
print(f"Разом воїнів: {result5}")

### Завдання 3. Пошук козацьких шифрів

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]



palindromes = list(
    filter(lambda message: is_palindrome(message), messages)
)


result = list(
    map(
        lambda message: f"🔐 {message} → {message.lower().replace(' ', '')[::-1]}",
        palindromes
    )
)

for message in result:
    print(message)