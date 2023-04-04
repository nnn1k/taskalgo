'''
(1,2,3)+,(4,5,6)+,(7,8,9)+,(1,4,7)+,(2,5,8)+,(3,6,9)+,(1,5,9)+,(3,5,7)+
1 2 3
4 5 6
7 8 9
'''

class TikTacToe:

    def __init__(self):
        self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

    def place_crosses(self, x, y):
        if self.board[x - 1][y - 1] not in ('X', 'O'):
            self.board[x - 1][y - 1] = 'X'
            return 1
        else:
            return 0

    def place_noughts(self, x, y):
        if self.board[x - 1][y - 1] not in ('X', 'O'):
            self.board[x - 1][y - 1] = 'O'
            return 1
        else:
            return 0

    def X_or_O(self, place):
        if place == 'X':
            return 1
        elif place == 'O':
            return 0

    def get_winner(self):
        for i in range(3):
            # по строке
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '*':
                print(self.board[i][0], 'win')
                return self.X_or_O(self.board[i][0])
            # по столбику
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '*':
                print(self.board[0][i], 'win')
                return self.X_or_O(self.board[0][i])
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '*':
            print(self.board[0][0], 'win')
            return self.X_or_O(self.board[0][0])
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[0][2] != '*':
            print(self.board[2][0], 'win')
            return self.X_or_O(self.board[2][0])

    def new_board(self):
        self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def test_1():
    game = TikTacToe()
    assert game.place_crosses(1, 3) == 1
    assert game.place_crosses(1, 3) == 0


t = TikTacToe()
print(t.get_winner())

