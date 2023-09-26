import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

"""Step1: Create a turtle player that starts at the bottom of the screen and listen for the "Up" 
keypress to move the turtle north."""
player = Player()

"""Step2: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 
No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
Hint: generate a new car only every 6th time the game loop runs."""
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()