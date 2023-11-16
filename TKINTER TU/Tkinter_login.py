from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Sign in')
GUI.geometry('300x150')
GUI.resizable(False, False)


email = StringVar()
password = StringVar()

def login_clicked():
    """
        Callback when the login button clicked
    """

    msg = f'You entered email: {email.get()} and password:{password.get()}'

    messagebox.showinfo(
        title='Information',
        message=msg
    )

signin  = ttk.Frame(GUI)
signin.pack(padx=10, pady=10, fill='x', expand=True)

#email
email_label = ttk.Label(signin, text='Email Address:')
email_label.pack(fill='x',expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x',expand=True)
email_entry.focus()

GUI.mainloop()