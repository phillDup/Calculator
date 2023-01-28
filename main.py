# Imports
import tkinter as tk
from tkinter import ttk


# Classes
# Widgets with window as container
class GUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # GUI elements here

        # Styles
        self.Style = ttk.Style(container)
        self.Style.configure('TButton', font=('Arial', 18))
        self.Style.configure('TEntry', font=('Arial', 20))

        # Main Input
        self.main_edt = ttk.Entry(container, width=28, font=('Arial', 24))
        self.main_edt.grid(column=0, row=0, sticky=tk.N, columnspan=3)

        # Number buttons
        row = 1
        col = 1
        self.buttons = []
        for btn_num in range(0, 10):
            new_button = ttk.Button(container, width=11, text=str(btn_num))
            new_button.grid(row=row, column=col)
            self.buttons.append(new_button)
            if btn_num % 3 == 0:
                row += 1
                col = 0
            else:
                col += 1


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
