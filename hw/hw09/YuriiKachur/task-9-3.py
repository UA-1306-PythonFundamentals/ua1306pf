import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450

# Your OpenWeatherMap API key
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Initialize the OWM object and weather manager
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Create the main window for the Tkinter application
root = tk.Tk()
root.title("Weather Application")

# Create a canvas to hold the elements
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Create a frame for the input and button
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Entry field for city name
entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

# Function to get the weather information and update the label
def get_weather():
    # Get the city entered in the input field
    city_name = entry_field.get()

    try:
        # Fetch the weather information for the city
        observation = mgr.weather_at_place(city_name)
        w = observation.weather

        # Extract weather details
        detailed_status = w.detailed_status  # weather status (e.g. 'clouds')
        wind = w.wind()  # wind speed and direction
        humidity = w.humidity  # humidity level
        temperature = w.temperature('celsius')  # temperature in Celsius
        temp = temperature['temp']
        temp_max = temperature['temp_max']
        temp_min = temperature['temp_min']

        # Format the weather information as a string
        weather_info = f"Weather: {detailed_status}\n"
        weather_info += f"Temperature: {temp}°C (Max: {temp_max}°C, Min: {temp_min}°C)\n"
        weather_info += f"Wind: {wind['speed']} m/s, Direction: {wind['deg']}°\n"
        weather_info += f"Humidity: {humidity}%"

        # Update the label with the weather information
        label.config(text=weather_info)
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

# Create the "Get Weather" button that calls the get_weather function
button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Frame for displaying the weather information
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Label to show the weather details
label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Start the Tkinter event loop
root.mainloop()
