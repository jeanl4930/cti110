#CTI110
#P4T1b
#Jean
#12/02/18


import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)
t.shape("turtle")

for i in range(2):
    t.backward(100)
    t.right(90)
    
t.penup()
t.backward(250)
t.pendown()
t.forward(100)  
t.penup()
t.backward(50)
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.penup()
t.forward(30)
t.pendown()
t.circle(1)
t.penup()
t.backward(105)
t.pendown()
t.circle(1)
t.penup()
t.backward(25)

win.mainloop()
