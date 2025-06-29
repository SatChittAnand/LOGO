import turtle as t
t.pen()
t.bgcolor("black")
colors=["red" , "green" , "yellow" , "blue" , "cyan" , "orange" , "brown" , "aqua" , "gray"]
name=t.textinput("Enter your name" , "Enter your  name")
s=int(t.numinput("Number of sides"  ,"How many sides you want(1-20)" , 7 , 1 , 20))
for i in range(200):
    t.pencolor(colors[i%s%10])
    t.penup()
    t.forward(i*5)
    t.pendown()
    t.write(name , font=("", int((i*2+4)/4) , "bold"))
    t.left(360/s-9)
done()