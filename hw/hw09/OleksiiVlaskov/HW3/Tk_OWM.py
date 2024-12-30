import tkinter as tk
from tkinter import font
from OWM import weather, API_KEY

def get_weather():
    field=entry_field.get()
    try:
        w=weather(API_KEY=API_KEY, City=field)
        label.config(text=w)
    except Exception as e:
        label.config(text=f'Error: {e}')
    

HEIGHT = 500
WIDTH = 900


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.75, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14), text='Queries the OWM Weather API\nfor the currently observed weather at the specified toponym \n(eg: \"London,uk\")', anchor='w', justify='left', wraplength=900*0.9)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

