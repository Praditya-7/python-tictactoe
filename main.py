print('This is tictac toe')

class Board:
    def __init__(self):
        self.board = ['']*9

    def display(self):
        b=self.cells
        print()
        print(f" {b[0]} | {b[1]} | {b[2]}  ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]}  ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")

b1 =Board()
b1.cells = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
b1.display()

guide = Board()
guide.cells = [str(i) for i in range(1,10)]
guide.display()
