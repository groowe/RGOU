try:
    # python2
    import Tkinter as tk
except ImportError:
    # python3
    import tkinter as tk

root = tk.Tk()
root.title("try")
## BG image
fname = "RGOU.gif"
bg_image = tk.PhotoImage(file=fname)
bg_image = bg_image.subsample(2,2)
w = bg_image.width()
h = bg_image.height()
strs = "%dx%d+50+30" % (w,h)
print(strs)
root.geometry(strs)
cv = tk.Canvas(width=w,height=h)
cv.pack(side='top',fill='both',expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')
#cv.create_rectangle(100,70,w-95,h-70)
## // BG image
#f = tk.Frame(cv)
#f.rowconfigure(0,weight=1)
#f.columnconfigure(0,weight=1)
#f.grid_propagate(0)
#f.grid(row=2,column=5)
pic = tk.PhotoImage(file="waves-white.gif")
pic = pic.subsample(2,2)
wg = pic.width()
hg = pic.height()
print(f"{wg}/{hg}")
#b = tk.Button(cv,image=pic)
#b.place(relx=100,rely=300,anchor="center")
#b.pack(padx=0,pady=0)
cv.create_image(104+int(wg/2), 155+int(wg/2), image=pic) 
#cv.bind("<KeyPress-Down>",lambda e: root.destroy)
#cv.addtag_enclosed(b, 100, 100, 150, 150)

# RUN!
root.mainloop()
