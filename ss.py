from tkinter import *
#from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue", height=800, width=450)
filename = PhotoImage(file = "RGOU.gif")
scaled = filename.subsample(2,2)
background_label = Label(top, image=scaled)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop()
