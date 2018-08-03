class tic_tac_toe_lei :

    def __init__(self, player = "x"):
        self._squares = {}
        self_winningCombos = [
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
        self._availableMoves = []
        for i in (0,9):
            if self._squares[i] == ".":
                self_avaiableMoves.append(i)
        return self_avaiableMoves

    def makeMove(self, position,player):
        self._squares[position] = player
        self.showBoard

    def complete(self):
        if "." not in self._squares.values():
            return True
        if self.getWinner() != None:
            return True
        return False

    def getWinner(self):
        for player in ("x", "o"):
            for combos in self_winningCombos:
                if self._squares[combos[0]] == player and self._squares[combos[1]] == player and self._squares[combos[2]] == player:
                    return player
            if "." not in self._squares.values():
                return "tie"
            return None

    def getEnemyPlayer(self, player):
        return "o" if  player == "x" else "x"

    def minimax(self, player, depth = 0):
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
            val, _ = self.minimax(self.getEnemyPlayer(player), depth +1)
            self.makeMove(move,".")
            if player == "o":
                if val > best:
                    best, bestMove = val, move
            else:
                if val < best:
                    best, bestMove = val, move
            return best, bestMove
