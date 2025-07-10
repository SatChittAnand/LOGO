from turtle import *
import colorsys as cs
bgcolor("black")
tracer(10)
pensize(4)
h = 0.3

def draw(angle , n):
    circle(n/2 , 30)
    left(angle)
    circle(n/2 , 30)

goto(0 , 0)

for i in range(280):
    c = cs.hsv_to_rgb(h , 1 , 1)
    h += 0.005
    color(c)
    draw(60 , i)
    draw(90 , i)
    draw(120 , i*2)
    draw(180 , i)
    draw(360 , i)

done()