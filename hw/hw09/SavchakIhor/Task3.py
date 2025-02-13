import tkinter as tk
from pyowm import OWM

class WeatherApp:
    def __init__(self, root, api_key):
        self.root = root
        self.api_key = api_key
        self.owm = OWM(api_key)
        self.mgr = self.owm.weather_manager()

        # Window properties
        self.root.title("Weather Application")
        self.root.geometry("450x350")

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Canvas for general layout
        self.canvas = tk.Canvas(self.root, height=350, width=450)
        self.canvas.pack()

        # Frame for city input and button
        self.frame = tk.Frame(self.root, bg="deep sky blue", bd=5)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        # Entry for city name
        self.entry_field = tk.Entry(self.frame, font=('Courier', 12))
        self.entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        # Button to get weather information
        self.button = tk.Button(self.frame, text="Get Weather", bg="gray", fg="white", font=('Courier', 8), command=self.get_weather)
        self.button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        # Frame for displaying weather information
        self.lower_frame = tk.Frame(self.root, bg='gold', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        # Label for displaying results
        self.label = tk.Label(self.lower_frame, font=('Courier', 14))
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)

    def get_weather(self):
        city = self.entry_field.get().strip()  # Remove any surrounding whitespaces
        if city:
            try:
                observation = self.mgr.weather_at_place(city)
                weather = observation.weather

                # Extract weather details
                detailed_status = weather.detailed_status
                wind = weather.wind()
                humidity = weather.humidity
                temperature = weather.temperature('celsius')

                # Format and display the weather info
                weather_info = (
                    f"Weather: {detailed_status}\n"
                    f"Temperature: {temperature['temp']}°C\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind['speed']} m/s\n"
                )
                self.label.config(text=weather_info)

            except Exception as e:
                self.label.config(text=f"Error: {str(e)}\nPlease check city name.")
        else:
            self.label.config(text="Please enter a city name.")

if __name__ == "__main__":
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'  # Your API key here
    root = tk.Tk()
    app = WeatherApp(root, API_KEY)
    root.mainloop()
