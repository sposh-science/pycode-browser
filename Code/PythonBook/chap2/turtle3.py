from turtle import *

def draw_rectangle():
    for k in range(4):
        a.forward(50)
        a.left(90)
  

a = Pen()	# Creates a graphics window

for k in range(36):
  draw_rectangle()
  a.left(10)
raw_input()