from tkinter import *
from tkinter import ttk

def return_pressed(event):
    print('Return key pressed')

def log(event):
    print(event)


GUI = Tk()

btn = ttk.Button(GUI, text='Save')
btn.bind('<Return>', return_pressed)
btn.bind('<Return>',log, add='+')


btn.focus()
btn.pack(expand=True)

GUI.mainloop()