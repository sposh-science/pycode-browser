from point import *

class colPoint(Point):	#colPoint inherits Point
  color = 'black'

  def __init__(self,x=0, y=0, col='black'):
    Point.__init__(self,x,y)
    self.color = col

  def __str__(self):
    return '%s colored Point at (%f,%f)'%(self.color,self.xpos, self.ypos)

