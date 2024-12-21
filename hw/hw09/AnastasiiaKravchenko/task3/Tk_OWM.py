import tkinter as tk
from tkinter import font
from OWM import mgr


def get_weather(loc, result_var):
    observation = mgr.weather_at_place(loc)
    w = observation.weather
    result = f"{w.detailed_status}\n" \
             f"{w.wind()}\n" \
             f"{w.humidity}\n" \
             f"{w.temperature('celsius')}\n" \
             f"{w.rain}\n" \
             f"{w.heat_index}\n" \
             f"{w.clouds}"
    result_var.set(result)


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get(), result_var))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

result_var = tk.StringVar()
result_var.set('')

label = tk.Label(lower_frame, font=('Courier', 14), textvariable=result_var, anchor=tk.CENTER)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

