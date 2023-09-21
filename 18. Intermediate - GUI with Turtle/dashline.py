from turtle import Turtle, Screen

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

for _ in range(10):
    my_turtle.forward(10)
    my_turtle.penup()   #Levanta el lapiz
    my_turtle.forward(10)
    my_turtle.pendown() #Baja el lapiz

my_screen = Screen()
my_screen.exitonclick()