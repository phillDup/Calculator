# Imports
import tkinter as tk
from tkinter import ttk

import clsEquation


# Classes
# Widgets with window as container
class GUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Objects
        self.equation = clsEquation.Equation()

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

        self.buttons[0]['command'] = lambda: self.equation.add_to_equation(0, self.main_edt)
        self.buttons[1]['command'] = lambda: self.equation.add_to_equation(1, self.main_edt)
        self.buttons[2]['command'] = lambda: self.equation.add_to_equation(2, self.main_edt)
        self.buttons[3]['command'] = lambda: self.equation.add_to_equation(3, self.main_edt)
        self.buttons[4]['command'] = lambda: self.equation.add_to_equation(4, self.main_edt)
        self.buttons[5]['command'] = lambda: self.equation.add_to_equation(5, self.main_edt)
        self.buttons[6]['command'] = lambda: self.equation.add_to_equation(6, self.main_edt)
        self.buttons[7]['command'] = lambda: self.equation.add_to_equation(7, self.main_edt)
        self.buttons[8]['command'] = lambda: self.equation.add_to_equation(8, self.main_edt)
        self.buttons[9]['command'] = lambda: self.equation.add_to_equation(9, self.main_edt)

        # Operator buttons
        btn_plus = ttk.Button(container, width=22, text='+', command=lambda: self.equation.add_to_equation('+', self.main_edt))
        btn_plus.grid(row=5, column=0, columnspan=3)
        btn_minus = ttk.Button(container, width=22, text='-', command=lambda: self.equation.add_to_equation('-', self.main_edt))
        btn_minus.grid(row=6, column=0, columnspan=3)
        btn_mult = ttk.Button(container, width=22, text='x', command=lambda: self.equation.add_to_equation('*', self.main_edt))
        btn_mult.grid(row=7, column=0, columnspan=3)
        btn_div = ttk.Button(container, width=22, text='÷', command=lambda: self.equation.add_to_equation('/', self.main_edt))
        btn_div.grid(row=8, column=0, columnspan=3)

        btn_equals = ttk.Button(container, width=22, text='=', command=lambda: self.equation.solve_equation(self.main_edt))
        btn_equals.grid(row=9, column=0, columnspan=3)
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
