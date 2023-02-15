import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="w", fun=player.player_move)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 23:
            print("crash")
            scoreboard.game_over()
            game_is_on = False

    # Detect finish line
    if player.ycor() >= 270:
        scoreboard.update_level()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()
