# Imports
import tkinter
from tkinter import  *


# Class
class Equation:
    def __init__(self):
        self.equation = []
        # Local copy made for displaying
        self.equation_copy = []
        self.num_string = ''

    def add_to_equation(self, char, edt: tkinter.Entry):
        self.equation_copy.append(char)

        if char in ['+', '-', '/', '*']:
            self.equation.append(self.num_string)
            self.equation.append(char)
            self.num_string = ''
        else:
            self.num_string = self.num_string + str(char)

        print(self.equation)
        print(self.num_string)

        # add to edit
        edt.delete(0, len(self.equation_copy))
        for char in self.equation_copy:
            edt.insert(len(self.equation_copy) - 1, char)

    def solve_equation(self):
        # Ensure final letter is added to lsit
        self.equation.append(self.num_string)

        # Calculate answer
        answer = ''
