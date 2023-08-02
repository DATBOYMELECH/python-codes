from tkinter import *
from time import strftime
window = Tk()
window.title('Melech Digital Clock Project')  
def clock():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, clock)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)
label = Label(window, font=('Arial', 120, 'bold'),
            background='black',
            foreground='blue')
label.pack(anchor='center')
day_label = Label(window, font=("Ink Free", 25),
 fg="#FFFF00", bg="black")
day_label.pack()

date_label = Label(window, font=("ink free", 30), fg="#FFFF00",bg="black")
date_label.pack()
clock()

mainloop()
