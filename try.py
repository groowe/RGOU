import tkinter as tk

game = tk.Tk()
game.title("RGOU")
rgou = tk.PhotoImage(file='RGOU.gif')
gf = tk.Frame(game,width=800,height=800)
#f = tk.Frame(gf,width=100,height=100)
#f.columnconfigure(0,weight=1)
#f.rowconfigure(0,weight=1)
#f.grid_propagate(0)

gf.pack()
white_piece = tk.PhotoImage(file='white_piece.gif')
white_piece = white_piece.subsample(2,2)
board_butts =[[None for i in range(3)] for i in range(8)]
white_pieces_coords = []
black_pieces_coords = []


# coords of icons:
def picbutton(x,y):
    name = ""
    wheel_icons = [[0,0],[0,2],[3,1],[6,0],[6,2]]

    bars_icons = [[0,1]]
    wave_icons = [[1,0],[1,2],[3,0],[3,2],[6,1]]
    dots_icons = [[1,1],[2,0],[2,2],[4,1],[7,1]]
    otherone_icons = [[2,1],[5,1]]
    cuby_icons = [[7,0],[7,2]]
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
    if coords in white_pieces_coords:
        name+="-white"
    elif coords in black_pieces_coords:
        name+="-black"
    if name:
        name+=".gif"
    else:
        return False
    
    pic= tk.PhotoImage(file=name)
    return pic






def board():
    for x in range(8):
        for y in range(3):
            if (x == 4 or x == 5) and (y != 1):
                continue

            f = tk.Frame(gf,width=60,height=60)
            f.rowconfigure(0,weight=1)
            f.columnconfigure(0,weight=1)
            f.grid_propagate(0)
            f.grid(row=x,column=y)
            b = tk.Button(f)

            b.pack()
            print(f"{x}{y}")
            board_butts[x][y] = f,b

board()
game.mainloop()

