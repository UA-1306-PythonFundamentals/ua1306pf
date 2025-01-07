# Об'єднана програма для OWM.py і Tk_OWM.py

import tkinter as tk
from tkinter import messagebox
import requests  # Використовується для запитів до OpenWeatherMap API (приклад логіки з OWM.py)

# === ЛОГІКА (з OWM.py) ===
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    """Функція для отримання даних про погоду"""
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data['cod'] == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
            return weather
        else:
            return {'error': data.get('message', 'Unknown error')}
    except Exception as e:
        return {'error': str(e)}


# === ГРАФІЧНИЙ ІНТЕРФЕЙС (з Tk_OWM.py) ===
def show_weather():
    """Обробка натискання кнопки 'Показати погоду'"""
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Помилка", "Будь ласка, введіть назву міста")
        return

    result = get_weather(city)
    if 'error' in result:
        messagebox.showerror("Помилка", result['error'])
    else:
        output = (
            f"Місто: {result['city']}\n"
            f"Температура: {result['temperature']}°C\n"
            f"Опис: {result['description']}"
        )
        weather_label.config(text=output)


# === Створення GUI ===
root = tk.Tk()
root.title("Прогноз погоди")

# Поле вводу
tk.Label(root, text="Введіть назву міста:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Кнопка
show_button = tk.Button(root, text="Показати погоду", command=show_weather)
show_button.pack(pady=10)

# Результати
weather_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
weather_label.pack(pady=10)

# Запуск програми
root.mainloop()
