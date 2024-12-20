import tkinter as tk
from pyowm.owm import OWM

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather(city_name):
    try:
        observation = mgr.weather_at_place(city_name)
        weather = observation.weather
        status = weather.detailed_status
        temperature = weather.temperature('celsius')['temp']
        wind = weather.wind()['speed']
        humidity = weather.humidity
        rain = weather.rain.get('1h', 0)
        temperature_f = (temperature * 9/5) + 32
        rh = humidity/100
        heat_index_f = temperature_f - (0.55 * (1 - rh) * (temperature_f - 58))
        heat_index = round((heat_index_f - 32) * 5/9, 1)
        result = (
            f"Status: {status}\n"
            f"Temperature: {temperature}°C\n"
            f"Wind Speed: {wind} m/s\n"
            f"Humidity: {humidity} %\n"
            f"Rain (last 1 hour): {rain} mm\n"
            f"Heat index: {heat_index}°C"
        )
    except Exception as e:
        result = f"Error: {str(e)}"
    label['text'] = result

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

