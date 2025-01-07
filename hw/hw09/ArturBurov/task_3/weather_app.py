import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def get_weather(city):
    """Fetches and displays weather information for the given city."""
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather

        weather_info = f"City: {city}\n"
        weather_info += f"Condition: {w.detailed_status}\n"
        weather_info += f"Wind: {w.wind()}\n"
        weather_info += f"Humidity: {w.humidity}%\n"

        temp = w.temperature('celsius')
        weather_info += f"Temperature: {temp['temp']}°C\n"
        weather_info += f"Feels Like: {temp['feels_like']}°C\n"
        weather_info += f"Min: {temp['temp_min']}°C\n"
        weather_info += f"Max: {temp['temp_max']}°C\n"

        if w.rain:
            weather_info += f"Rain: {w.rain}\n"
        else:
            weather_info += "Rain: No rain\n"

        weather_info += f"Clouds: {w.clouds}%"

        label['text'] = weather_info
        label['font'] = ('Courier', 14)

    except Exception as e:
        label['text'] = f"Error: {e}"
        label['font'] = ('Courier', 12)

    finally:
        # Force resize window
        root.update_idletasks()
        root.geometry("")  # Reset geometry to recalculate window based on its content


def get_weather_on_enter(event):
    """Triggers weather retrieval when Enter key is pressed."""
    get_weather(entry_field.get())


def clear_entry():
    """Clears the entry field."""
    entry_field.delete(0, tk.END)
    label['text'] = ""


root = tk.Tk()
root.title("Weather Application")

# Use grid layout for the root window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)  # Top frame row
root.rowconfigure(1, weight=1)  # Lower frame row

# Frame for entry, button, and clear button
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.grid(row=0, column=0, sticky="ew")

# Use grid layout for the frame
frame.columnconfigure(0, weight=1)  # Entry field expands
frame.columnconfigure(1, weight=0)  # Clear button fixed size
frame.columnconfigure(2, weight=0)  # Get Weather button fixed size

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.grid(row=0, column=0, sticky="ew")
entry_field.bind("<Return>", get_weather_on_enter)

# Clear button (red x)
clear_button = tk.Button(frame, text="X", bg="red", fg="white",
                         font=('Courier', 8), command=clear_entry)
clear_button.grid(row=0, column=1, sticky="e")

button = tk.Button(frame,
                   text="Get Weather",
                   bg="green", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather(entry_field.get()))
button.grid(row=0, column=2, sticky="e")

# Lower frames for the label
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.grid(row=1, column=0, sticky="nsew")

# Use grid layout for the lower frame
lower_frame.columnconfigure(0, weight=1)
lower_frame.rowconfigure(0, weight=1)

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left')
label.grid(row=0, column=0, sticky="nsew")

root.mainloop()
