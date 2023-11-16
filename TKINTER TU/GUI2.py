from tkinter import *
from tkinter import ttk


GUI = Tk()
GUI.geometry('500x300')

def button_clicked():
    print('Button clicked')


def select(option):
    print(option)

button = ttk.Button(GUI, text='Click Me', command=button_clicked)
button.pack()

ttk.Button(GUI, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(GUI, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(GUI, text='Scissors', command=lambda: select('Scissors')).pack()


GUI.mainloop()