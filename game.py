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

        if self.isAnySpaceInBoard():

            if self.isAvailable(row, column):
                self.board[row][column] = self.player

                if self.checkForWin():
                    self.printTheBoard()
                    print(self.player, " Win the game !!")

                    return "win"

                else:
                    print("Player Changed")
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
            return "draw"

        self.printTheBoard()


    def isAvailable(self, row, column):
        return self.board[row][column] == "-"

    def printTheBoard(self):
        print("\n\n****Tic Tac Toe*****")
        print(self.board)

    def isAnySpaceInBoard(self):
        return "-" in self.board

    def checkForWinHorizontal(self):
        # checking win conditioun for row
        for row in self.board:
            a = row[0]
            counter = 0

            for i in range(len(row)):
                if a == row[i] and a != "-":
                    counter = 1 + counter
                else:
                    a = row[i]
                    counter = 0
                if counter == self.winConunter:
                    return True

        return False

    def checkForWinVertical(self):
        # checking win condition for column
        for i in range(len(self.board)):
            counter = 0
            a = self.board[0][i]
            for column in range(len(self.board)):
                if a == self.board[column][i] and a != "-":
                    counter = counter + 1
                else:
                    a = self.board[column][i]
                    counter = 0

                if counter == self.winConunter:
                    return True

        return False

    def checkForWinDiagonal(self):
        # first part of diagonal

        a = self.board[0][0]
        counter = 0
        for i in range(len(self.board)):

            if a == self.board[i][i] and a != "-":
                counter = counter + 1
            else:
                a = self.board[i][i]
                counter = 0
            if counter == self.winConunter:
                return True

        # second part of diagonal
        a = self.board[0][len(self.board[0]) - 1]
        counter = 0
        j = 0
        for i in reversed(range(len(self.board))):

            if a == self.board[j][i] and a != "-":
                counter = counter + 1
            else:
                a = self.board[j][i]
                counter = 0
            if counter == self.winConunter:
                return True
            j = j+1
        return False

    def checkForWin(self):
        return self.checkForWinHorizontal() or self.checkForWinVertical() or self.checkForWinDiagonal()

    def player(self):
        return self.player

    def restart(self):
        self.board = np.full((3, 3), "-")
        self.player = x
        print(self.board)


