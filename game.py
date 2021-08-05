import numpy as np

x = "X"
o = "O"


class game():
    def __init__(self):
        self.board = np.full((3, 3), "-")
        self.player = x
        self.winConunter = 3
        print(self.board)

    def clearTheBoard(self):
        self.board = np.full((3, 3), "-")

    def play(self, row, column):
        print("win ", self.checkForWin())

        if self.isAnySpaceInBoard():

            if self.isAvailable(row, column):
                self.board[row][column] = self.player
                if self.player == x:
                    self.player = o
                else:
                    self.player = x
            else:
                # wrong place print a warning for user
                print("Please choose an empty place")
        else:
            # game ended in drawn
            print("Drawn")
        self.printTheBoard()

    def isAvailable(self, row, column):
        return self.board[row][column] == "-"

    def printTheBoard(self):
        print("\n****************\n\n", self.board)

    def isAnySpaceInBoard(self):
        return "-" in self.board

    def checkForWinHorizontal(self):
        win = False
        for row in self.board:
            if win:
                return win

            a = row[0]
            if a == "-":
                continue
            for i in row:
                if not (a == i):
                    win = False
                    break
                else:
                    win = True
        return win

    def checkForWinVertical(self):
        # checking win condition for column
        for i in range(len(self.board)):
            counter = 0
            a = self.board[0][i]
            for column in range(len(self.board)):
                if a == self.board[column][i] and a != "-":
                    counter = counter + 1
                else:
                    counter = 0
            if counter == self.winConunter:
                return True

        return False

    def checkForWin(self):
        return self.checkForWinHorizontal()


g = game()
print(g.checkForWinVertical())
g.play(0, 0)
g.play(0, 1)
g.play(1, 0)
g.play(1, 1)
g.play(2, 0)
print("---------------")
print(g.checkForWinVertical())
