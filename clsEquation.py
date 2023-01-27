import tkinter
from main import AppGui


class Equation:
    def __init__(self):
        self.equation = []

    def add_num(self, num):
        # Add to list
        self.equation.append(num)
        print(self.equation)
        self.add_to_edt(AppGui.return_main_edt())

    def return_list_len(self):
        return len(self.equation)

    def add_to_edt(self, entry=tkinter.Entry):
        entry.delete(first=0, last=len(self.equation))
        for char in self.equation:
            entry.insert(self.equation.index(char) - 1, char)