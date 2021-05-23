from array import *

class players:
    def __init__(self, playerOne: str, playerTwo: str):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.printPlayers()

    def printPlayers(self):
        print(f'{self.playerOne} and {self.playerTwo}')

class board:
    def __init__(self, obj: players, board: array):
        self.obj = obj
        self.board = board
        self.play1 = True

    def printMatrix(self):
        for i in range(9):
            if i % 3 == 0:
                print()
            print(f'{self.board[i]}', end=" ")
        print()
    
    def updateBoard(self, x: bool, val: str):
        board = self.board

        if x:
            board[int(val) - 1] = "X"
            self.printMatrix()
        else:
            board[int(val) - 1] = "O"   
            self.printMatrix()
    
    def checkForDraw(self):
        board = self.board

        for i in range(9):
            if board[i] == '_':
                return False

        return True


    def checkForWin(self):
        board = self.board

        if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
            return True
        if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
            return True
        if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            return True
        if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            return True

        for i in range(3):
            if board[0+i] == 'X' and board[3+i] =='X' and board[6+i]== 'X':
                return True
            elif board[0+i] == 'X' and board[1+i] == 'X' and board[3+i] == 'X':
                return True
            elif board[0+i] == 'O' and board[3+i] =='O' and board[6+i]== 'O':
                return True
            elif board[0+i] == 'O' and board[1+i] == 'O' and board[3+i] == 'O':
                return True
        
        return False
        

