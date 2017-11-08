#Denver Wydermyer
#Computer Programming
#9/18/17


import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")

sammy = turtle.Turtle()

sammy.shape("turtle")
sammy.speed(14)
sammy.fillcolor('white')
sammy.pensize(7)
sammy.pencolor("black")

abe = turtle.Turtle()

def draw_spiral():
    print(range(5, 345, 2))
    sammy.up()
    for size in range(5, 135, 2):
        sammy.begin_fill()
        sammy.stamp()
        sammy.forward(size)
        sammy.right(50)
        sammy.end_fill()

            
abe.shape("circle")
abe.speed(12)
abe.fillcolor('orange')
abe.pensize(9)
abe.pencolor("black")

def draw_circle():
    print(range(7, 123, 4))
    abe.down()
    for size in range(5, 135, 2):
          abe.begin_fill()
          abe.stamp()
          abe.forward(size)
          abe.right(75)
          abe.end_fill()
draw_spiral()
