
text = input("Введіть текст: ")# Введення тексту від користувача


words = text.lower().split()  # Розбиття текст на слова

count_of_better = 0
count_of_never = 0
count_of_is = 0

for word in words:
    if word == "better":
        count_of_better += 1

for word in words:
    if word == "never":
        count_of_never += 1

for word in words:
    if word == "is":
        count_of_is += 1

# Заміна всіх символів 'i' на '&' за допомогою циклу
modified_text = ""
for char in text:
    if char == "i":
        modified_text += "&"
    elif char == "I":
        modified_text += "&"
    else:
        modified_text += char

final_text = modified_text.upper()# Перетворення тексту у верхній регістр

# Вивід результатів
print(f"Змінений текст: {final_text}")
print(f"Кількість входжень слова 'better': {count_of_better}")
print(f"Кількість входжень слова 'never': {count_of_never}")
print(f"Кількість входжень слова 'is': {count_of_is}")
