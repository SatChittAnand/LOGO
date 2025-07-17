from turtle import Screen , Turtle

def sp():
    for i in range(360):
        t.circle(i , 8)
        t.color("snow")
        t.width(20)

screen = Screen()
screen.bgcolor("black")
screen.tracer(False)

t = Turtle()

for angle in range(750):
    t.reset()
    t.hideturtle()
    t.left(angle)
    sp()
    screen.update()

screen.tracer(True)
screen.mainloop()

turtle.done()