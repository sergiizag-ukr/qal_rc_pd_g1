"""
Домашнє завдання: Основи Python

**1.** Створіть три змінні з правильними іменами (англійською мовою): 
одну для збереження віку, 
одну для імені студента, 
одну для позначення чи є особа студентом. 
Додайте коментарі до кожної змінної.
"""
age = 43 # Age of student
name = "Sergii" # Name of student
student = True # Is she/he a student?
"""

**2.** Рзкоментуйте та виправте помилки в наступних назвах змінних.
Поясніть у коментарях, чому початкові назви неправильні:
"""
name = "John" #ім`я змінної не може починатися з цифри
user_age = 25 # у назві змінної не можна використовувати дефіс (-)
price = 100 # назва змінної не може починатися з спеціального знаку
class_name = "Math" # слово class зарезервоване
"""
**3.** Створіть змінну з описовим ім'ям для збереження максимальної кількості студентів у групі. 
Присвойте їй значення 30.
"""
max_students_in_group = 30

"""
**4.** Створіть змінні для збереження: 
назви курсу, 
кількості годин, 
вартості курсу. 
Використайте правильне іменування змінних.
"""
course_name = "Python"
number_of_hours = 100
cost_of_course = 30000

"""
**5.** Розрхуйте та виведіть Затрати курсу: 
Затрати курсу  = кількість годин / вартість курсу
Використайте правильне іменування змінних.
"""
course_cost = number_of_hours / cost_of_course
print("Course cost is: ", course_cost)

"""
**6.** Створіть змінні з різними способами запису чисел:
- Десяткове число: 42
- Двійкове число: 101010 (в двійковій системі)
- Шістнадцяткове число: 2A (в шістнадцятковій системі)
- Восьмеричне число: 52 (в восьмеричній системі)
"""
decimal_number = 42
binary_number = 0b101010
hexadecimal_number = 0x2A
octal_number = 0o52

"""
**7.** Виконайте всі арифметичні операції (+, -, *, /, //, %, **) з числами 17 та 5. 
Виведіть результати з поясненнями.
"""
number1 = 17
number2 = 5
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_Division = number1 // number2
modulo = number1 % number2
exponentiation = number1 ** number2

print("Addition of two numbers: ", addition)
print("Subtraction of of two numbers: ", subtraction)
print("Multiplication of two numbers: ", multiplication)
print("Division of two numbers: ", division)
print("Floor Division of two numbers: ", floor_Division)
print("Modulo of two numbers: ", modulo)
print("Exponentiation of two numbers: ", exponentiation)



"""
**8.** Обчисліть площу кола з радіусом 7.5. Використайте значення π = 3.14159.
"""
radius = 7.5
pi = 3.14159
circle_area = pi*(radius ** 2)
print("Circle area is: ", circle_area)

"""
**9.** Обчисліть залишок від ділення будь-якого числа на 7. 
Виведіть результат з числами 50, 33, 14.
"""
modulo1 = 50 % 7
modulo2 = 33 % 7
modulo3 = 14 % 7
print("Modulo1 is: ", modulo1)
print("Modulo2 is: ", modulo2)
print("Modulo3 is: ", modulo3)


"""
**10.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436_402 # Area of the Black Sea is 436 402 km2
area_azov_sea = 37_800 # Area of the Azov Sea is 37 800 km2
total_area = area_black_sea + area_azov_sea # Total area of two Seas

print("Total area of the Black and Azov Seas is: ", total_area, "km2")

"""
**11.** Створіть рядок з вашим повним ім'ям та виведіть:
- Перший символ
- Останній символ  
- Довжину рядка
"""
my_name = "Sergii Zagoruiko"
first_symbol = my_name[0]
last_symbol = my_name[-1]
length = len(my_name)

print("The First symbol in my name is: ", first_symbol)
print("The Last symbol in my name is: ", last_symbol)
print("The length of my name is: ", length, "symbols")

"""
**12.** Створіть рядок "Would you tell me, please, which way I ought to go from here?" 
та отримайте з нього підстрічки:
- Перші 6 символів
- Останні 11 символів
"""
speech = "Would you tell me, please, which way I ought to go from here?"
first_6 = speech[:6]
last_11 = speech[-11:]
print("First 6 symbols are: ", first_6)
print("Last 11 symbols are: ",last_11)

"""
**13.** Створіть багаторядковий рядок (використовуючи потрійні лапки) зі своїм улюбленим віршем або цитатою.
"""
favorite_verse = """Борітеся — поборете!
Хай Вам Бог помагає!
За вас правда,
За вас слава
І воля святая!"""
print("My favorite speech for this time is: ", favorite_verse)

"""
**14.** Поєднайте два рядки "Hello" та "World" у різні способи (з пробілом, з комою, з новим рядком).
"""
word1 = "Hello"
word2 = "World"

print(word1 + ' ' + word2)
print(word1 + ', ' + word2)
print(word1 + '\n' + word2)

"""
**15.** Створіть рядок з символами, які потребують екранування (лапки, зворотна коса риска).
"""
sentence1 = "Його звати \"Арт\""
sentence2 = "Його звати \\Арт\\"
sentence3 = "Його звати -Арт-" # не зрозумів чи потрібно було робити окремо зворотню косу з рискою, чи разом
sentence4 = "Його звати -\\Арт\\-" # не зрозумів чи потрібно було робити окремо зворотню косу з рискою, чи разом
print("З лапками: ", sentence1)
print("З зворотньою косою окремо : ", sentence2)
print("З рискою окремо : ", sentence3)
print("З зворотньою косою та рискою разом : ", sentence4)

"""
**16.** Напишіть код, який запитує у користувача його ім'я та вік, 
а потім виводить привітання у форматі: "Привіт, [ім'я]! Тобі [вік] років."
"""
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello {name}! You are {age} years old.")

"""

**17.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
igor_photos = 232 # The total quantity of photos which Igor has
photos_page = 8 # The max quantity of photos in one page
pages_album = igor_photos // photos_page

print(f"Igor needs {pages_album} pages in his album to paste all his photos")

"""
**18.** Напишіть код який запитує у користувача 
його улюблений колір та число, а потім створює персоналізоване
повідомлення використовуючи f-string форматування.
"""
color = input("What is your favorite color?")
number = input("What is your favorite number?")

print(f"Hello. Your favorite color is {color}. Your favorite number is {number}")


"""
**19.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

store1_2 = 250_449 #The first and second stores have 250 449 goods
store2_3 = 222_950 #The second and third stores have 222 950 goods.
store1_2_3 = 375_291 #total quantity of goods in 3 stores is  375 291 
store3 = store1_2_3 - store1_2 # definding quantity of good in the third store 
store1 = store1_2_3 - store2_3 # definding quantity of good in the first store 
store2 = store1_2_3 - store1 - store3 # definding quantity of good in the first store

#print(store1_2_3 - store1 - store2 - store3)
print(f"The first store has {store1} goods. The second store has {store2} goods. The third store has {store3} goods")

"""
**20.** Переведіть задачу з книги "Математика, 5 клас"
на мову пітон і виведіть відповідь, так, щоб було
зрозуміло дитині, що навчається в п'ятому класі:
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_term = 18 # term of partial payment in months
month_payment = 1179 # payment for 1 month in grivnas
total_pc_cost = month_payment * payment_term # total cost of pc

print(f"The total cost of pc is {total_pc_cost} grivnas")
