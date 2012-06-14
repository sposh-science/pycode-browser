from Tkinter import *
from math import *

class disp:
    """
    Class for displaying items in a canvas using a world coordinate system. The range of the
    world coordinate system is specified by calling the setWorld method.
    """
    traces = []
       
    def __init__(self, parent, width=400., height=200.):
	self.parent = parent
	self.SCX = width 
	self.SCY = height
	self.border = 1
	self.canvas = Canvas(parent, width=width, height=height)
	self.canvas.pack(side = LEFT)
	self.setWorld(0 , 0, self.SCX, self.SCY)   # initialize scale factors 

    def setWorld(self, x1, y1, x2, y2):   #Calculates the scale factors 
	self.xmin = float(x1)
	self.ymin = float(y1)
	self.xmax = float(x2)
	self.ymax = float(y2)
	self.xscale = (self.xmax - self.xmin) / (self.SCX)
	self.yscale = (self.ymax - self.ymin) / (self.SCY)
      
    def w2s(self, p):	      # World to Screen xy conversion before plotting anything
	ip = []
	for xy in p:
		ix = self.border + int( (xy[0] - self.xmin) / self.xscale)
		iy = self.border + int( (xy[1] - self.ymin) / self.yscale)
		iy = self.SCY - iy
		ip.append((ix,iy))
	return ip

    def line(self, points, col='blue'):
       ip = self.w2s(points)
       t = self.canvas.create_line(ip, fill=col)
       self.traces.append(t)

    def delete_lines(self):
       for t in self.traces:
           self.canvas.delete(t)
       self.traces = []





