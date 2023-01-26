# Imports
import tkinter as tk
from tkinter import *


# Main GUI OOP
class AppGui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Window
        self.geometry('513x500')
        self.title('Calculator')

        # Frame
        # self.frame = tk.Frame(self, bg='blue')

    def create_widgets(self):
        # Insert --> Equation
        edt_main = tk.Entry(self, width=28, bd=3, font=('Arial', 24))
        edt_main.grid(column=0, row=0, columnspan=3, sticky=tk.N)

        row = 1
        col = 0
        for btn_num in range(1, 10):
            btn = tk.Button(self, width=5, bd=3, font=('Arial', 24), text=str(btn_num))
            btn.grid(column=col, row=row)

            if btn_num % 3 == 0:
                col = 0
                row += 1
            else:
                col += 1


if __name__ == "__main__":
    Gui = AppGui()
    Gui.create_widgets()
    Gui.mainloop()
