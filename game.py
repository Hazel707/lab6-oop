
import random
from logic import get_winner, check_move, isfull, make_empty_board, show_board
from typing import Tuple


"""class Board:
    def __init__(self):
        self.rows=[
        [None, None, None],
        [None, None, None],
        [None, None, None],
        ]
    def __str__(self) :
        s='-------\n'
        for row in self.rows:
            for cell in row:
                s=s+'|'
                if cell==None:
                    s=s+' '
                else:
                    s=s+cell
            s=s+'|\n-------\n'
        return s
    def get(self,x,y):
        return self.rows[x][y]

    def set(self,x,y,value):
        self.rows[x][y]=value"""

      

class Game:
    def __init__(self) :
        self.board=make_empty_board()
        #self._playerx=playerx
        #self._playero=playero
        self.winner=None #get_winner(self._board)
        self.user_turn=True
        

    def get_board(self):
        return self.board

    def set_move(self,x,y,value):
        self.board[x][y]=value

    
    def _get_empty_space(self):
        space = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    space.append((i, j))

        return space

    def bot_random_step(self) -> Tuple:
        _empty_space = self._get_empty_space()

        return _empty_space[random.randint(0, len(_empty_space) - 1)]


    def run(self):
        show_board(self.board)
        while self.winner is None:
            if self.user_turn:
                
                print("It's your turn!")
                row=int(input("pick a row: "))
                while (row<0 or row>2):
                    row=int(input("out of boundary, please pick a numer(0<= x <3): "))
                col=int(input("pick a col: "))
                while (col<0 or col>2):
                    col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                
                while check_move(self.board,row,col): #keep input until input move is vailed
                    print("this position was taken, please choose a new one")
                    row=int(input("pick a row: "))
                    while (row<0 or row>2):
                        row=int(input("out of boundary, please pick a numer(0<= x <3): "))

                    col=int(input("pick a col: "))
                    while (col<0 or col>2):
                        col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                self.set_move(row,col,"X")
                #print(self._board)
                #self.winner=get_winner(self._board)

                
                
            else:
                print("It's bot's turn!")
                bot_step = self.bot_random_step()

                print("Bot takes " + str(bot_step))

                self.board[bot_step[0]][bot_step[1]] = "O"

                #make_move(self._board,current_player)

            show_board(self.board)
            self.winner=get_winner(self.board)
            
            if self.winner=="X":
                print("Congratulation! Yor're winner!")
            elif self.winner=="O":
                print("You failed")
            else:
                if isfull(self.board):
                    print("The grid is full, draw!")
                    self.winner="Draw"

            self.user_turn=not self.user_turn

"""class Human:
    def get_move(self,x,y,board):
        return parse_move(input())

class Bot:
    def get_move(self,board):
        return some_available_square(board)"""


"""game=Game()
game.run"""

"""b=Board()
b.set(1,1,'X')
b.set(2,1,'O')
print(b)"""