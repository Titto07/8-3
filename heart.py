import turtle
from random import randint
turtle.Screen().bgcolor("#942727")
turtle.Screen().setup(width=1.0,height=1.0,startx=None,starty=None)
meow = turtle.Turtle()
meow.color("#660000")
meow.speed(0)
meow.up()
meow.down()
for i in range (60):
 meow.circle(300,20,5)
 meow.lt(520)
 meow.circle(300,20,5)
 meow.rt(160)
 meow.rt(270)    
turtle.colormode(255) 
while True:
    meow.color(randint(0, 255),randint(0, 255),randint(0, 255))
    meow.begin_fill()
    meow.left(140)
    meow.forward(113) 
    for i in range(200):
          meow.right(1)
          meow.forward(1)
    meow.left(120)
    for i in range(200):
          meow.right(1)
          meow.forward(1)
    meow.forward(121)
    meow.end_fill()
    meow.penup()
    meow.goto(randint(-600,500), randint(-300,300))
    meow.pendown()
