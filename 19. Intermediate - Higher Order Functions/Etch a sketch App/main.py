from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_screen = Screen()

def move_forwards():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def turn_left():
    my_turtle.left(10)

def turn_right():
    my_turtle.right(10)

def reset():
    my_screen.resetscreen()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=reset)
my_screen.exitonclick()