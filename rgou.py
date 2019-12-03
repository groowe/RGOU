#!/usr/bin/env python
# Royal Game of Ur

#Equipment

#The game of Royal game of Ur is played on an unusually shaped special board. To understand the shape of the board, f>

#The boards found at Ur have been accompanied by small round counters, each with five white dots on them, seven light>



import tkinter as tk
import random
from tkinter.messagebox import showinfo

game = tk.Tk()
game.title("RGOU")
gf = tk.Frame(game,width=800,height=800)
### background : TBD
#rgou = tk.PhotoImage(file='RGOU.gif')
#rgou = rgou.subsample(2,2)
#rgou_label = tk.Label(gf,image=rgou)
#rgou_label.place(x=-73,y=50,relwidth=1,relheight=1)
#######
#f = tk.Frame(gf,width=100,height=100)
#f.columnconfigure(0,weight=1)
#f.rowconfigure(0,weight=1)
#f.grid_propagate(0)

gf.pack()
#white_piece = tk.PhotoImage(file='white_piece.gif')
#white_piece = white_piece.subsample(2,2)
board_butts =[[None for i in range(3)] for i in range(9)] # one line more for buttons
#board_butts.append([None]) # for extra button(s)
white_pieces_coords = [[4,0] for i in range(7)]
black_pieces_coords = [[4,2] for i in range(7)]
pieces_coords = [white_pieces_coords,None,black_pieces_coords]
white_track = [[4,0],[3,0],[2,0],[1,0],[0,0],
        [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
        [7,0],[6,0]]
black_track = [[4,2],[3,2],[2,2],[1,2],[0,2],
        [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
        [7,2],[6,2]]
common_track = [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
tracks = [white_track,None,black_track]

# some variables:
rolled = False
rolled_num = 0 # number rolled
turn = 0 # 0 = white 2= black
moved = True # did we move after roll ?
def rollicon(y): # needed only 0 or 2
    s = ""

    if turn == y:
        if not rolled:
            s+="roll"
        else:
            s+= str(rolled_num)

        if not moved:
            s+="-active"
    else:
        if rolled_num == 0:
            s = "0"
        else:
            s+="wait"
    print(f"turn: {turn},rolled_num {rolled_num},moved {moved}")
    return s

def checkroll():
# rolls
    butts(5,0)
    butts(5,2)
# starting position
    butts(4,0)
    butts(4,2)

# coords of icons:
def picbutton(x,y):
    name = ""
    wheel_icons = [[0,0],[0,2],[3,1],[6,0],[6,2]]
    bars_icons = [[0,1]]
    wave_icons = [[1,0],[1,2],[3,0],[3,2],[6,1]]
    dots_icons = [[1,1],[2,0],[2,2],[4,1],[7,1]]
    otherone_icons = [[2,1],[5,1]]
    cuby_icons = [[7,0],[7,2]]
    rolling_icons = [[5,0],[5,2]]
    coords = [x,y]
    if coords in wheel_icons:
        name+="wheel"
    elif coords in bars_icons:
        name+="bars"
    elif coords in dots_icons:
        name+="dots"
    elif coords in otherone_icons:
        name+="otherone"
    elif coords in cuby_icons:
        name+="cuby"
    elif coords in wave_icons:
        name+="waves"
    if coords in white_pieces_coords:
        name+="-white"
    elif coords in black_pieces_coords:

        name+="-black"

    if coords in rolling_icons:
        name = rollicon(y)

    if coords == [4,0] or coords == [4,2]:
        if len(pieces_coords[y]) == 0:
            name = "-empty-"
    if name:
        name+=".gif"
    else:
        pic= tk.PhotoImage(file="-empty-.gif")
        pic = pic.subsample(2,2)
        return pic

#    print(name)
    pic= tk.PhotoImage(file=name)
    pic = pic.subsample(2,2)
    return pic


def roll():
    global rolled_num
    global moved , rolled
#    rolled_num = 0

    # check if game did not ended already
    if not pieces_coords[0]:

        game_ended(0)
        return
    elif not pieces_coords[2]:

        game_ended(2)

        return

    if moved == False or rolled == True:
        return
    i = 0
    for a in range(4):
        i += random.randint(0,1)
#    print(i)
    rolled_num = i
    moved = False
    if i == 0:
        moved = True
    rolled = True
    checkroll()
    print(f"rolled_num {rolled_num}")
    return i

def game_ended(turn):
    if turn == 0:
        s = "white"
        opp = 2
    else:
        s = "black"
        opp = 0
    t = s + f" won  7 : {7 - len(pieces_coords[opp])}"
    showinfo("Window",t)

def reset():
    global white_pieces_coords,black_pieces_coords,pieces_coords
    global rolled, rolled_num , turn, moved

    a = tk.messagebox.askokcancel("popup","reset?")
    if a:
        white_pieces_coords = [[4,0] for i in range(7)]
        black_pieces_coords = [[4,2] for i in range(7)]
        pieces_coords = [white_pieces_coords,None,black_pieces_coords]
        rolled = False
        rolled_num = 0 # number rolled
        turn = 0 # 0 = white 2= black
        moved = True # did we move after roll ?
#        checkroll()
        for x in range(8):
            for y in range(3):
                butts(x,y)

        score()
#        checkroll()


def play(x,y):
    global white_pieces_coords
    global black_pieces_coords
    global pieces_coords , board_butts
    global rolled_num , turn ,moved , rolled

    checkroll()
    print(f"{x},{y} pressed\nturn {turn}\nrolled_num {rolled_num}")
#    rolled_num = 0

   # if rollbutton,roll
    if x == 5 and y == turn:
        if moved:
            roll()
#        print(f"rolled_num {rolled_num}")
        if rolled_num == 0:
            if turn == 0:
                turn = 2
            else:
                turn = 0
            moved = True
            rolled = False
            checkroll()
            return
        checkroll()
        return
    # elif moving pieces
    elif [x,y] in pieces_coords[turn] and not moved:
        if turn == 0:
            opponent = 2
        else:
            opponent = 0
        # manipulate exact piece
        pieceindex = pieces_coords[turn].index([x,y])
        # position on table
        tableindex = tracks[turn].index([x,y])

        # work only with valid rolls
        if rolled_num == 0:
            return
        # if roll goes over, ignore
        if rolled_num + tableindex > len(tracks[turn]):
            return
        # if roll is exact, remove piece
        if rolled_num + tableindex == len(tracks[turn]):
            del pieces_coords[turn][pieceindex]
            print(f"pieces_coords[turn] == {pieces_coords[turn]}")
            print(f"{pieces_coords[turn] == True}")

            print(f"{pieces_coords[turn] == False}")
            # update score
            score()
            if not pieces_coords[turn]:
                game_ended(turn)
            butts(x,y)
            turn = opponent
            rolled = False
            moved = True
            checkroll()
            return
        newx,newy = tracks[turn][rolled_num+tableindex]
        # special case
        if [newx,newy] == [3,1] : # can't take piece there
            if [newx,newy] in pieces_coords[opponent]: # go one step further
                newx+=1
        if [newx,newy] in pieces_coords[turn]: # can't take own piece
            return
        pieces_coords[turn][pieceindex] = [newx,newy]
        if [newx,newy] in pieces_coords[opponent]:
            oppindex = pieces_coords[opponent].index([newx,newy])
            pieces_coords[opponent][oppindex] = [4,opponent]
        playagain =[ [0,0] , [0,2] , [3,1] ,[6,0] , [6,2] ] # "play again" squares
        if [newx,newy] in playagain:
            moved = True
            rolled = False
            s = turn
            roll()
            if rolled_num != 0:
#            moved = True
                turn = s
        else:
            moved = True
            rolled = False
            turn = opponent
        butts(x,y)
#        checkroll()
        butts(newx,newy)
        checkroll()
        return

    return
def moves():
    global turn
    global moved
    if turn == 0:
        turn = 2
    else :
        turn = 0
    moved = True

def is_move_possible():
    a = pieces_coords[turn] # all pieces of player who's move it is
    road = tracks[turn]
    if turn == 0:
        opponent = 2
    else:
        opponent = 0
    for piece in a:
        # where is the piece
        piece_position = road.index(piece)
        if rolled_num + piece_position <= len(road):
            newcoords = road[piece_position+rolled_num]
            if newcoords == [3,1]:
                if newcoords in pieces_coords[opponent]:
                    newcoords = [4,1]
            if newcoords not in a:
                return True
    return False




def printbuts():
    for a in pieces_coords:
        print(a)

def butts(x,y):
#    print(f"butts {x}{y}")
    global board_butts
    f,b,p = board_butts[x][y]
    p = picbutton(x,y)
    b["image"] = p
    try:
        board_butts[x][y] = f,b,p
    except IndexError:
        print(f"{x}{y}")
        print(f"board_butts = {board_butts}")
        raise IndexError

def board():
    for x in range(8):
        for y in range(3):
#            if (x == 4 or x == 5) and (y != 1):
#                continue
            if board_butts[x][y] == None:
                f = tk.Frame(gf,width=60,height=60)
                f.rowconfigure(0,weight=1)
                f.columnconfigure(0,weight=1)
                f.grid_propagate(0)
                f.grid(row=x,column=y)
#                b = tk.Button(f,picture=picture)
                picture = picbutton(x,y)
                b= ""
#                print(b)
                if picture:
                    b = tk.Button(f,image=picture)
    
                else:
                    b = tk.Button(f,text="roll")
                b["command"] = lambda *args,a=x,c=y: play(a,c)

                b.pack()
#                print(f"{x}{y}")
                board_butts[x][y] = f,b,picture
    # button for forfeit move
    f = tk.Frame(gf,width = 120,height=60)
    f.rowconfigure(0,weight=1)
    f.columnconfigure(0,weight=1)
    f.grid_propagate(0)
    f.grid(row=8,column=0)
    b = tk.Button(f,text="forfeit move",command = forfeit)
    b.pack()
    board_butts[8][0] = f,b
    # button for reset
    f = tk.Frame(gf,width = 120,height=60)
    f.rowconfigure(0,weight=1)
    f.columnconfigure(0,weight=1)
    f.grid_propagate(0)
    f.grid(row=8,column=2)
    b = tk.Button(f,text="reset",command = reset)
    b.pack()
    board_butts[8][2] = f,b
    # score button
    score()


def score():
    w = str(7 - len(pieces_coords[0]))
    b = str(7 - len(pieces_coords[2]))
    string = f"score\n{w} : {b}"

    global board_butts
    if board_butts[8][1] == None:
        # score :
        f = tk.Frame(gf,width = 120,height= 60)
        f.rowconfigure(0,weight = 1)
        f.columnconfigure(0,weight=1)
        f.grid_propagate(0)
        f.grid(row=8,column=1)
        b = tk.Button(f,text=string)
        b.pack()
        board_butts[8][1] = f,b
    else:
        f,b = board_butts[8][1]
        b["text"] = string
        board_butts[8][1] =f, b


def forfeit():
    global moved,rolled , turn
    if not rolled:

        tk.messagebox.askokcancel("popup","ROLL!")
        return
    if pieces_coords[0] == 0:
        finished(0)
        return
    if pieces_coords[2] == 0:
        finished(2)
        return

    if rolled and is_move_possible():


        tk.messagebox.askokcancel("popup","you can move!")
        return
    moved = True
    rolled = False
    if turn == 0:
        turn = 2
    else:
        turn = 0
    
    checkroll()

board()
game.mainloop()

