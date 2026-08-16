### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
from pathlib import Path

current_file = Path(__file__)
new_file = current_file.parent / "hello.txt"
content = "Hello, Python!"

def write_file(filepath: Path, content: str):
    with open(filepath, "w", encoding="utf-8", ) as file:
        file.write(content)

write_file(new_file, content)

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""

def read_file(filepath: Path):
    with open(filepath, "r", encoding="utf-8", ) as file:
        content = file.read()
        return content

content = read_file(new_file)
print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
new_content = "Learning file operations. "

def append_file(filepath: Path, content: str):
    with open(filepath, "a", encoding="utf-8", ) as file:
        file.write(content)

append_file(new_file, new_content)

# content = read_file(new_file)
# print(content)

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
def read_file(filepath: Path):
   with open(filepath, "r", encoding="utf-8", ) as file:
      all_line = file.read()
      return all_line
       
cont = read_file(new_file)

for i in cont:
    if i == "." or i == "!" or i == "?":
        print(i)
    else:
        print(i, end="")
      

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
with open(new_file, "r", encoding="utf -8",) as f:
   amount = f.read()
   print(amount)
   print(f.tell())

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""

current_directory = Path.cwd()
print("Поточна робоча директорія:", current_directory)
new_directory = current_directory / "lesson_08_pathlib" / "data"
new_directory.mkdir(parents=True, exist_ok=True) #mode=0o777,  
print("Директорія створена успішно!")

new_file1 = Path(new_directory) / "notes.txt"
content1 = "My first note."

write_file(new_file1, content1)

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""

all_files = [d for d in new_directory.iterdir() if d.is_file()]
print(all_files)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""

content2 = read_file(new_file1)
new_file2 = Path(new_directory) / "copy.txt"

write_file(new_file2, content2)


"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
content3 = "qwerty asdfg"
content4 = " 123456/.,mnb"

new_file3 = Path(new_directory) / "a.txt"
new_file4 = Path(new_directory) / "b.txt"
new_file5 = Path(new_directory) / "ab.txt"

write_file(new_file3, content3)
write_file(new_file4, content4)

content5 = read_file(new_file3)
content6 = read_file(new_file4)

content56 = content5 + content6

write_file(new_file5, content56)

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""

content7 = read_file(new_file1)

if "note" in content7:
   print("Знайдено")
else:
    print("Не знайдено")