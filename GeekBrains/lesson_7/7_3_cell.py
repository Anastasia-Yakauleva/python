class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.quantity * "*"}'

    def __add__(self, other):
        print("Sum of cells is: ")
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        print("Subtraction of cells is: ")
        return Cell(self.quantity - other.quantity) if self.quantity - other.quantity > 0 \
                    else 'less than zero!'

    def __mul__(self, other):
        print("Multiply of cells is: ")
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        print("True division of cells is: ")
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        print("order of cells is: ")
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cell_1 = Cell(25)
cell_2 = Cell(5)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2 * cell_1)
print(cell_2.make_order(5))
print(cell_1.make_order(10))
print(cell_1 / cell_2)
