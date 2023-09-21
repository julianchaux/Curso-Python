from turtle import Screen
import turtle as t
import random

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

my_turtle = t.Turtle()
my_turtle.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


directions = [0, 90, 180, 270]
my_turtle.pensize(10)
my_turtle.speed("fastest")

for _ in range(200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))

print(random_color())

my_screen = Screen()
my_screen.exitonclick()