print('This is tictac toe')

class Board:
    def __init__(self):
        self.board = ['']*9

    def display(self):
        print("   |   |   ")
        print("---+---+---")
        print("   |   |   ")
        print("---+---+---")
        print("   |   |   ")

b1 =Board()
b1.display()