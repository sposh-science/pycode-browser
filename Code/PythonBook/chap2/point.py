class Point:
  xpos = 0
  ypos = 0
  
  def __init__(self, x=0, y=0):
    self.xpos = x
    self.ypos = y

  def __str__(self):
    return 'Point at (%f,%f)'%(self.xpos, self.ypos)

  def __add__(self, other):
    xpos = self.xpos + other.xpos
    ypos = self.ypos + other.ypos
    res = Point(xpos,ypos)
    return res

  def __sub__(self, other):
    import math
    dx = self.xpos - other.xpos
    dy = self.ypos - other.ypos
    return math.sqrt(dx**2+dy**2)

  def dist(self):
    import math
    return math.sqrt(self.xpos**2 + self.ypos**2)
