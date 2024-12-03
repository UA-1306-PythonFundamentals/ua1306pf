# Температурний конвертер
def c_to_f(celsius):
    """Перетворюємо цельсії у фаренгейти."""
    return (celsius * 9 / 5) + 32


while True:
    user_input = input("Введіть температуру в цельсіях (або напишіть 'exit' для виходу): ")

    if user_input.lower() == "exit":
        print("До зустрічі!")
        break

    try:
        celsius = float(user_input)

        if celsius < -273.15:
            print("Помилка: Температура нижча за абсолютний 0 (-273.15°C)")
        else:
            fahrenheit = c_to_f(celsius)
            print(f"{celsius}°C еквівалент {fahrenheit}°F")
    except ValueError:
        print("Невірний ввід. Будьласка введіть правильне число або 'exit'.")
