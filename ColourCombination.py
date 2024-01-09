from turtle import *
import colorsys as cs 
bgcolor("black")
speed(100000)
width(1)

def square(x):
    for i in range(4):
        forward(x)
        left(90)

def shape(x):
    forward (x)
    left(45)
    forward(x)
    right(60)
    width(3)
    square(x)
    width(1)
    right(165)
    forward(x)
    left(45)
    forward(x)
  

h = 0.0
for i in range (500):
    color (cs.hsv_to_rgb(h,1,1))
    circle(50,4)
    right(90)
    shape(70)
    right(135)
    h+=0.0111
