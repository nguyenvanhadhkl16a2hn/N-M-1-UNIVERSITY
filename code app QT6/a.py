from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("digital clock")
def clock():
    string = strftime("%H:%M:%S:%p")
    label.config(text = string)
    label.after(500,clock)
label = Label(root, font = ("Digital-7", 50), background = 'black', foreground='red')
label.pack(anchor='center')
clock()
root.mainloop()