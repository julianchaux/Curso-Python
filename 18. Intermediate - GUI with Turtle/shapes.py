from turtle import Turtle, Screen
from random import choice

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

my_turtle = Turtle()
my_turtle.shape("turtle")

colors = ["blue", "dark green", "dark green", "dark magenta", "lime"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_side_in in range(3, 11):
    my_turtle.color(choice(colors))
    draw_shape(shape_side_in)

my_screen = Screen()
my_screen.exitonclick()