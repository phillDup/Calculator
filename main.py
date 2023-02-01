# Imports
import tkinter as tk
from tkinter import ttk

import clsEquation


# Classes
# Widgets with window as container
class GUI(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Other attributes
        self.buttons = []

        # Objects
        self.equation = clsEquation.Equation()
        self.container = container

        # Styles
        self.Style = ttk.Style(container)
        self.Style.configure('TButton', font=('Arial', 18))
        self.Style.configure('TEntry', font=('Arial', 20))

        # Main Input
        self.main_edt = ttk.Entry(container, width=28, font=('Arial', 24))
        self.main_edt.grid(column=0, row=0, sticky=tk.N, columnspan=3)
        self.equation.get_main_edt(self.main_edt)

    # GUI elements here
    # Number buttons
    def create_buttons(self):
        row = 1
        col = 1
        for btn_num in range(0, 10):
            new_button = ttk.Button(self.container, width=11, text=str(btn_num))
            new_button.grid(row=row, column=col)
            self.buttons.append(new_button)
            if btn_num % 3 == 0:
                row += 1
                col = 0
            else:
                col += 1

        self.buttons[0]['command'] = lambda: self.equation.add_to_equation(0)
        self.buttons[1]['command'] = lambda: self.equation.add_to_equation(1)
        self.buttons[2]['command'] = lambda: self.equation.add_to_equation(2)
        self.buttons[3]['command'] = lambda: self.equation.add_to_equation(3)
        self.buttons[4]['command'] = lambda: self.equation.add_to_equation(4)
        self.buttons[5]['command'] = lambda: self.equation.add_to_equation(5)
        self.buttons[6]['command'] = lambda: self.equation.add_to_equation(6)
        self.buttons[7]['command'] = lambda: self.equation.add_to_equation(7)
        self.buttons[8]['command'] = lambda: self.equation.add_to_equation(8)
        self.buttons[9]['command'] = lambda: self.equation.add_to_equation(9)

        # Operator buttons
        btn_plus = ttk.Button(self.container, width=22, text='+', command=lambda: self.equation.add_to_equation('+'))
        btn_plus.grid(row=5, column=0, columnspan=3)
        btn_minus = ttk.Button(self.container, width=22, text='-', command=lambda: self.equation.add_to_equation('-'))
        btn_minus.grid(row=6, column=0, columnspan=3)
        btn_mult = ttk.Button(self.container, width=22, text='x', command=lambda: self.equation.add_to_equation('*'))
        btn_mult.grid(row=7, column=0, columnspan=3)
        btn_div = ttk.Button(self.container, width=22, text='÷', command=lambda: self.equation.add_to_equation('/'))
        btn_div.grid(row=8, column=0, columnspan=3)

        btn_equals = ttk.Button(self.container, width=22, text='=', command=lambda: self.equation.solve_equation())
        btn_equals.grid(row=9, column=0, columnspan=3)

        btn_clear = ttk.Button(self.container, width=22, text='Clear', command=lambda : self.equation.clear_equation())
        btn_clear.grid(row=10, column=0, columnspan=3)

    # Bindings
    def bindings(self):
        for i in range(0, 9):
            self.container.bind(str(i), self.equation.add_via_entry)

        self.container.bind('+', self.equation.add_via_entry)
        self.container.bind('-', self.equation.add_via_entry)
        self.container.bind('*', self.equation.add_via_entry)
        self.container.bind('/', self.equation.add_via_entry)
        self.container.bind('=', self.equation.add_via_entry)


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
    App_Gui.create_buttons()
    App_Gui.bindings()
    App.mainloop()
