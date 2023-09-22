from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_screen = Screen()

def move_forwards():
    my_turtle.forward(10)

my_screen.listen()
my_screen.onkey(key="space", fun=move_forwards)
my_screen.exitonclick()