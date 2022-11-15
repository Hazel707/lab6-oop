# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, other_player, make_move, check_move, get_winner, isfull
from logic import show_board
from game import Game
"""def show_board(board): #display board
    output_board=[
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    for row in range(3):
        for col in range(3):
            if board[row][col]==None:
                output_board[row][col]=" " #make printed board looks more pretty
            else:
                output_board[row][col]=board[row][col]

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(output_board[0][0], output_board[0][1], output_board[0][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(output_board[1][0], output_board[1][1],output_board[1][2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(output_board[2][0], output_board[2][1], output_board[2][2]))
    print("\t     |     |")
    print("\n")"""
 


if __name__ == '__main__':
    ans=input("Do you want to play against the bot?(y or n): ").lower()
    if ans=='y':
        game=Game()
        game.run()
    else:
        board = make_empty_board()
        winner = None
        turn=0 
        now=1 #Represents the current player that should be operating
        show_board(board)
        player1=input("Player 1 choose which one you want to be, X or O?").upper()
        while (player1 !="X" and player1!="O"):
            player1=input(("Please choose X or O"))
        player2=other_player(player1)
        print("So player 2 you are letter "+player2)
        print("Player 1, you go first")
        row=int(input("pick a row: "))
        while (row<0 or row>2):
            row=int(input("out of boundary, please pick a numer(0<= x <3): "))

        col=int(input("pick a col: "))
        while (col<0 or col>2):
            col=int(input("out of boundary, please pick a numer(0<= y <3): "))
        board=make_move(board,player1,player2,now,row,col)
        turn+=1
        show_board(board)

        while winner == None: #make a turn
            if turn%2==0:
                now=1
            else:
                now=2
            print("TODO: take a turn!")
            # TODO: Input a move from the player.
            if now==1:
                print("Player 1 is your turn!")
            else:
                print("Player 2 is your turn!")

            row=int(input("pick a row: "))
            while (row<0 or row>2):
                row=int(input("out of boundary, please pick a numer(0<= x <3): "))

            col=int(input("pick a col: "))
            while (col<0 or col>2):
                col=int(input("out of boundary, please pick a numer(0<= y <3): "))

            while check_move(board,row,col): #keep input until input move is vailed
                print("this position was taken, please choose a new one")
                row=int(input("pick a row: "))
                while (row<0 or row>2):
                    row=int(input("out of boundary, please pick a numer(0<= x <3): "))

                col=int(input("pick a col: "))
                while (col<0 or col>2):
                    col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                
            # TODO: Update the board.
            board=make_move(board,player1,player2,now,row,col)

            # TODO: Show the board to the user.
            show_board(board)

            winner=get_winner(board)
            
            if winner==player1:
                print("Congratulation! Player 1 is winner!")
            elif winner==player2:
                print("Congratulation! Player 2 is winner!")
            else:
                if isfull(board):
                    print("The grid is full, draw!")
                    winner="Draw"
                #break

            # TODO: Update who's turn it is.
            turn+=1


        
     