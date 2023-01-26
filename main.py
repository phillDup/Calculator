# Imports
import tkinter as tk
from tkinter import *

import clsEquation


# Main GUI OOP
class AppGui(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Window
        self.geometry('513x500')
        self.title('Calculator')

        # Equation Object
        self.equation = clsEquation.Equation()

    # Function automatically creates number buttons
    def create_num_buttons(self):

        row = 1
        col = 0
        for btn_num in range(0, 10):

            if btn_num == 0:
                btn = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(btn_num), command= lambda : self.equation.add_num(0))
                btn.grid(column=1, row=4)
            else:

                btn = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(btn_num),  command= lambda : self.equation.add_num(3))
                btn.grid(column=col, row=row)

                if btn_num % 3 == 0:
                    col = 0
                    row += 1
                else:
                    col += 1

    # Function to add other widgets
    def create_widgets(self):
        # Insert --> Equation
        edt_main = tk.Entry(self, width=28, bd=3, font=('Arial', 24))
        edt_main.grid(column=0, row=0, columnspan=3, sticky=tk.N)

        btn_plus = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('+'))
        btn_plus.grid(column=0, row=5)
        btn_minus = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('-'))
        btn_minus.grid(column=1, row=5)
        btn_mult = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('X'))
        btn_mult.grid(column=2, row=5)


if __name__ == "__main__":
    Gui = AppGui()
    Gui.create_num_buttons()
    Gui.create_widgets()

    Gui.mainloop()
