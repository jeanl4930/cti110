import turtle

"""This teaches our program how to make triangles
of a color and x,y coordinates we choose
"""
def make_triangle(x, y, color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.begin_fill()
  turtle.color(color)
  turtle.pendown()
  for count in range(3):
    turtle.forward(50)
    turtle.left(120)
  turtle.end_fill()

"""This teaches our program how to make triangles of a color and x,y squares we choose
"""
def make_square(x, y, color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.begin_fill()
  turtle.color(color)
  turtle.pendown()
  for count2 in range(3):
    turtle.forward(50)
    turtle.left(90)
  turtle.end_fill()


turtle.shape("turtle")
turtle.penup()
turtle.goto(0,-150)
turtle.color('#ff6600')
turtle.begin_fill()
turtle.pendown()
turtle.circle(150)
turtle.penup()
turtle.end_fill()
turtle.left(180)
# The Teeth:
make_triangle(-35, -20, '#ffffff')
make_triangle(0, -20, '#ffffff')
make_triangle(65, -20, '#ffffff')
make_triangle(95, -20, '#ffffff')
make_triangle(35, -20, '#ffffff')
turtle.left(180)
# The Eyes:
make_triangle(-70, 50, '#ff0000')
make_triangle(25, 50, '#ff0000')
# The Stump:
make_square(-25, 150, '#000000')

turtle.penup()
turtle.goto(-100,-185)
turtle.write('Happy Halloween!',('Arial', 24, 'normal'))
turtle.goto(-170,150)
turtle.write('JeanL', ('Arial', 24, 'normal'))
turtle.goto(85,150)
turtle.write('CTI110', ('Arial', 24, 'normal'))
turtle.goto(-120,-185)
turtle.left(180)
