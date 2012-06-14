from Tkinter import *

def draw(event):
   c.create_rectangle(event.x, event.y, event.x+5, event.y+5)

w = Tk()
c = Canvas(w, width = 300, height = 200)
c.pack()
c.bind("<Button-1>", draw)
w.mainloop() 
