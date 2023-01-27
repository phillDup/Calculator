class Equation:
    def __init__(self):
        self.equation = []

    def add_num(self, num):
        self.equation.append(num)
        print(self.equation)

    def return_list_len(self):
        return len(self.equation)