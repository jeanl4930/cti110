import turtle
win = turtle.Screen()
t = turtle.Turtle()


turtle.shape("arrow")
t.pensize(2)
t.shape("turtle")

t.color('yellow')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

t.color('pink')
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)



for i in range(4):
    t.color('red')
    t.forward(100)
    t.left(90)

for i in range (3):
    t.color('blue')
    t.forward(100)
    t.left(120)

win.mainloop()
