import math
import turtle
 
win = turtle.Screen()
win.bgcolor("white")
 
# coordinate setting
win.setworldcoordinates(0, -2, 3600, 2)
t = turtle.Turtle()
 
# Draw a vertical line
t.goto(0, 2)
t.goto(0, -2)
t.goto(0, 0)
 
# Draw a Horizontal line
t.goto(3600, 0)
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("blue")
t.pensize(4)
 
# Generate wave form
for x in range(3600):
    y = math.sin(math.radians(x))
    t.goto(x, y)