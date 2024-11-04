import sys

class Board:
    def __init__(self, size, board):
        self.size = size
        self.board = board
        
    def row_reverse(self):
        for i in range(self.size):
            self.board[i].reverse()
            
    def col_reverse(self):
        new_board = []
        for i in range(self.size):
            cur = []
            for j in range(size):
                cur.append(self.board[j][i])
            new_board.append(cur)
        self.board = new_board
    
    def transform(self, move, back=False):
        if move == 1:
            self.col_reverse()
        elif move == 2:
            self.row_reverse()
        elif move == 3 and not back:
            self.col_reverse()
            self.row_reverse()
        elif move == 3 and back:
            self.row_reverse()
            self.col_reverse()

    def make_move(self, move):
        self.transform(move)
        new_board = []
        for i in range(self.size):
            cur_row = []
            cur = -1
            counter = 0
            while counter < self.size:
                if self.board[i][counter] == 0:
                    counter += 1
                elif cur == -1:
                    cur = self.board[i][counter]
                    counter += 1
                elif self.board[i][counter] == cur:
                    cur_row.append(2 * self.board[i][counter])
                    cur = -1
                    counter += 1
                else:
                    cur_row.append(cur)
                    cur = self.board[i][counter]
                    counter += 1
            if cur != -1:
                cur_row.append(cur)
            fill_zeroes = len(cur_row)
            while fill_zeroes < size:
                cur_row.append(0)
                fill_zeroes += 1
            new_board.append(cur_row)
        self.board = new_board
        self.transform(move, back=True)
    
    def __str__(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                string += str(self.board[i][j]) + " "
            string += "\n"
        return string

if __name__ == "__main__":
    input = sys.stdin.readline
    size = 4
    board = []
    for i in range(size):
        board.append(list(map(int, input().split())))
    
    game_board = Board(size, board)
    game_board.make_move(int(input()))
    print(game_board)