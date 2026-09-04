adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_replace1 = adwentures_of_tom_sawer.replace("\n", " ")
print("TEXT WITHOUT \\n : ", adwentures_of_tom_sawer_replace1)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_replace2 = adwentures_of_tom_sawer.replace("....", " ")
print("TEXT WITHOUT .... : ", adwentures_of_tom_sawer_replace2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_split = adwentures_of_tom_sawer.split(" ")
adwentures_of_tom_sawer_join = " ".join(adwentures_of_tom_sawer_split)
print("TEXT WITH ONE GAP: ", adwentures_of_tom_sawer_join)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
numbers_of_h = adwentures_of_tom_sawer.count("h")
print( f"The text has 'h' {numbers_of_h} times")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
numbers_A = adwentures_of_tom_sawer.count("A")
numbers_B = adwentures_of_tom_sawer.count("B")
numbers_C = adwentures_of_tom_sawer.count("C")
numbers_D = adwentures_of_tom_sawer.count("D")
numbers_E = adwentures_of_tom_sawer.count("E")
numbers_F = adwentures_of_tom_sawer.count("F")
numbers_G = adwentures_of_tom_sawer.count("G")
numbers_H = adwentures_of_tom_sawer.count("H")
numbers_I = adwentures_of_tom_sawer.count("I")
numbers_J = adwentures_of_tom_sawer.count("J")
numbers_K = adwentures_of_tom_sawer.count("K")
numbers_L = adwentures_of_tom_sawer.count("L")
numbers_M = adwentures_of_tom_sawer.count("M")
numbers_N = adwentures_of_tom_sawer.count("N")
numbers_O = adwentures_of_tom_sawer.count("O")
numbers_P = adwentures_of_tom_sawer.count("P")
numbers_Q = adwentures_of_tom_sawer.count("Q")
numbers_R = adwentures_of_tom_sawer.count("R")
numbers_S = adwentures_of_tom_sawer.count("S")
numbers_T = adwentures_of_tom_sawer.count("T")
numbers_U = adwentures_of_tom_sawer.count("U")
numbers_V = adwentures_of_tom_sawer.count("V")
numbers_W = adwentures_of_tom_sawer.count("W")
numbers_X = adwentures_of_tom_sawer.count("X")
numbers_Y = adwentures_of_tom_sawer.count("V")
numbers_Z = adwentures_of_tom_sawer.count("Z")

total = numbers_A + numbers_B + numbers_C + numbers_D + numbers_E + numbers_F + numbers_G + numbers_H + numbers_I + numbers_J + numbers_K + numbers_L + numbers_M + numbers_N + numbers_O + numbers_P + numbers_Q + numbers_R + numbers_S + numbers_T + numbers_U + numbers_V + numbers_W + numbers_X + numbers_Y + numbers_Z
print (f"The text has {total} capital letters")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
position1 = adwentures_of_tom_sawer.find("Tom")
position2 = adwentures_of_tom_sawer.find("Tom", position1 + 1)

#print("first position: ", position1)
print("second position: ", position2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_replace1 = adwentures_of_tom_sawer.replace("....", " ")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_replace1.split(".")
print("Separated by sentence: ", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

sentence4 = adwentures_of_tom_sawer_sentences[3]
print("FORTH SENTENCE: ", sentence4.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

a = adwentures_of_tom_sawer.find("By the time") #startswith не працює. тільки через цикл for
print(a)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
sentencelast = adwentures_of_tom_sawer_sentences[-2]
lastsentence_sep = len(adwentures_of_tom_sawer_sentences[-2].split(" "))
print("Numbers of words: ", lastsentence_sep)