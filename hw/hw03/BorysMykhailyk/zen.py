import io
import sys

# Хотів спробувати не задавати через змінну а зчитати імпорт
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout

import this

sys.stdout = old_stdout
zen_of_python = new_stdout.getvalue()

# Пошук слів "better", "never", "is"
# Так, жодне з зазначених слів не зустрічаеться з великої літери
zen_of_python_lower = zen_of_python.lower()

# Кількість слів "better"
what_to_find = "better"
count = zen_of_python_lower.count(what_to_find)
print(f"Number of occurence: {count}")
# Положення слів  "better"
start = 0
indexs = []
while (index := zen_of_python_lower.find(what_to_find, start)) != -1:
    indexs.append(index)
    start = index + 1

print(f"location index: {indexs}")

# Кількість слів  "never"
what_to_find = "never"
count = zen_of_python_lower.count(what_to_find)
print(f"Number of occurence: {count}")
# Положення слів  "never"
start = 0
indexs = []
while (index := zen_of_python_lower.find(what_to_find, start)) != -1:
    indexs.append(index)
    start = index + 1

print(f"location index: {indexs}")

# Кількість слів  "is"
what_to_find = "is"
count = zen_of_python_lower.count(what_to_find)
print(f"Number of occurence: {count}")
# Положення слів  "is"
start = 0
indexs = []
while (index := zen_of_python_lower.find(what_to_find, start)) != -1:
    indexs.append(index)
    start = index + 1

print(f"location index: {indexs}")

# Зен великими літерами
print()
print(zen_of_python.upper())

# Зен заміна "i" на "&"
print(zen_of_python.replace('i', '&'))

# Зен заміна всіх (разом з великими) "i" на "&"
zen_of_python_i=zen_of_python.replace('I', 'i')
print(zen_of_python_i.replace('i', '&'))