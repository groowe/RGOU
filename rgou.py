#!/usr/bin/env python
# Royal Game of Ur

#Equipment

#The game of Royal game of Ur is played on an unusually shaped special board. To understand the shape of the board, first draw grid of 3 x 8 squares. Then, counting from the left, eliminate from the top and the bottom row, the 5th and 6th squares. You should be left with a block of 4 x 3 squares connected to a block of 2 x 3 squares by a bridge of 2 squares in the middle. Although boards with various patterns have been found, the only consistent factor has been that five of the squares on the board have rosettes inscribed in them and the consensus has been that these squares have a special significance. On the top and bottom rows, a rosette should appear in the second square from the right and the first square from the left. A fifth rosette should appear in the fourth square from the left in the middle row.

#The boards found at Ur have been accompanied by small round counters, each with five white dots on them, seven light and seven dark. Also found have been six pyramidal dice each with two dots on two of the four corners. These are simply binary lots - throw three dice and count the number that land with a spotted corner upwards giving a number from 0 to 3.
import tkinter as tk
import tkinter.font as font
from PIL import ImageTk,Image
import os

game = tk.Tk()
game.title("Royal game of Ur")
gf = tk.Frame(game,width=800,height=800)
#gf.rowconfigure(1,weight = 1)
#gf.columnconfigure(2,weight=1)
#gf.grid_propagate(0)
#gf.pack()

board_img = tk.PhotoImage(file='RGOU.gif')
scaled_board = board_img.subsample(2,2)

white_piece = tk.PhotoImage(file='white_piece.gif')

black_piece = tk.PhotoImage(file='black_piece.gif')

pieces = [white_piece,black_piece]

#panel = tk.Label(gf,image=scaled_board)
#panel.pack(side = "bottom",fill = "both", expand = "yes")

#white coords:
white_track = [[0,3],[0,2],[0,1],
        # common
        [0,0],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],
        [1,6],[1,7],
        # / common
        [0,7],[0,6]]
# black coords
black_track = [[2,3],[2,2],[2,1],
        # common
        [2,0],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],
        [1,6],[1,7],
        # /common
        [2,7],[2,6]]
board = [[None in range(3)] in range(8)]
#bt = tk.Button(gf, text = 'Click Me !', image = white_piece).pack(side = "top")
#def mf():
#    global wf
f = tk.Frame(gf,width=100,height=100)
f.rowconfigure(0,weight=1)
f.columnconfigure(0,weight=1)
f.grid_propagate(0)
b = tk.Button(f,text="ads"
        #,image = white_piece
        )
def showboard():
    global board
    for y in range(3):
        for x in range(8):
            if ((x == 0 or x == 2) and (y == 4 or y == 5)):
                if board[x][y] == None:
                    f = tk.Frame(gf)
                    f.rowconfigure(0,weight=1)
                    f.columnconfigure(0,weight=1)
                    f.grid_propagate(0)
                    b = tk.Button(f,text=""
                            #,image = white_piece)
                            ).pack(side='top')
                    board[x][y] == f,b
#                continue
#showboard()


game.mainloop()




