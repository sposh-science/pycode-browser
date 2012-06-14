from Tkinter import *

recs = []    # List keeping track of the rectangles

def remove(event):
   global recs
   if len(recs) > 0:
      c.delete(recs[0]) # delete from Canvas
      recs.pop(0)       # delete first item from list

def draw(event):
   r = c.create_rectangle(event.x, event.y, event.x+5, event.y+5)
   recs.append(r)

w = Tk()
c = Canvas(w, width = 300, height = 200)
c.pack()
c.bind("<Button-1>", draw)
c.bind("<Button-3>", remove)
w.mainloop() 

