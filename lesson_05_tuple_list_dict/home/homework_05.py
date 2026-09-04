# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unigue = set(small_list)
print("unigue list:", unigue)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
amount = 0
summa = 0

for index in small_list:
    amount += 1
    summa = summa + index

average = summa/amount
print("average is: ", average)


# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
amount = 0
for index in big_list:
    if big_list.count(index) > 1:
        amount += 1

if amount > 0:
    print("big list has duplicates")
else:
    print("big list does not have duplicates")


# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

max_value =0
name_key = ""

for key in add_dict:
    if add_dict[key] > max_value:
        max_value = add_dict[key]
        name_key = key

print(f"dictionary with key: '{name_key}' has the biggest value '{max_value}'")
print(add_dict[name_key])


# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})

new_key = ""
new_value = ""
new_dict = {}

for key in base_dict:
    new_key = base_dict[key]
    new_value = key
    new_dict[new_key] = new_value

print("new dictionary with exchanged keys and values: ", new_dict)



# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict.copy()
new_value = ""
for key_bd in base_dict:
    for key_ad in add_dict:
        if key_bd == key_ad:
            new_value = str(base_dict[key_bd]) + str(add_dict[key_ad])
            sum_dict[key_bd] = new_value
        else:
            sum_dict[key_ad] = add_dict[key_ad]

print(sum_dict)



# task 7.
line = "Створіть список з всіх символів, які входять у заданий рядок"

line_sep = list(line)
print(line_sep)

# task 8. Обчисліть суму елементів двох змінних через sum()
value_1  = [1, 2, 3, 4, 5]
value_2 = (4, 6, 5, 10)

total1 = sum(value_1)
total2 = sum(value_2)
total = total1 + total2

print("Sum of two values is: ", total)
