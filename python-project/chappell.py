import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Chappell Roan Inspired Drawing")

# Create turtle
cr = turtle.Turtle()
cr.speed(5)
cr.pensize(3)

# Draw face (circle)
cr.penup()
cr.goto(0, -100)
cr.pendown()
cr.color("peachpuff")
cr.begin_fill()
cr.circle(100)
cr.end_fill()

# Draw pink hair
cr.penup()
cr.goto(-100, 80)
cr.pendown()
cr.color("hotpink")
cr.begin_fill()
cr.setheading(60)
cr.circle(120, 120)
cr.goto(100, 80)
cr.goto(-100, 80)
cr.end_fill()

# Draw heart sunglasses
def draw_heart_sunglass(x, y):
    cr.penup()
    cr.goto(x, y)
    cr.pendown()
    cr.color("black", "red")
    cr.begin_fill()
    cr.setheading(0)
    cr.forward(20)
    cr.circle(10, 180)
    cr.left(90)
    cr.circle(10, 180)
    cr.forward(20)
    cr.goto(x, y)
    cr.end_fill()

draw_heart_sunglass(-50, 30)
draw_heart_sunglass(20, 30)

# Bridge between glasses
cr.penup()
cr.goto(-10, 35)
cr.pendown()
cr.pensize(5)
cr.forward(20)
cr.pensize(3)

# Draw mouth
cr.penup()
cr.goto(-30, -30)
cr.setheading(-60)
cr.pendown()
cr.color("red")
cr.circle(30, 120)

# Hide turtle
cr.hideturtle()

# Keep window open
turtle.done()