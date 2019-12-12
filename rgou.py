#!/usr/bin/env python
# Royal Game of Ur
try:
    # python2
    import Tkinter as tk
    from Tkinter.messagebox import showinfo
except ImportError:
    # python3
    import tkinter as tk
    from tkinter.messagebox import showinfo
import random # for rolls

def callback(event):
    print("clicked at", event.x, event.y)

    coords(event.x,event.y)
#    coordss(event.x,event.y)



#frame = Frame(game, width=100, height=100)


#game.mainloop()

game = tk.Tk()
game.title("Royal Game of Ur")
## BG image
#fname = "RGOU.gif"
#fname = "RGOU2.gif"
fname = "RGOU4.gif"
bg_image = tk.PhotoImage(file=fname)
bg_image = bg_image.subsample(2,2)
w = bg_image.width()
h = bg_image.height()
strs = "%dx%d+50+30" % (w,h)
print(strs)
game.geometry(strs)
cv = tk.Canvas(width=w,height=h)
cv.pack(side='top',fill='both',expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')
cv.bind("<Button-1>", callback)
cv.pack()
print(dir(cv))
board_x_y = [ # x ,y ,xn,yn,[xycoordinates]
        [100,80,180,152,[0,0]],
        [100,170,180,231,[1,0]],

        [100,245,180,315,[2,0]],
        [100,325,180,394,[3,0]],
        [20,332,69,386,[4,0]], # white start

        [60,443,142,517,[5,0]], # roll white
        [100,578,180,635,[6,0]],
        [100,650,180,719,[7,0]],


#    w = cv.create_image(100,480,image=whiterollicon)
#        [270,489,338,560,[5,2]], # roll black
#        [287,428,338,560,[5,2]], # roll black
#    b = cv.create_image(330,480,image=blackrollicon)

        [189,80,257,152,[0,1]],
        [189,170,257,231,[1,1]],
        [189,239,257,315,[2,1]],
        [189,325,257,394,[3,1]],
        [189,403,257,478,[4,1]],
        [189,489,257,560,[5,1]],
        [189,578,257,635,[6,1]],
        [189,650,257,719,[7,1]],

        [270,80,338,152,[0,2]],
        [270,170,338,231,[1,2]],
        [270,245,338,315,[2,2]],
        [270,325,338,394,[3,2]],
        [365,319,445,396,[4,2]], # black start
        [293,446,368,517,[5,2]], # roll black
        [270,578,338,635,[6,2]],
        [270,650,338,719,[7,2]]

        ]

def setup():
    global white_pieces, black_pieces
    global pieces
    global white_track, black_track
    global tracks
    global turn , rolled_num, moved , rolled
    rolled = False 
    moved = True # did we move after roll?
    turn = 0 # 0 = white , 2 = black
    rolled_num = 0 # number rolled
    white_pieces = [[4,0] for i in range(7)] # score white
    black_pieces = [[4,2] for i in range(7)]
    pieces =  [white_pieces,None,black_pieces]
    white_track = [[4,0],[3,0],[2,0],[1,0],[0,0],
                   [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
                   [7,0],[6,0]]
    black_track = [[4,2],[3,2],[2,2],[1,2],[0,2],
                   [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],
               [7,2],[6,2]]
    # common_track = [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    tracks = [white_track,None,black_track]
    def_cv_pieces()
    # roll icons
    checkroll()
    score()
    # forfeit "button"
    t = cv.create_text(90,770,text="forfeit move",font="Times 20 bold")
    r = cv.create_text(350,770,text="reset",font="Times 20 bold")

rollicons = []

def rollicon(y): # 0 white , 2 black
    s = ""
    if turn == 2:
        dd = "-black"
    else:
        dd = "-white"
    if turn == y:
        s+=dd
        if not rolled:
            s+="roll"
        else:
            s+= str(rolled_num)
#        if not moved:
#            s+="-active"
    else:
        if rolled_num == 0:
            s = "0"
        else:
            s="wait"
    s+=".gif"
    pc = tk.PhotoImage(file=s)
    pc = pc.subsample(2,2)
    return pc

def checkroll():
    # 5,0 and 5,2 coords
    global rollicons
    global w ,b
    global cv
    global whiterollicon,blackrollicon
    whiterollicon = rollicon(0)
    blackrollicon = rollicon(2)
    if len(rollicons) == 3:
        cv.delete(rollicons[0])
        cv.delete(rollicons[2])
#        w = rollicons[0]
#        b = rollicons[2]
#        cv[w]["image"] = whiterollicon
#        cv[b]["image"] = blackrollicon
        print(f"rollicons = {rollicons}")
#        cv.delete(w)
#        cv.delete(b)
#        tk.Canvas.itemconfig(w,100,493,image=whiterollicon)

#        tk.Canvas.itemconfig(b,270,489,image=blackrollicon)
#        cv.itemcomfigure(w,image = whiterollicon)
#        cv.itemconfigure(b,image = blackrollicon)
#    if len(rollicons) == 0:
        # white
#        [100,493,152,526,[5,0]], # roll white
#        [73,433,152,526,[5,0]], # roll white
    w = cv.create_image(100,480,image=whiterollicon)
#        [270,489,338,560,[5,2]], # roll black
#        [287,428,338,560,[5,2]], # roll black
    b = cv.create_image(330,480,image=blackrollicon)

#        print(cv.itemconfig(b))        
    rollicons = [w,None,b]

    
def def_cv_pieces(delete=False):
    global whitepic , blackpic
    global cv
    global white_cv
    global black_cv
    global pieces_cv
    if delete:
        for i in white_cv:
            cv.delete(i)
#
        for i in black_cv:
            cv.delete(i)
        return

    white_cv= []
    black_cv = []
    pieces_cv = []
    whitepic = tk.PhotoImage(file="-white.gif")
    whitepic = whitepic.subsample(2,2)
    blackpic = tk.PhotoImage(file="-black.gif")
    blackpic = blackpic.subsample(2,2)
    ## check if there are no more cv objects
    t = cv.create_image(-100,-100,image=whitepic)
#    for i in range(2,t+1):
#        cv.delete(i)
    for i in white_pieces:
        x,y = i[0],i[1]
        for c in board_x_y:
            if c[4] == [x,y]:
                xx = int((c[2] + c[0]) /2)
                yy = int((c[3] + c[1]) / 2)
                s = cv.create_image(xx, yy, image=whitepic) 
                white_cv.append(s)
                print("white")

    for i in black_pieces:
        x,y = i[0],i[1]
        for c in board_x_y:
            if c[-1] == [x,y]:
                xx = int((c[2] + c[0]) /2)
                yy = int((c[3] + c[1]) / 2)
                s = cv.create_image(xx, yy, image=blackpic) 
                black_cv.append(s)
                print("black")
    pieces_cv = [white_cv,None,black_cv]
    print(pieces_cv)

def roll():
    score()
    global rolled_num
    global moved,rolled
    # check if game did not ended already
    for i in range(0,3,2):
        if not pieces[i]:
            game_ended(i)
            return
    if moved == False or rolled == True:
        return
    i = 0
    for a in range(4):
        i+= random.randint(0,1)
    rolled_num = i
    moved = False
    rolled = True
    checkroll()

def game_ended(turn):
    if turn == 0:
        s = "white"
        opp = 2
    else:
        s = "black"
        opp = 0
    t = f"{s} won 7 : {7 - len(pieces[opp])}"
    showinfo("Window",t)


def reset():
    a = tk.messagebox.askokcancel("popup","reset?")
    if a:

        def_cv_pieces(True)
        setup()
#        score()

def endmove(playagain = False): # True == one more move
    global turn,rolled,moved
    if turn == 0:
        opponent = 2
    else:
        opponent = 0
    if not playagain:
        turn = opponent
    rolled = False
    moved = True
    if playagain:
        s = roll()
        if s == 0:
            endmove()
    checkroll()

def coords(x,y):
    if 16 < x < 164:
        if 753 < y < 776:
            forfeit()
            return
    if 315 < x < 390:
        if 757 < y < 779:
            reset()
            return
    for item in board_x_y:
        if item[0] <= x <= item[2]:
            if item[1] <= y <= item[3]:
                print(item[4])
                play(item[4])
#                movec(item[4])
                return


def getpossition(x,y):
    for i in board_x_y:
        if i[4] == [x,y]:
            return i[0],i[1]

def play(coords):
#    global white_pieces
#    global black_pieces
#    global pieces, board_butts
    global rolled_num , turn, moved, rolled
    global tracks
    global pieces_cv
    global pieces
    print(f"rolled_num = {rolled_num}")
    print(f"turn = {turn}")
    print(f"moved = {moved}")
    print(f"rolled = {rolled}")
    print(pieces)
    checkroll()
    x = coords[0]
    y = coords[1]
    # if rollbutton ,rull
    if x == 5 and y == turn:
        if moved:
            roll()
        if rolled_num ==0:
            if turn == 0:
                turn = 2
            else:
                turn = 0
            moved = True
            rolled = False
            checkroll()

            return

    if coords in pieces[turn] and not moved:
        if turn == 0:
            opponent = 2
        else:
            opponent = 0
        trackindex = tracks[turn].index(coords) # position on board
        print(f"trackindex = {trackindex}")
        indpiece = pieces[turn].index(coords) # identify piece
        print(f"indpiece = {indpiece}")
        t = pieces_cv[turn][indpiece] # identify canvas of piece
        print(f"t = {t}")
        result = trackindex + rolled_num
        print(result)
        if len(tracks[turn]) < result:
            return
        if len(tracks[turn]) == result:
            pieces[turn].pop(indpiece)
            pieces_cv[turn].pop(indpiece)
            cv.delete(t)
            score()
            if len(pieces[turn]) == 0:
                game_ended(turn)
            endmove()

            # next turn
            return
        coords_new = tracks[turn][trackindex+rolled_num]
        newx = coords_new[0]
        newy = coords_new[1]
        print(f"coords_new = {coords_new}")
        # special case
        if [newx,newy] == [3,1] : # can't take piece there
            if [newx,newy] in pieces[opponent]:
                newx+=1
        if [newx,newy] in pieces[turn]: # can't take own piece
            return
        newcoordx,newcoordy = getpossition(newx,newy)
        if [newx,newy] in pieces[opponent]: # take
            oppindex = pieces[opponent].index([newx,newy])
            oppx,oppy = getpossition(4,opponent)
            difopx = oppx - newcoordx
            difopy = oppy - newcoordy
            taken = pieces_cv[opponent][oppindex]
            cv.move(taken,difopx,difopy) # move to start
            pieces[opponent][oppindex] = [4,opponent] # set coords


        print(f"{newcoordx},{newcoordy}")
        oldx,oldy = getpossition(x,y)
        difx = newcoordx - oldx
        dify = newcoordy - oldy

        cv.move(t,difx,dify)
        pieces[turn][indpiece] = [newx,newy]
        print("move!!")
        print(f"{t},{difx},{dify}")
        print(f"{pieces[turn][indpiece]}")
        print(f"{pieces[turn]}")
        # play again squares
        playagain = [ [0,0] , [0,2] , [3,1], [6,0] ,[6,2]]
        play =( [newx,newy] in playagain )
        endmove(play)
        return

def is_move_possible():
    a = pieces[turn] # all pieces of player on move
    road = tracks[turn]
    if turn == 0:
        opponent = 2
    else:
        opponent = 0
    alreadychecked = []
    for piece in a:
        if piece in alreadychecked:
            continue
        piece_position = road.index(piece)
        if rolled_num + piece_position <= len(road):
            newcoords = road[piece_position+rolled_num]
            if newcoords == [3,1] : # special square check
                if newcoords in pieces_coords[opponent]:
                    newcoords = [4,1]
            if newcoords not in a:
                return True
        alreadychecked.append(piece)
    return False

def forfeit():
    global moved,rolled,turn
    # check if game did not ended already
    for i in range(0,3,2):
        if not pieces[i]:
            game_ended(i)
            return
    if not rolled:
        tk.messagebox.askokcancel("popup","ROLL!")
        return

    if rolled and is_move_possible():
        tk.messagebox.askokcancel("popup","you can move!")
        return
    endmove()


scoretext = []
def score():
    global scoretext
    w = str(7 - len(pieces[0]))
    b = str(7 - len(pieces[2]))
    t = f"{w} : {b}"

    if len(scoretext) == 0:
        score = cv.create_text(220,780,font="Times 30 italic bold",text=t)
        scoretext.append(score)
    else:
        cv.itemconfig(scoretext[0],font="Times 30 italic bold",text=t)

    # show canvas text :p
    return

# RUN!

setup()
game.mainloop()
