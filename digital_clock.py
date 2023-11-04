from tkinter import Tk, Label, Frame
from datetime import datetime

def display_info():
    today = datetime.now()
    time = today.strftime('%I:%M:%S %p')
    time_label.config(text=time)
    time_label.after(1000, display_info)
    today_name = today.strftime('%A')
    day_label.config(text=today_name)
    today_date = today.strftime('%d %B %Y')
    date_label.config(text=today_date)

root = Tk()
root.title('Digital Clock')
root.geometry('300x200')
clock_frame = Frame(root)
clock_frame.place(relx=0.5, rely=0.5, anchor='center')
time_label = Label(clock_frame, font=('calibri', 40, 'bold'), 
                   background='black', 
                   foreground='green')
time_label.pack()
day_label = Label(clock_frame, font=('calibri', 12,))
day_label.pack()
date_label = Label(clock_frame, font=('calibri', 12))
date_label.pack()
display_info()
root.mainloop()