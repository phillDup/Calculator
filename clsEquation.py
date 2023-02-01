# Imports
import tkinter
from tkinter import *


# Class
class Equation:
    def __init__(self):
        self.equation = []
        # Local copy made for displaying
        self.equation_copy = []
        self.num_string = ''
        self.operands = {'+': '+', '-': '-', '*': 'x', '/': '÷'}

    def add_to_equation(self, char, edt: tkinter.Entry):
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
        edt.delete(0, len(self.equation_copy))
        for char in self.equation_copy:
            if char in ['+', '-', '/', '*']:
                char = self.operands[char]
            edt.insert(len(self.equation_copy) - 1, char)

    def solve_equation(self, edt: tkinter.Entry):
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

        edt.delete(0, len(edt.get()))
        edt.insert(0, answer)
        print(answer)

    def clear_equation(self, edt: tkinter.Entry):
        self.equation = []
        self.num_string = ''
        self.equation_copy = []
        edt.delete(0, len(edt.get()))

    def add_via_entry(self, event):
        print(event)

