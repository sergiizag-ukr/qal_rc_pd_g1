# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

password = input("password: ")
lenth = len(password)

if lenth >=8:
    print("the lenth of password is enough")
else:
    print("the lenth of password is not enough")

# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 І не ділиться на 100")
print("- АБО ділиться на 400")

year = int(input("enter yer: "))

if (year %4 == 0 and year%100 != 0) or year%400 == 0:
    print("Рік є високосним")
else:
    print("Рік не високосний")


# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

text = input("Введіть текст: ").lower()
vowels = "аеиіїоуюя"
count = 0

for symb in text:
    if symb in vowels:
        count +=1

print(f"Кількість голосних: {count}")


# Вправа 5: Гра 
print("\n=== ВПРАВА 5: Гра ===")
"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""

alien_color = input("'green', 'yellow', або 'red': ")

if alien_color == "green":
    print("you get 5 balls")
elif alien_color == "yellow":
    print("you get 10 balls")
elif alien_color == "red":
    print("you get 15 balls")


# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

filling =""

while True:
    ingredient = input("яку начинку ви бажаєте? ")

    if ingredient == "quit":
        break

    filling = filling + " " + ingredient    

print("Ви замовили начинку з - ", filling)



# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

numbers = range(10)
number_len= len(numbers)
for i in numbers:
    print(number_len - i-1)

# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

number1 = 1
number2 = 1

while number1 != 0 and number2 != 0 :
    number1 = int(input("enter the number 1: "))
    number2 = int(input("enter the number 2: "))

    if number1 == 0 or number2 == 0:
        break
    elif number1 > number2:
        print(f"number1 '{number1}' is more than number2 '{number2}'")
    elif number2 > number1:
        print(f"number2 '{number2}' is more than number1 '{number1}'")
    else:
        print(f"number1 '{number1}' is equal number2 '{number2}'")


# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for i in fruits:
    if i == "orange":
        continue
    else:
        print(i)

# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
print(result)  #  [4, 16, 36, 64, 100]
counter = 0
for i in numbers:
    if i %2 == 0:
        counter +=1
        result.extend([i **2])

print(result)

result = [i**2 for i in numbers if i%2 == 0]

print(result)