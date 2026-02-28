print('This is tictac toe')

class Board:
    def __init__(self):
        self.cells = [" "]*9

    def display(self):
        b=self.cells
        print()
        print(f" {b[0]} | {b[1]} | {b[2]}")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]}")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]}")

    def place(self, position: int, mark: str):
        if not 1 <= position <= 9:
            raise ValueError("Position must be between 1 and 9.")
        i = position - 1
        if self.cells[i] != " ":
            return False
        self.cells[i] = mark
        return True
    


class Player:
    def __init__(self, name: str, mark: str):
        self.mark = mark
        self.name = input(f"Player Selecting {mark}, enter your name: ") 

class Game:
    def __int__(self):
        self.board = Board()
        self.p1 = Player("X")
        self.p2 = Player("O")
        self.current_player_index = self.p1

p1 = Player("Alice", "X")
p2 = Player("Bob", "O")
        
# b1 =Board()
# b1.cells = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# b1.display()

# guide = Board()
# guide.cells = [str(i) for i in range(1,10)]
# guide.display()


b2 = Board()
b2.place(5,"O")
b2.display()