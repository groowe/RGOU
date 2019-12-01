from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
#img = ImageTk.PhotoImage(Image.open("RGOU.gif"))
img = PhotoImage(file='RGOU.gif')
smaller_image = img.subsample(2, 2) 
panel = Label(root, image = smaller_image)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
