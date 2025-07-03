import turtle
from turtle import Screen

s = Screen()
s.bgcolor("white")

#blue box code
a = turtle.Turtle()
a.pensize(5)
a.color("#00BFFF")
a.speed(10)
a.begin_fill()
a.right(45)
a.backward(200)
a.right(45)
a.forward(285)
a.right(45)
a.backward(200)
a.end_fill()
a.hideturtle()

#green box code
b = turtle.Turtle()
b.pensize(5)
b.color("#228B22")
b.begin_fill()
b.left(45)
b.forward(100)
b.left(105)
b.forward(193)
b.circle(30 , 120)
b.end_fill()
b.hideturtle()

#red box code
c = turtle.Turtle()
c.pensize(5)
c.color("#FF4040")
c.begin_fill()
c.left(-45)
c.forward(100)
c.left(-105)
c.forward(193)
c.circle(-30 ,120)
c.end_fill()
c.hideturtle()


#yellow box code
d = turtle.Turtle()
d.pensize(5)
d.color("#FFB90F")
d.begin_fill()
d.left(-45)
d.forward(100)
d.right(-75)
d.forward(80)
d.circle(35 , 120)
d.forward(80)
d.right(-75)
d.forward(100)
d.end_fill()
d.hideturtle()

#playstore name
e = turtle.Turtle()
e.hideturtle()
e.penup()
e.goto(-80 , -200)
e.pendown()
e.color("black")
e.speed(10)
e.write("Play Store" , font = ("ENGLISH" , 20 , "bold"))

turtle.done()