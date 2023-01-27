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
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(1), command=lambda: self.equation.add_num(1))
        btn1.grid(column=0, row=1)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(2), command=lambda: self.equation.add_num(2))
        btn1.grid(column=1, row=1)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(3), command=lambda: self.equation.add_num(3))
        btn1.grid(column=2, row=1)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(4), command=lambda: self.equation.add_num(4))
        btn1.grid(column=0, row=2)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(5), command=lambda: self.equation.add_num(5))
        btn1.grid(column=1, row=2)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(6), command=lambda: self.equation.add_num(6))
        btn1.grid(column=2, row=2)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(7), command=lambda: self.equation.add_num(7))
        btn1.grid(column=0, row=3)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(8), command=lambda: self.equation.add_num(8))
        btn1.grid(column=1, row=3)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(9), command=lambda: self.equation.add_num(9))
        btn1.grid(column=2, row=3)
        btn1 = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str(0), command=lambda: self.equation.add_num(0))
        btn1.grid(column=1, row=4)

    # Function to add other widgets
    def create_widgets(self):

        # Global objects
        global btn_plus, btn_minus, btn_mult, edt_main

        # Insert --> Equation
        edt_main = tk.Entry(self, width=28, bd=3, font=('Arial', 24))
        edt_main.grid(column=0, row=0, columnspan=3, sticky=tk.N)

        btn_plus = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('+'),
                             command=lambda: self.equation.add_num('+'))
        btn_plus.grid(column=0, row=5)
        btn_minus = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('-'),
                              command=lambda: self.equation.add_num('-'))
        btn_minus.grid(column=1, row=5)
        btn_mult = tk.Button(self, width=8, bd=3, font=('Arial', 24), text=str('X'),
                             command=lambda: self.equation.add_num('*'))
        btn_mult.grid(column=2, row=5)

    @staticmethod
    def return_main_edt():
        return edt_main

    @staticmethod
    def disable_button(*args):
        for btn in args:
            btn["state"] = DISABLED

    @staticmethod
    def enable_button(*args):
        for btn in args:
            btn["state"] = NORMAL


if __name__ == "__main__":
    # Instantiate
    Gui = AppGui()
    Gui.create_num_buttons()
    Gui.create_widgets()

    # Run time Substitutes for GUI.mainloop()
    while True:

        if Gui.equation.return_list_len() < 1:
            Gui.disable_button(btn_plus, btn_minus, btn_mult)
        else:
            Gui.enable_button(btn_plus, btn_minus, btn_mult)

        Gui.update_idletasks()
        Gui.update()


