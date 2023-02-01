# Imports
import tkinter
from tkinter import *


# Class
class Equation:
    def __init__(self):
        self.equation = []
        # Local copy made for displaying
        self.equation_copy = []
        self.main_edt = tkinter.Entry
        self.num_string = ''
        self.operands = {'+': '+', '-': '-', '*': 'x', '/': '÷'}

    def add_to_equation(self, char):
        self.equation_copy.append(char)

        if char in ['+', '-', '/', '*', '=']:
            self.equation.append(self.num_string)
            self.equation.append(char)
            self.num_string = ''
        else:
            self.num_string = self.num_string + str(char)

        # print(self.equation)
        # print(self.num_string)

        # add to edit
        self.main_edt.delete(0, len(self.equation_copy))
        for char in self.equation_copy:
            if char in ['+', '-', '/', '*']:
                char = self.operands[char]
            self.main_edt.insert(len(self.equation_copy) - 1, char)

    def solve_equation(self):
        # Ensure final letter is added to list
        self.equation.append(self.num_string)
        print(self.equation)

        # Calculate answer
        answer = int(self.equation[0])
        for char in self.equation:
            if char == '+':
                answer = answer + int(self.equation[self.equation.index(char) + 1])
                print((self.equation[self.equation.index(char) + 1]))
            elif char == '-':
                answer = answer - int(self.equation[self.equation.index(char) + 1])
            elif char == '*':
                answer = answer * int(self.equation[self.equation.index(char) + 1])
            elif char == '/':
                answer = answer / float((self.equation[self.equation.index(char) + 1]))

        self.main_edt.delete(0, len(self.main_edt.get()))
        self.main_edt.insert(0, answer)
        print(answer)

    def clear_equation(self):
        self.equation = []
        self.num_string = ''
        self.equation_copy = []
        self.main_edt.delete(0, len(self.main_edt.get()))

    def remove_from_equation(self):

        if len(self.num_string) > 0:
            # Remove from string and equation copy (output)
            self.num_string = self.num_string[:-1]
            self.equation_copy.pop(len(self.equation_copy) - 1)

        elif len(self.num_string) == 0:
            # Get string from equation and remove (make current string)
            self.num_string = self.equation[len(self.equation) - 1]
            self.equation.pop(len(self.equation) - 1)

            # Remove from string and equation copy (output)
            self.num_string = self.num_string[:-1]
            self.equation_copy.pop(len(self.equation_copy) - 1)

        # Add to edit
        self.main_edt.delete(0, len(self.equation_copy) + 1)
        for char in self.equation_copy:
            if char in ['+', '-', '/', '*']:
                char = self.operands[char]
            self.main_edt.insert(len(self.equation_copy) - 1, char)

    def get_main_edt(self, edt: tkinter.Entry):
        self.main_edt = edt

    def add_via_entry(self, char):
        print(char)
        # Check if equation should be solved
        if char.char == '=':
            self.solve_equation()
        # Check for backspace
        elif char.keycode == 8:
            self.remove_from_equation()
        else:
            self.add_to_equation(char.char)


