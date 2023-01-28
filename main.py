# Imports
import tkinter as tk
from tkinter import ttk


# Classes
# Widgets with window as container
class GUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # GUI elements here
        # Main Input
        self.main_edt = ttk.Entry(container, font=('Arial', 25), width=28)
        self.main_edt.grid(column=0, row=0, sticky=tk.N)


# Tkinter window
class APP(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry("500x500")


# Instances
if __name__ == "__main__":
    App = APP()
    App_Gui = GUI(App)
    App.mainloop()
