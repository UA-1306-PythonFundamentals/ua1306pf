l=list(range(1, 11)) 
lEven=[] # Пустий список парних чисел
lOdd=[] # Пустий список чисел дільником яких є 3
lNone=[] # Пустий список для чисел які не входять в перші два
# Перевірка на необхідні умови
for i in l:
    if i % 2 == 0:
        lEven.append(i)
    if i % 3 == 0:
        lOdd.append(i)
    if i % 2 != 0 and i % 3 != 0:
        lNone.append(i)
# Виведення інформації
print("List of even numbers that are divisible by 2:\n", 
      lEven,
     "\nList of odd numbers which are divisible by 3:\n",
     lOdd,
     "\nList of numbers thst are not divisible by 2 and 3:\n",
     lNone
     )