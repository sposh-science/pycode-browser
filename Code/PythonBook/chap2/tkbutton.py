from Tkinter import *

def hello():
    print 'hello world'                
    
w = Tk()   # Creates the main Graphics window
b = Button(w, text = 'Click Me', command = hello)
b.pack()
w.mainloop()