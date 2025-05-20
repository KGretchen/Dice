class Player:
    """
    Represents a player in the Tic-Tac-Toe game.
    """
    def __init__(self, name, symbol):
        """
        Initialize a new Player instance.
        """
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        """
        Return a string representation of the Player object.
        """
        return f"Player(name='{self.name}', symbol='{self.symbol}')"


class Board:
    """
    Represents the Tic-Tac-Toe game board.

    The board is a 2D grid of cells, where each cell can be either empty or occupied by a
    player's symbol.
    """
    def __init__(self, size=3):
        """
        Initialize a new Board instance.
        """
        self.size = size
        self._cells = [[" "] * size for _ in range(size)]
        setattr(self, 'move_count', 0)

    def print_board(self):
        """
        Print the current state of the game board.
        """
        for row in self._cells:
            print("|" + "|".join(row) + "|")

    def is_cell_empty(self, row, col):
        """
        Print whether the current cell is empty.
        """
        return self._cells[row][col] == " "

    def set_cell(self, row, col, symbol):
        """
        Set the value of a cell on the board.
        """
        if not self.is_cell_empty(row, col):
            raise ValueError("Cell is already occupied")
        self._cells[row][col] = symbol
        self.move_count += 1

    def check_winner(self):
        """
        Check if there is a winner on the board.

        The function checks for a row, column, or diagonal with three matching symbols.
        """
        for i in range(self.size):
            if self._cells[i][0] == self._cells[i][1] == self._cells[i][2] != " ":
                return self._cells[i][0]
            if self._cells[0][i] == self._cells[1][i] == self._cells[2][i] != " ":
                return self._cells[0][i]
        if self._cells[0][0] == self._cells[1][1] == self._cells[2][2] != " ":
            return self._cells[0][0]
        if self._cells[0][2] == self._cells[1][1] == self._cells[2][0] != " ":
            return self._cells[0][2]
        return None

    def is_full(self):
        """
        Check if there is no empty cells on the board.
        """
        return all(" " not in row for row in self._cells)


class Game:
    """
    Represents a Tic-Tac-Toe game.

    The Game class manages the game flow, including switching between players, handling user
    input, and determining the game's outcome.
    """
    def __init__(self, player1, player2):
        """
        Initialize a new Game instance.
        """
        self.board = Board()
        self.players = [player1, player2]
        self.current = 0

    def switch_player(self):
        """
        Switch to the next player's turn.
        """
        self.current = 1 - self.current

    def play_turn(self):
        """
        Execute a single turn of the game.
        """
        player = self.players[self.current]
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                    raise ValueError("Invalid input")
                self.board.set_cell(row, col, player.symbol)
                break
            except ValueError as error:
                print(f"Invalid input: {error}")
        self.board.print_board()
        print(f"Move count: {self.board.move_count}")

    def play(self):
        """
        Run the game until the winner is determined.
        """
        while True:
            self.play_turn()
            winner = self.board.check_winner()
            if winner:
                print(f"{winner} wins!")
                break
            if self.board.is_full():
                print("It's a draw!")
                break
            self.switch_player()

    def __getattr__(self, name):
        return f"Attribute '{name}' not found"


if __name__ == "__main__":
    p1 = Player("Alice", "X")
    p2 = Player("Bob", "O")
    game = Game(p1, p2)
    game.play()
