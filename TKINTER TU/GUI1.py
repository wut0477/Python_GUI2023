from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('ระบบฐานข้อมูลการผลิต')
#GUI.resizable(False, False)
#GUI.minsize(min_width, min_height)
#GUI.maxsize(min_height, max_height)
#GUI.attributes('-alpha',0.5)
GUI.attributes('-topmost', 1)

#GUI.lift(another_window)
#GUI.lower(another_window)
GUI.iconbitmap('gear.ico')



window_width = 1000
window_height = 900


screen_width = GUI.winfo_screenwidth()
screen_height = GUI.winfo_screenheight()


center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)




GUI.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


label = ttk.Label(GUI)
label.config(text='Hi, there')
label.pack()


GUI.mainloop()

"""
Summary
Use the title() method to change the title of the window.
Use the geometry() method to change the size and location of the window.
Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
Use the window.attributes('-alpha',0.5) to set the transparency for the window.
Use the window.attributes('-topmost', 1) to make the window always on top.
Use lift() and lower() methods to move the window up and down of the window stacking order.
Use the iconbitmap() method to change the default icon of the window.
"""