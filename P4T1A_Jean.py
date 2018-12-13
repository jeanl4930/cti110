#CTI110
#P4T1a
#Jean
#12/02/18


import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(2)
t.shape("turtle")

for i in range(4):
    t.color('red')
    t.forward(100)
    t.left(90)

for i in range (3):
    t.color('blue')
    t.forward(100)
    t.left(120)

win.mainloop()
