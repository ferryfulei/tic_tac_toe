import time
class tic_tac_toe_ttt:
    def __init__ (self, board):
        self.chess_board = [board[i : i + 3] for i in range(0,len(board), 3)]
        self.move = []
    def inspect_if_over(self):
        sum_board_horizon = [0, 0, 0]
        sum_board_vertical = [0, 0, 0]
        for i in (0, 1, 2):
            sum_board_horizon[i] = self.chess_board[i][0] + self.chess_board[i][1] + self.chess_board[i][2]
            sum_board_vertical[i] = self.chess_board[0][i] + self.chess_board[1][i] + self.chess_board[2][i]
        sum_board_slash = self.chess_board[0][0] + self.chess_board[1][1] + self.chess_board[2][2]  # \
        sum_board_backslash = self.chess_board[0][2] + self.chess_board[1][1] + self.chess_board[2][0]  # /
        for ii in (0, 1, 2):
            if sum_board_horizon[ii] == 3 or sum_board_vertical[ii] == 3 \
                    or sum_board_slash == 3 or sum_board_backslash == 3:
                return 1  # USER WIN
            if sum_board_horizon[ii] == -3 or sum_board_vertical[ii] == -3 \
                    or sum_board_slash == -3 or sum_board_backslash == -3:
                return -1  # COM WIN
        for iii in (0, 1, 2):
            for j in (0, 1, 2):
                if self.chess_board[iii][j] == 0:
                    return 100
        return 0

    def put_the_chessman(self, coordinate, player):
        self.chess_board[coordinate[0]][coordinate[1]] = player
        self.move = coordinate
    def inspect_if_is_danger(self,player):
        sum_board_horizon = [0, 0, 0]
        sum_board_vertical = [0, 0, 0]
        for i in (0, 1, 2):
            sum_board_horizon[i] = self.chess_board[i][0] + self.chess_board[i][1] + self.chess_board[i][2]
            sum_board_vertical[i] = self.chess_board[0][i] + self.chess_board[1][i] + self.chess_board[2][i]
        sum_board_slash = self.chess_board[0][0] + self.chess_board[1][1] + self.chess_board[2][2]
        sum_board_backslash = self.chess_board[0][2] + self.chess_board[1][1] + self.chess_board[2][0]
        for i in (0, 1, 2):
            if sum_board_horizon[i] == player:
                for j in (0, 1, 2):
                    if self.chess_board[i][j] == 0:
                        return [i, j]
            if sum_board_vertical[i] == player:
                for j in (0, 1, 2):
                    if self.chess_board[j][i] == 0:
                        return [j, i]
        if sum_board_slash == player:
            for i in (0, 1, 2):
                if self.chess_board[i][i] == 0:
                    return [i, i]
        if sum_board_backslash == player:
            for i in (0, 1, 2):
                if self.chess_board[i][2 - i] == 0:
                    return [i, 2 - i]
        return 0
    def moveChess(self):
        danger_output = self.inspect_if_is_danger(-2)
        if danger_output == 0:
            danger_output2 = self.inspect_if_is_danger(2)
            if danger_output2 != 0:
                self.put_the_chessman(danger_output2, -1)
            elif self.chess_board[1][1] == 0:
                self.put_the_chessman([1, 1], -1)
            elif self.chess_board[0][0] == 0:
                self.put_the_chessman([0, 0], -1)
            elif self.chess_board[0][2] == 0:
                self.put_the_chessman([0, 2], -1)
            elif self.chess_board[2][0] == 0:
                self.put_the_chessman([2, 0], -1)
            elif self.chess_board[2][2] == 0:
                self.put_the_chessman([2, 2], -1)
            else:
                for i in (0, 1, 2):
                    for j in (0, 1, 2):
                        if self.chess_board[i][j] == 0:
                            self.put_the_chessman([i, j], -1)
        else:
            self.put_the_chessman(danger_output, -1)

class tic_tac_toe_lei :

    def __init__(self, board ,player = "x"):
        self._squares = ["." if i == 0 else i for i in board]
        self._winningCombos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
        ]

    def createBoard(self):
        for i in (0,9):
            self._squares[i] = "."
        self.showBoard()

    def showBoard(self) :
        print(self._squares[0], self._squares[1], self._squares[2])
        print(self._squares[3], self._squares[4], self._squares[5])
        print(self._squares[6], self._squares[7], self._squares[8])

    def getAvailableMoves(self):
        availableMoves = []
        for i in range(9):
            if self._squares[i] == ".":
                availableMoves.append(i)
        return availableMoves

    def makeMove(self, position,player):
        self._squares[position] = player
        self.showBoard

    def complete(self):
        if "." not in self._squares:
            return True
        if self.getWinner() != None:
            return True
        return False

    def getWinner(self):
        for player in ("x", "o"):
            for combos in self._winningCombos:
                if self._squares[combos[0]] == player and self._squares[combos[1]] == player and self._squares[combos[2]] == player:
                    return player
            if "." not in self._squares:
                return "tie"
            return None

    def getEnemyPlayer(self, player):
        return "o" if  player == "x" else "x"

    def minimax(self, player, depth = 4):
        if player == "o":
            best = -10
        else:
            best = 10
        if self.complete():
            if self.getWinner() == "x":
                return -10 + depth, None
            elif self.getWinner() == "tie":
                return 0, None
            elif self.getWinner() == "o":
                return 10 - depth, None
        for move in self.getAvailableMoves():
            self.makeMove(move, player)
            val, _ = self.minimax(self.getEnemyPlayer(player), depth + 1)
            self.makeMove(move,".")
            if player == "o":
                if val > best:
                    best, bestMove = val, move
            else:
                if val < best:
                    best, bestMove = val, move
        return best, bestMove

class competition_board:
    def __init__(self):
        self._tttboard = [0,0,0,0,0,0,0,0,0]
        self._leiboard = [0,0,0,0,0,0,0,0,0]
    def ttt_move(self):
        ttt = tic_tac_toe_ttt(self._tttboard)
        ttt.moveChess()
        move = ttt.move[0] * 3 + ttt.move[1]
        self._tttboard[move] = -1
        self._leiboard[move] = "x"
    def lei_move(self):
        lei = tic_tac_toe_lei(self._leiboard)
        best, bestmove = lei.minimax("o")
        self._tttboard[bestmove] = 1
        self._leiboard[bestmove] = "o"
    def printBoard(self):
        board = [" " if i == 0 else i for i in self._leiboard]
        for i in range(len(board)):
            print("|{}|\t".format(board[i]), end = " ")
            if (i+1) % 3 == 0:
                print()
        print()
    def game(self,tttfirst):
        while(0 in self._leiboard):
            print("ttt's turn")  if tttfirst else print("lei's turn")
            self.ttt_move() if tttfirst else self.lei_move()
            self.printBoard()
            tttfirst = False if tttfirst else True
            time.sleep(1)
        print("DRAW")
    def demo(self):
        print("Round 1 ttt first")
        self.game(True)
        self._tttboard = [0,0,0,0,0,0,0,0,0]
        self._leiboard = [0,0,0,0,0,0,0,0,0]
        print("Round 2 lei first")
        self.game(False)
competition_board().demo()
