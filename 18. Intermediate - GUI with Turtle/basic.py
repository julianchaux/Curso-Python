from turtle import Turtle, Screen

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90) #grados

my_screen = Screen()
my_screen.exitonclick()