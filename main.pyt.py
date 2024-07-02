class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def place_token(self, row, col, token):
        if 1 <= row <= self.size and 1 <= col <= self.size and self.board[row-1][col-1] is None:
            self.board[row-1][col-1] = token

    def is_game_over(self):
        return all(all(cell is not None for cell in row) for row in self.board) and any(self.check_win())

    def check_win(self):
        for row in self.board:
            if all(cell == True or cell == False for cell in row):
                return True
        for col in zip(*self.board):
            if all(cell == True or cell == False for cell in col):
                return True
        diag1 = all(self.board[i][i] for i in range(self.size))
        diag2 = all(self.board[i][self.size-1-i] for i in range(self.size))
        return diag1 or diag2

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))

game = TicTacToe()

while not game.is_game_over():
    try:
        coord = list(map(int, input().split()))
        token = input() == 'O'
        game.place_token(coord[0], coord[1], token)
        game.print_board()
        if game.check_win():
            print('Player O won!')
            break
    except ValueError:
        print('Invalid input.')