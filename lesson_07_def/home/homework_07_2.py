# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9



# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summa(a, b):
    return(f"{a} + {b} = {a+b}")

print(summa(6, 7))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

numbers = [1, 2, 3, 4, 5]

def avarage_number(numbers):
    summa = 0
    count = 0
    avarage_num = 0

    for i in numbers:
        summa +=i
        count +=1

    avarage_num = summa / count

    return f" avarage number is {avarage_num}"

print(avarage_number(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

text = "Доброго вечора пане господаре"

words = text.split()
count = len(words)


def reverse(text):
    words = text.split()
    count = len(words)
    reverse_text = ""
    while count != 0:
        reverse_text = reverse_text + words[count-1] + " "
        count -=1
    return reverse_text

print(reverse(text))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
words = ["banana", "apple", "orange", "pineapple"]

def longest_word(words):
    longest = ""
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest

print(longest_word(words))



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    for i in range(len(str1)):
        if str1[i:i + len(str2)] == str2:
            return i

    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # -1

# task 7
# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

password = input("password: ")

def lenth_pass(password):
    """Перевіряє кількість символів у паролі. Повинно бути не меньше 8"""
    lenth = len(password)
    if lenth >=8:
        return("the lenth of password is enough")
    else:
        return("the lenth of password is not enough")

print(lenth_pass(password))

# task 8
# Вправа 4: Лічильник голосних
text = input("Введіть текст: ").lower()

def count_vowels(text):
    """Підраховує кількість голосних у тексті"""
    vowels = "аеиіїоуюя"
    count = 0

    for symb in text:
        if symb in vowels:
            count +=1
    return (f"Кількість голосних: {count}")

print(count_vowels(text))


# task 9

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

def duplicat(numbers):
    """Перевіряє, чи є у списку дублікати."""
    amount = 0
    for index in numbers:
        if numbers.count(index) > 1:
            amount += 1

    if amount > 0:
        return("big list has duplicates")
    else:
        return("big list does not have duplicates")

print(duplicat(big_list))

# task 10
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

def key_max_value(dict):
    """ знаходить ключ з максимальним значенням у словнику """
    max_value =0
    name_key = ""

    for key in dict:
        if dict[key] > max_value:
            max_value = dict[key]
            name_key = key

    return (f"dictionary with key: '{name_key}' has the biggest value '{max_value}'")

print (key_max_value(add_dict))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""